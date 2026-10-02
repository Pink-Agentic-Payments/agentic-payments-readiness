# Changelog

## v1.3 — 2026-10-02

Added the publisher (Pink Agentic AI Payments) as a self-scored row under the same methodology; titles updated; no other company's data changed.

- Added 17 rows for Pink Agentic AI Payments (D1.1–D7.2), self-scored under the identical 7-dimension methodology and evidence rules used for the other 16 companies, labeled "publisher; self-scored; sandbox stage."
- Titles updated to include "Pink Agentic AI Payments" (README H1, METHODOLOGY.md, CITATION.cff, `data/dataset-jsonld.json`) while keeping the words "Agentic Payments Readiness" unchanged.
- Added a "How Pink Agentic AI Payments compares" section (sourced bullets + guardrail-depth list + "where Pink is behind"), replacing the earlier "Where Pink fits (self-assessed, not scored)" section.
- Added Pink as the first row in both results tables (README.md and METHODOLOGY.md), and a "Company notes" entry for Pink in METHODOLOGY.md.
- Evidence: `evidence/quote-check-v1.3-pink.csv`, mechanically verified 26/26 quoted claims PASS via `scripts/quote_checker_pink.py`.
- The `v1.1` and `v1.2` tags/releases are untouched.

## v1.2 — 2026-09-29

Additive release. Added 3 providers: Mollie, Square, Tempo (13 → 16 providers; 185 → 228 rows: 42 scored rows + 1 informational D3.x row for Tempo's Machine Payments Protocol). Every v1.1 row is unchanged; the `v1.1` tag/release still points at the original 13-provider/185-row snapshot.

- All 3 new providers have an official, vendor-hosted MCP server.
- 1 of 3 (Tempo) documents a configurable per-key spend limit.
- 0 of 3 self-declare x402/AP2/ACP/Visa TAP/Mastercard Agent Pay.
- All 3 publish some pricing; Tempo is the first `pricing: agent-specific` row in this dataset.
- Evidence: `evidence/quote-check-v1.2-additions.csv`, mechanically verified 48/48 quoted claims PASS via `scripts/quote_checker.py`.

## v1.1 — 2026-09-28

Initial public release. 13 providers × 7 dimensions, 185 rows.
