## Methodology (Pink Agentic AI Payments)

We evaluated 13 payment and financial infrastructure providers against 7 dimensions, each broken into 2–4 binary or ternary checks (23 distinct check types; some checks don't apply to every company, e.g. a card network isn't scored on its own card rail). v1.2 added 3 more providers (16 total); v1.3 added the publisher, Pink Agentic AI Payments, as a self-scored row under the same methodology (16 providers + the publisher).

**The seven dimensions:**

- **D1 — Agent API/SDK**: is there a publicly documented, agent-specific SDK/toolkit (D1.1), and is it GA or still beta/preview (D1.2)?
  **How Pink does it:** publishes a documented REST API and MCP server for agents ([developers](https://pinkwallet.com/agentic/developers/)); D1.2 is scored "partial" because every developer page states "Sandbox live... Production is not yet available" — there is no GA agent API yet.
- **D2 — MCP server**: does the company itself (not a community project) host an MCP server (D2.1), and does its documentation state whether that server can move money or is read/search-only (D2.2)?
  **How Pink does it:** hosts its own MCP server at `agentic-sandbox.pinkwallet.com/mcp`; this report's own `tools/list` call against it on 2026-10-01 returned exactly 7 tools including `pink.request_payment`, i.e. it initiates payments rather than only reading data — see [tools-reference](https://pinkwallet.com/agentic/developers/tools-reference/).
- **D3 — Agent payment protocol support**: does the company's own documentation or repo self-describe support for x402, AP2, ACP, or Visa TAP/Mastercard Agent Pay? A protocol's own operator (Visa for TAP, Mastercard for Agent Pay) is not scored against its own protocol.
  **How Pink does it:** does not implement x402, AP2, ACP, Visa TAP, or Mastercard Agent Pay — all four are "no" in Pink's own row. Instead, Pink runs its own rule engine (ordered rules, circuit breakers, default-block) in front of card and bank rails; see ["How Pink decides a payment"](#how-pink-decides-a-payment) below and [policy-rules-reference](https://pinkwallet.com/agentic/developers/policy-rules-reference/).
- **D4 — Developer sandbox**: is there a self-serve signup/sandbox, or does access require contacting sales?
  **How Pink does it:** a workspace can be created with a single unauthenticated `POST /v1/sandbox/workspaces` call, no sales contact — this report created one live; see ["Try Pink Agentic AI Payments in 2 minutes"](https://github.com/Pink-Agentic-Payments/agentic-payments-readiness#try-pink-agentic-ai-payments-in-2-minutes) in the README.
- **D5 — Guardrails**: configurable spend limits (D5.1), human-confirmation or delegated/one-time credentials (D5.2), identity/compliance screening such as KYA or OFAC (D5.3).
  **How Pink does it:** D5.1/D5.2 are "yes" — per-agent monthly budgets, a per-payment cap, and a company-wide daily ceiling across all agents, plus named-approver/quorum human confirmation and single-use credentials expiring 15 minutes after issue ([policy-rules-reference](https://pinkwallet.com/agentic/developers/policy-rules-reference/), [security-model](https://pinkwallet.com/agentic/developers/security-model/)). D5.3 is "not verified" — identity/compliance screening (KYA, OFAC) is not documented in the pages reviewed.
- **D6 — Payment rails**: card (D6.1), bank/ACH/wire (D6.2), stablecoin/crypto (D6.3) — specifically for agent-initiated payments, not the company's general product.
  **How Pink does it:** D6.1/D6.2 are "yes" — a single-use test-BIN virtual card or a sandbox ACH bank-transfer object, both confirmed in this report's own live payment calls (see the trial section in the README). D6.3 (stablecoin) is "not verified" — not documented in the pages reviewed.
- **D7 — Documentation and pricing transparency**: can the core agent docs be read without login (D7.1), and is pricing for agent-specific usage public (D7.2)?
  **How Pink does it:** D7.1 is "yes" — the developer docs at [pinkwallet.com/agentic/developers/](https://pinkwallet.com/agentic/developers/) are readable without login. D7.2 is "not verified" — no published production pricing was found.

**Evidence rule:** every check is tied to an evidence URL (the company's own domain or official GitHub org — never a search-engine summary or a third party naming the company as a partner) and, for every "yes" or "partial" result, a verbatim quote copied from that source. Checks that could not be resolved are marked **not verified** — this is not the same as "no." A page returning 403/404/526, requiring login, or simply not yet deep-dived into its sub-pages is recorded as "not verified," not scored as absent. All fetches for this v1.1 pass were performed on 2026-09-28.

**Evidence states used in the CSV:** `yes`, `partial`, `no`, `not verified`, `not applicable`, and for D7.2 specifically: `pricing: agent-specific`, `pricing: general rates`, `pricing: not found`.

## Results

Legend: **✓** yes · **◐** partial · **✗** no · **?** not verified · **–** not applicable/no data

### D1–D2, D4–D7 (sub-checks shown in order, separated by "/")

| Company | D1 (SDK/beta) | D2 (MCP/money-out) | D4 (sandbox) | D5 (limits/confirm/screen) | D6 (card/bank/stablecoin) | D7 (docs/pricing) |
|---|---|---|---|---|---|---|
| **Pink Agentic AI Payments** (publisher; self-scored; sandbox stage) | ✓/◐ | ✓/✓ | ✓ | ✓/✓/? | ✓/✓/? | ✓/? |
| Airwallex | ✓/◐ | ✓/◐ | ◐ | ?/✓/? | ?/?/? | ✓/? |
| Skyfire | ✓/? | ?/? | ✓ | ✓/?/✓ | ✓/✓/✓ | ✓/? |
| Payman | ✓/? | ✓/? | ? | ?/?/? | ? | ◐/? |
| Crossmint | ✓/? | ✓/? | ✓ | ✓/✓/? | ✓/?/✓ | ✓/? |
| Visa | ✓/◐ | ✓/? | ✓ | ?/?/? | ✓/–/? | ✓/? |
| Mastercard | ✓/? | ✓/✗ | ? | ?/?/? | ✓/✓/✓ | ◐/? |
| Adyen | ✓/? | ✓/? | ? | ?/?/? | ? | ✓/? |
| PayPal | ?/◐ | ✓/? | ◐ | ✓/✓/? | ✓/?/? | ✓/? |
| Checkout.com | ?/? | ✓/◐ | ✓ | ? | ? | ✓/? |
| Circle | ✓/? | ✓/✗ | ✓ | ✓/✓/? | ?/?/✓ | ✓/✓ |
| Stripe | ✓/◐ | ✓/✓ | ✓ | ◐/✓/? | ?/?/✓ | ✓/? |
| Coinbase | ✓/? | ?/? | ✓ | ✓/?/✓ | ✗/✗/✓ | ✓/? |
| Wise | ✗/– | ✗/– | ✗ | ? | ?/?/? | ?/? |

*D5 order is limits / human-confirmation / identity screening. D6 order is card / bank / stablecoin. D7 order is docs-without-login / agent-specific pricing.*

### D3 — self-described protocol support

| Company | x402 | AP2 | ACP | Visa TAP / MC Agent Pay |
|---|---|---|---|---|
| **Pink Agentic AI Payments** (publisher; self-scored; sandbox stage) | ✗ | ✗ | ✗ | ✗ |
| Airwallex | ? | ? | ? | ? |
| Skyfire | ? | ? | ? | ? |
| Payman | ? | ? | ? | ? |
| Crossmint | ✓ | ? | ? | ? |
| Visa | – | – | – | ✓ (own protocol) |
| Mastercard | – | – | – | ✓ (own protocol) |
| Adyen | ? | ? | ✓ | ? |
| PayPal | ? | ? | ✓ | ? |
| Checkout.com | ? | ? | ✓ | ? |
| Circle | ✓ | ? | ? | ? |
| Stripe | ✓ | ? | ✓ | ? |
| Coinbase | ✓ | ? | ? | ? |
| Wise | ? | ? | ? | ? |

Note: Adyen also self-describes support for UCP (Universal Commerce Protocol), a protocol not in the original four-protocol methodology; see the CSV row `D3.x UCP`.

Note on the publisher row: Pink Agentic AI Payments rows were scored by the publisher itself (not an independent third party) under the identical methodology and evidence rules used for the other 16 companies, and are labeled "publisher; self-scored; sandbox stage" throughout. See ["How Pink Agentic AI Payments compares"](https://github.com/Pink-Agentic-Payments/agentic-payments-readiness#how-pink-agentic-ai-payments-compares) in the README for the sourced comparison.

## Company notes

**Pink Agentic AI Payments (publisher; self-scored).** Publicly documents an agent-specific REST API and a company-hosted MCP server (`agentic-sandbox.pinkwallet.com/mcp`) that can initiate a single-use card or bank transfer, gated by per-agent monthly budgets, a company daily ceiling, ordered rules with default-block, and named-approver/quorum holds; self-describes no x402, AP2, ACP, Visa TAP, or Mastercard Agent Pay support; is in early access with a public self-serve sandbox, and does not publish production pricing. Identity/compliance screening and stablecoin rails are not documented in the pages reviewed for this check.

**Airwallex.** Documents a dedicated AgentOS MCP endpoint (`mcp.airwallex.com/mcp`) with an explicit "no money-out actions by default" statement and human approval required for write tools, but the skill set is labeled beta rather than GA, and access requires OAuth against an existing production account rather than a fresh self-serve sandbox.

**Skyfire.** Built around an agent-specific identity/token system (KYA) with self-described per-agent spending limits and funding across cards, ACH, and USDC — the most fully self-described guardrail and rail set in this sample outside Circle — though its MCP server and protocol-support pages were not deep-dived this round.

**Payman.** Positions itself on its homepage as agentic-AI banking, and its GitHub org contains a documented Genie MCP bridge, but its technical documentation subdomain (docs.paymanai.com) returned HTTP 526 on every fetch attempt this round, leaving most guardrail and rail checks unverified rather than resolved.

**Crossmint.** Self-describes x402 client support, scoped/revocable card allowances, and one-time/encrypted agent credentials, plus non-custodial stablecoin agent wallets — a broad set of agent-specific guardrail and rail claims backed by verbatim quotes from its own docs.

**Visa.** As the operator of Visa Intelligent Commerce/Trusted Agent Protocol, is treated as not applicable for other companies' protocols; its own protocol page and a dedicated MCP server for integration guidance are both self-serve and publicly documented, but specific spend-limit and human-confirmation mechanisms were not found in the pages fetched this round.

**Mastercard.** Its GitHub-hosted Agent Toolkit is public and MIT-licensed, and Mastercard's own investor-relations release describes Agent Pay for Machines as settling "across cards, accounts and stablecoins" (mastercard.com/global's press page itself 403s to every fetch method we tried, including a browser-rendered check), but developer.mastercard.com is JavaScript-rendered and returned only page titles to this round's fetches, leaving several checks (guardrails, self-serve sandbox) unresolved.

**Adyen.** Self-describes support for both ACP and UCP checkout flows for merchants, and its agentic-commerce documentation is public without login, and it publishes an official MCP server (docs.adyen.com/development-resources/mcp-server); other protocols, guardrail mechanisms, and specific agent-scenario rails were not found in the pages fetched this round.

**PayPal.** Its Agent Ready / ACP integration guide documents card, Apple Pay, and Google Pay as supported payment methods with transaction-amount validation and single-use payment references, and PayPal's official docs state it "developed an MCP server" for merchants (corrected 2026-09-28; the first version said it did not host one), while D1.1's specific SDK details were not directly verified this round.

**Checkout.com.** Hosts an official MCP server described as supporting payment status queries, voids, and payment-link management (a partial, not full, money-movement scope), self-describes ACP support, and offers a self-serve test-account signup, but guardrail and rail-specific pages were not found in the content fetched this round.

**Circle.** Its open-source `circlefin/skills` repo documents per-transaction/daily/weekly/monthly agent-wallet spend limits, OTP-gated limit changes, an x402 seller-integration skill, and stablecoin payments via Circle Wallets — the most fully evidenced guardrail set alongside Skyfire — though several protocol checks (AP2/ACP/Visa-MC) were not found in the repo docs.

**Stripe.** Documents an MCP server with an explicit write/read tool split, human confirmation required before certain write actions such as refunds, x402 and ACP support, and stablecoin payments over MPP/x402; a same-day re-check could not find a verbatim statement that ACP payments settle over card rails specifically (D6.1), so that check is now "not verified" rather than "yes."

**Coinbase.** AgentKit's README states "Every AI Agent deserves a wallet," and its Agentic Wallet CLI documents per-session/per-transaction caps, built-in OFAC screening, and USDC support across five chains; it does not describe card or bank rails for agent wallets (both explicitly "no"), and its Mastercard-Agent-Pay partner mention was downgraded to background-only because Coinbase's own docs don't self-describe that integration.

**Wise.** The clearest "not built for this yet" profile in the sample: the developer-portal URL used in this check returned 404, no MCP server, agent-specific SDK, or self-serve agent sandbox was found, and most other checks are "not verified" because Wise's general merchant-API sandbox is not agent-specific evidence under this methodology.

## What this means for teams deploying AI agents

1. **"Has an MCP server" is not the same as "agents can spend money through it."** Check D2.2 specifically — several officially documented MCP servers in this sample are explicitly read/search-only or capped at void/query operations.
2. **A protocol partner announcement is not the same as a self-described integration.** This report only counts a company's own docs/repo naming a protocol; press-release partner lists (e.g. Mastercard's 30+-partner Agent Pay announcement) are excluded per v1.1 rule 4, and two prior "yes" entries (Coinbase, Crossmint on Visa TAP/MC Agent Pay) were downgraded on that basis.
3. **"Not verified" is a research-coverage gap, not evidence of absence.** A large share of this table's cells are "?" because a page was JS-rendered, gated, or simply not deep-dived this round — treat them as open questions to ask a vendor directly, not as a "no."
4. **Guardrail specifics (spend limits, human confirmation, compliance screening) are the least-documented dimension across the sample.** If spend control is a requirement for your deployment, expect to verify D5 directly with each vendor rather than relying on marketing language like "enterprise-grade security."
5. **Self-serve access and agent-specific pricing are two different questions.** Most vendors let you start building without a sales call (D4), but almost none publish an agent-specific rate card (D7.2) — budget for a sales conversation before production spend, even where the sandbox is open.
6. **Re-verify before you build.** This is a point-in-time snapshot (accessed 2026-09-28); two claims changed between v1.1's draft and this publication after a same-day re-check (see changelog), which is itself evidence that this space is moving fast enough to warrant checking primary sources yourself.

**Applying this with Pink specifically** (the publisher's own row, self-scored under the same rules above): if guardrail depth (D5) and dual card/bank rails (D6) matter more to your deployment than protocol conformance (D3), Pink's sandbox is a concrete reference point to test against your own rules before a vendor conversation — create a free workspace (`POST /v1/sandbox/workspaces`, no sales call, see the README's ["Try Pink Agentic AI Payments in 2 minutes"](https://github.com/Pink-Agentic-Payments/agentic-payments-readiness#try-pink-agentic-ai-payments-in-2-minutes)), connect it to the agent framework you already use (15 connect guides at [pinkwallet.com/agentic/connect/](https://pinkwallet.com/agentic/connect/)), and read a worked example close to your business at [pinkwallet.com/agentic/industries/](https://pinkwallet.com/agentic/industries/). Because D1.2 and D7.2 are both open (early access, no production pricing), budget time for a sales conversation before any production spend, same as finding 5 above for the sample as a whole.

## Corrections policy

This report and its underlying CSV are published under CC BY 4.0. If you are one of the companies covered, or have found a page we misread, misquoted, or missed, submit a correction with: the check ID, the URL, and the exact text you believe supports a different result. Verified corrections will be applied and logged in the changelog below, with the original entry struck through rather than silently removed.

