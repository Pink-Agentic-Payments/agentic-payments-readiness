# Agentic Payments Readiness Dataset 2026

**Can an AI agent actually pay through today's payment providers?** This dataset scores 16 payment and financial-infrastructure providers against their own official documentation on 7 dimensions: agent SDK/API, MCP server, agent payment protocols (x402, AP2, ACP, Visa TAP, Mastercard Agent Pay), developer sandbox access, spending guardrails, payment rails, and documentation/pricing transparency.

Also available on Hugging Face: https://huggingface.co/datasets/Agentic-Payment/agentic-payments-readiness (with the dataset viewer).

- **Providers (16):** Adyen, Airwallex, Checkout.com, Circle, Coinbase, Crossmint, Mastercard, Mollie, PayPal, Payman, Skyfire, Square, Stripe, Tempo, Visa, Wise
- **Rows:** 228 checks (185 from v1.1 + 43 added in v1.2). Each row has an evidence URL on the provider's own domain or official repo, a verbatim quote, and an access date.
- **Version:** v1.2, published 2026-09-29 (v1.2 additions accessed 2026-09-29; v1.1 baseline accessed 2026-09-27 to 2026-09-28). v1.1 remains available unmodified at the [`v1.1` tag](https://github.com/Pink-Agentic-Payments/agentic-payments-readiness/releases/tag/v1.1).
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Full report (with key findings and changelog):** https://pinkwallet.com/agentic/research/agentic-payments-readiness-report-2026/

## What's new in v1.2 (2026-09-29)

Added 3 providers — Mollie, Square, Tempo (13 → 16 providers, 42 scored rows + 1 informational row). This is additive only: every v1.1 row is unchanged, and the `v1.1` git tag/release still points at the original 13-provider/185-row snapshot.

- All 3 new providers have an official, vendor-hosted MCP server (`mcp.mollie.com`, `mcp.squareup.com`, `mcp.tempo.xyz`) — vs. 6 of 13 in the v1.1 baseline.
- Only 1 of the 3 (Tempo) documents a genuine configurable spend cap: wallet access keys carry independent per-key spending limits plus a `--max-spend` flag and `--dry-run` cost preview.
- 0 of the 3 self-declare x402/AP2/ACP/Visa TAP/Mastercard Agent Pay integration. Tempo instead pushes its own "Machine Payments Protocol" (MPP, co-authored with Stripe) — recorded as an informational D3.x row, not scored under the fixed D3 list.
- All 3 publish some pricing info (Mollie/Square reuse their standard card rates; Tempo is the first provider in this dataset scored `pricing: agent-specific`, with published sub-cent per-request fees) — vs. 2 of 13 in v1.1.
- The 3 additions lag the v1.1 median on protocol self-declaration (0 of 3 vs. 8 of 13) but lead on pricing transparency (3 of 3 vs. 2 of 13 "some pricing" / 11 of 13 "not found").

## Files

| File | What it is |
|---|---|
| `data/agentic-payments-readiness-2026.csv` | The scoring data: one row per provider × check |
| `data/dataset-jsonld.json` | schema.org `Dataset` metadata |
| `METHODOLOGY.md` | Dimensions, checks, scoring rules, evidence rules |
| `CITATION.cff` | How to cite this dataset |
| `CHANGELOG.md` | Version history |
| `evidence/quote-check-v1.2-additions.csv` | Mechanical quote-verification log for the v1.2 additions (48/48 quoted claims passed) |
| `scripts/quote_checker.py` | The script used to produce that verification log |

## CSV columns

`company, dimension_id, dimension_name, check_id, check_description, result, verdict_symbol, evidence_status, evidence_url, verbatim_quote, accessed_date, reverified_2026-09-28, notes`

`result` values: `yes`, `partial`, `no`, `not verified` (we could not find a self-described statement; this does **not** mean the capability is absent), `not applicable`, `pricing: not found`, `pricing: general rates`, `pricing: agent-specific`.

The `reverified_2026-09-28` column reflects the v1.1 same-day re-verification pass; v1.2 rows (Mollie, Square, Tempo) are marked `new in v1.2` since they were not part of that round.

## Key findings (v1.1, 13 providers)

1. Every provider in the sample has shipped something agent-facing, but a capability that is official, money-moving and self-serve all at once is rare.
2. MCP servers are proliferating, but most are read/search tools, not payment tools.
3. x402 and ACP tie on self-described adopters in this sample (four each); no provider self-describes an AP2 integration in its own docs as of 2026-09-28.
4. Human-in-the-loop confirmation is documented by name for a minority of providers (e.g. Stripe's MCP write actions; Circle's OTP-gated spend-limit changes).
5. Agent-specific pricing is essentially undisclosed (11 of 13 providers: not found).

These five findings describe the original 13-provider v1.1 sample only and were not recomputed against the 16-provider v1.2 set.

## Conflict of interest

Published by PinkWallet. Pink Agentic AI Payments (by PinkWallet, early access) is the approval layer between AI agents and company money: plain-language rules, per-agent budgets and human approvals decide each payment before a single-use card or bank transfer is issued. PinkWallet is **not scored** and does not appear in the data.

Try the interactive prototype (sample companies, no real money moves): https://claude.ai/public/artifacts/TpsUqLKnqZ3jHpghEGcimx

## Corrections

If a row is wrong, open an issue with the correct URL and quote. Accepted corrections are versioned and listed in the report's changelog.
