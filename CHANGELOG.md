# Changelog

## v1.2 — 2026-09-29

Additive release. Added 3 providers: Mollie, Square, Tempo (13 → 16 providers; 185 → 228 rows: 42 scored rows + 1 informational D3.x row for Tempo's Machine Payments Protocol). Every v1.1 row is unchanged; the `v1.1` tag/release still points at the original 13-provider/185-row snapshot.

- All 3 new providers have an official, vendor-hosted MCP server.
- 1 of 3 (Tempo) documents a configurable per-key spend limit.
- 0 of 3 self-declare x402/AP2/ACP/Visa TAP/Mastercard Agent Pay.
- All 3 publish some pricing; Tempo is the first `pricing: agent-specific` row in this dataset.
- Evidence: `evidence/quote-check-v1.2-additions.csv`, mechanically verified 48/48 quoted claims PASS via `scripts/quote_checker.py`.

## v1.1 — 2026-09-28

Initial public release. 13 providers × 7 dimensions, 185 rows.
