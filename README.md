# Agentic Payments Readiness Dataset 2026

**Can an AI agent actually pay through today's payment providers?** This dataset scores 13 payment and financial-infrastructure providers against their own official documentation on 7 dimensions: agent SDK/API, MCP server, agent payment protocols (x402, AP2, ACP, Visa TAP, Mastercard Agent Pay), developer sandbox access, spending guardrails, payment rails, and documentation/pricing transparency.

- **Providers (13):** Adyen, Airwallex, Checkout.com, Circle, Coinbase, Crossmint, Mastercard, PayPal, Payman, Skyfire, Stripe, Visa, Wise
- **Rows:** 185 checks. Each row has an evidence URL on the provider's own domain or official repo, a verbatim quote, and an access date.
- **Version:** v1.1, published 2026-09-28 (evidence accessed 2026-09-27 to 2026-09-28)
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Full report (with key findings and changelog):** https://pinkwallet.com/agentic/research/agentic-payments-readiness-report-2026/

## Files

| File | What it is |
|---|---|
| `data/agentic-payments-readiness-2026.csv` | The scoring data: one row per provider × check |
| `data/dataset-jsonld.json` | schema.org `Dataset` metadata |
| `METHODOLOGY.md` | Dimensions, checks, scoring rules, evidence rules |
| `CITATION.cff` | How to cite this dataset |

## CSV columns

`company, dimension_id, dimension_name, check_id, check_description, result, verdict_symbol, evidence_status, evidence_url, verbatim_quote, accessed_date, reverified_2026-09-28, notes`

`result` values: `yes`, `partial`, `no`, `not verified` (we could not find a self-described statement; this does **not** mean the capability is absent), `not applicable`, `pricing: not found`, `pricing: general rates`.

## Key findings (v1.1)

1. Every provider in the sample has shipped something agent-facing, but a capability that is official, money-moving and self-serve all at once is rare.
2. MCP servers are proliferating, but most are read/search tools, not payment tools.
3. x402 and ACP tie on self-described adopters in this sample (four each); no provider self-describes an AP2 integration in its own docs as of 2026-09-28.
4. Human-in-the-loop confirmation is documented by name for a minority of providers (e.g. Stripe's MCP write actions; Circle's OTP-gated spend-limit changes).
5. Agent-specific pricing is essentially undisclosed (11 of 13 providers: not found).

## Conflict of interest

Published by PinkWallet, which is building agentic-payments products ([Pink Agentic AI Payment](https://pinkwallet.com/agentic), early access). PinkWallet is **not scored** and does not appear in the data.

## Corrections

If a row is wrong, open an issue with the correct URL and quote. Accepted corrections are versioned and listed in the report's changelog.
