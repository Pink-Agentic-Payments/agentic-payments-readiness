#!/usr/bin/env python3
"""Mechanical quote checker for scores-v1.2-additions.csv.

For every row: fetch the evidence_url (curl + browser UA; Playwright render as
fallback if the curl body looks too thin / JS-shell-only), normalise whitespace/
quotes/dashes on both the page text and each verbatim quote embedded in
evidence_quote_or_note, and confirm every quote is a substring of the page.
Rows whose evidence_quote_or_note contains no quoted ("...") segment (i.e. a
pure absence-of-evidence note) are recorded as PASS/no-quote-to-check.
"""
import csv
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).parent
CSV_IN = HERE / "scores-v1.2-additions.csv"
CSV_OUT = HERE / "quote-check-results.csv"

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0 Safari/537.36")

QUOTE_RE = re.compile(r'«([^»]{8,})»')

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


def fetch_curl(url: str) -> str:
    try:
        out = subprocess.run(
            ["curl", "-s", "-A", UA, "-L", "--max-time", "30", url],
            capture_output=True, timeout=40,
        )
        return out.stdout.decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"curl failed for {url}: {e}", file=sys.stderr)
        return ""


def fetch_playwright(url: str) -> str:
    try:
        from playwright.sync_api import sync_playwright
    except Exception as e:
        print(f"playwright unavailable: {e}", file=sys.stderr)
        return ""
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(user_agent=UA)
            page.goto(url, timeout=30000, wait_until="networkidle")
            content = page.content()
            browser.close()
            return content
    except Exception as e:
        print(f"playwright render failed for {url}: {e}", file=sys.stderr)
        return ""


def get_page_text(url: str, cache: dict) -> str:
    if url in cache:
        return cache[url]
    html = fetch_curl(url)
    text = normalise(html_to_text(html))
    # A JS-shell-only page (Next.js error shell, or curl body under ~1.5KB of
    # rendered text) is treated as "not found" -> retry with Playwright render.
    if len(text) < 1500:
        rendered = fetch_playwright(url)
        if rendered:
            rendered_text = normalise(html_to_text(rendered))
            if len(rendered_text) > len(text):
                text = rendered_text
    cache[url] = text
    return text


def main():
    rows = list(csv.DictReader(CSV_IN.open(encoding="utf-8")))
    page_cache = {}
    results = []
    n_pass = 0
    for row in rows:
        url = row["evidence_url"].strip()
        note = row["evidence_quote_or_note"]
        quotes = QUOTE_RE.findall(note)
        page_text = get_page_text(url, page_cache)
        if not quotes:
            results.append({
                **{k: row[k] for k in ["company", "check_id", "evidence_url"]},
                "quote_checked": "",
                "status": "PASS",
                "detail": "no verbatim quote in notes (absence-based / methodology note only)",
            })
            n_pass += 1
            continue
        for q in quotes:
            nq = normalise(q)
            ok = nq in page_text
            status = "PASS" if ok else "FAIL"
            if ok:
                n_pass += 1
            results.append({
                "company": row["company"],
                "check_id": row["check_id"],
                "evidence_url": url,
                "quote_checked": q,
                "status": status,
                "detail": "" if ok else "normalised quote not found as substring of fetched page text",
            })

    with CSV_OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["company", "check_id", "evidence_url", "quote_checked", "status", "detail"])
        w.writeheader()
        w.writerows(results)

    total = len(results)
    failed = [r for r in results if r["status"] == "FAIL"]
    print(f"Checked {total} entries across {len(rows)} CSV rows.")
    print(f"PASS: {total - len(failed)}  FAIL: {len(failed)}")
    if failed:
        print("Failing rows:")
        for r in failed:
            print(f"  {r['company']} {r['check_id']}: {r['quote_checked'][:80]!r} @ {r['evidence_url']}")
        sys.exit(1)
    print("100% pass.")


if __name__ == "__main__":
    main()
