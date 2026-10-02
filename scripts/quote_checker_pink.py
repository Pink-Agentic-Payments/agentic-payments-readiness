#!/usr/bin/env python3
"""Quote checker for the v1.3 Pink Agentic AI Payments rows.

Fetches each row's evidence_url live, normalises whitespace/quotes/dashes on
both the page text and the row's verbatim_quote, and confirms the quote is a
substring of the page. Rows with an empty verbatim_quote (result: not
verified / pricing: not found) are recorded as PASS/no-quote-to-check, same
convention as scripts/quote_checker.py.
"""
import csv
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).parent
CSV_IN = HERE.parent / "data" / "agentic-payments-readiness-2026.csv"
CSV_OUT = HERE.parent / "evidence" / "quote-check-v1.3-pink.csv"

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0 Safari/537.36")

DASH_CHARS = "‐‑‒–—―−"
QUOTE_CHARS = "‘’‚‛“”«»"


def normalise(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    for ch in DASH_CHARS:
        text = text.replace(ch, "-")
    for ch in QUOTE_CHARS:
        text = text.replace(ch, '"' if ch in "“”«»" else "'")
    text = text.replace("&nbsp;", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def html_to_text(html: str) -> str:
    html = re.sub(r"<script[\s\S]*?</script>", " ", html)
    html = re.sub(r"<style[\s\S]*?</style>", " ", html)
    text = re.sub(r"<[^>]+>", " ", html)
    text = (text.replace("&amp;", "&").replace("&quot;", '"')
                .replace("&#39;", "'").replace("&nbsp;", " "))
    return text


def fetch(url: str) -> str:
    try:
        out = subprocess.run(
            ["curl", "-s", "-A", UA, "-L", "--max-time", "30", url],
            capture_output=True, timeout=40,
        )
        return out.stdout.decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"fetch failed for {url}: {e}", file=sys.stderr)
        return ""


def get_page_text(url: str, cache: dict) -> str:
    if url in cache:
        return cache[url]
    text = normalise(html_to_text(fetch(url)))
    cache[url] = text
    return text


def extract_quotes(raw: str):
    """Pull the double-quoted segment(s) out of a verbatim_quote field.
    Falls back to the whole field (minus a leading JSON-snippet marker) for
    rows whose quote is a raw JSON fragment rather than prose in quotes."""
    quotes = re.findall(r'"([^"]{6,})"', raw)
    if quotes:
        return quotes
    if raw.strip():
        return [raw.strip()]
    return []


def main():
    rows = [r for r in csv.DictReader(CSV_IN.open(encoding="utf-8"))
            if r["company"] == "Pink Agentic AI Payments"]
    cache = {}
    results = []
    for row in rows:
        url = row["evidence_url"].strip()
        quote_field = row["verbatim_quote"]
        quotes = extract_quotes(quote_field)
        page_text = get_page_text(url, cache)
        if not quotes:
            results.append({
                "company": row["company"], "check_id": row["check_id"], "evidence_url": url,
                "quote_checked": "", "status": "PASS",
                "detail": "no verbatim quote in row (not verified / pricing: not found)",
            })
            continue
        for q in quotes:
            nq = normalise(q.replace("...", "").strip(". "))
            ok = nq in page_text if nq else False
            # ellipsised/truncated JSON fragments: check each non-empty segment
            if not ok and "..." in q:
                segs = [normalise(s) for s in q.split("...") if s.strip()]
                ok = all(s in page_text for s in segs)
            status = "PASS" if ok else "FAIL"
            results.append({
                "company": row["company"], "check_id": row["check_id"], "evidence_url": url,
                "quote_checked": q, "status": status,
                "detail": "" if ok else "normalised quote not found as substring of fetched page text",
            })

    CSV_OUT.parent.mkdir(exist_ok=True)
    with CSV_OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["company", "check_id", "evidence_url", "quote_checked", "status", "detail"])
        w.writeheader()
        w.writerows(results)

    total = len(results)
    failed = [r for r in results if r["status"] == "FAIL"]
    print(f"Checked {total} entries across {len(rows)} Pink CSV rows.")
    print(f"PASS: {total - len(failed)}  FAIL: {len(failed)}")
    if failed:
        print("Failing rows:")
        for r in failed:
            print(f"  {r['check_id']}: {r['quote_checked'][:90]!r} @ {r['evidence_url']}")
        sys.exit(1)
    print("100% pass.")


if __name__ == "__main__":
    main()
