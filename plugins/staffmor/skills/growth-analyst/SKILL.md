---
name: growth-analyst
description: "Reconcile acquisition, revenue and retention before recommending growth work. Use it to compare signup and paid cohorts using supplied revenue and partner-promo exports."
---

# Growth Analyst
Canonical source: staffmor.specialists.growth-analyst
Edition: 1.0.1-source-20261008; first-party Staffmor procedure authored by original Mara.
Purpose: Reconcile acquisition, revenue and retention before recommending growth work.

Workspace applicability: named partners, organizations, brand/promo codes and sport priorities in this procedure are examples from supplied work. Apply them only when explicitly supplied and verified in the authenticated current workspace and authorized conversation. Otherwise use the current workspace's actual roles, assets and priorities; do not fetch another workspace or infer account, channel or tool authority.

Inputs: permitted current-workspace aggregate exports, event and transaction definitions, period/time zone, currencies, source systems, original identifiers, refund/chargeback status and existing attribution rules. Reported Stripe promo partners SPLASHPLAY/SPLASH are hypotheses until their exact authorized records are acquired; names do not grant Stripe access.

Method:
1. Establish the grain and reconcile source totals before segmenting. Separate user, signup, subscription, invoice, payment and balance transaction. Repeated webhooks are intake events, not new paid customers.
2. Define gross charged, refunded, processor fees, net cash and earned revenue separately. Maintain currency and settlement/available dates. Never sum different currencies or treat unsettled balance as available payout.
3. Build cohorts by agreed signup/paid-start date. Count activated first successful task, paid conversion and retained customers within explicit windows. Right-censored recent cohorts remain incomplete; churn does not mean the same thing as scheduled cancellation.
4. Preserve attribution touchpoints, chosen model and unknown/unattributed traffic. A promo code can identify an association, not causal incrementality. Compare results under defensible attribution choices and holdout evidence when available; do not overwrite canonical transaction records.
5. Normalize for exposure and eligibility. A heavily shown role/card can have more selections without higher underlying demand. Plan separate selection, first successful task, paid conversion and retention measures, but do not implement new tracking or collect personal/sensitive context under this guide.
6. Rank bottlenecks by verified scale, value and uncertainty. Check per-period totals against accounting/Riley and distinguish actual findings from data-quality repair. Prepare an isolated calculation, reconciliation exceptions and an experiment hypothesis.

Deliverable: a concise metric dictionary, dated source lineage, checked cohort/funnel table with denominators, money reconciliation and uncertainty, plus one bounded next investigation. No invented usage/popularity, acquisition cost or partner revenue.

Tools: supported permitted source readers and supplied exports/spreadsheets. Verify actual access and data completeness. No account linking, Stripe grants, promo creation, payout, subscription/spend or analytics installation. If denied, retain the exact denied route and useful analysis possible with existing data; request the rightful original reader through the established task route.

Primary references inspected2026-10-08 (verify current material requirements at execution):
- https://docs.stripe.com/api/balance_transactions/object
- https://support.google.com/analytics/answer/10596866?hl=en

Scope: this is expertise guidance, not a tool, native session, running model or authority grant. Use only the authenticated current workspace and permitted original conversation. Keep source/candidate, reviewed distribution, installed availability and actual native consumption separate. Original source/history and held records remain intact.
