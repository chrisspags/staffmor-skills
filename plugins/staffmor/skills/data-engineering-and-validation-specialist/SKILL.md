---
name: data-engineering-and-validation-specialist
description: "Make authorized product data traceable, reconciled and reproducible. Use it to compare a dated scoring result with its exact original player pool and configuration."
---

# Data Engineering and Validation Specialist
Canonical source: staffmor.specialists.data-engineering-validation
Edition: 1.0.1-source-20261008; first-party Staffmor procedure authored by original Mara.
Purpose: Make authorized product data traceable, reconciled and reproducible.

Workspace applicability: named partners, organizations, brand/promo codes and sport priorities in this procedure are examples from supplied work. Apply them only when explicitly supplied and verified in the authenticated current workspace and authorized conversation. Otherwise use the current workspace's actual roles, assets and priorities; do not fetch another workspace or infer account, channel or tool authority.

Inputs: the authorized dataset/export and schema, observation grain, sport/site/slate and time-zone boundary, source version, original run/build IDs, units and primary keys. Ask for the missing exact artifact instead of finding private caches or guessing joins. Keep reported counts separate from acquired rows.

Method:
1. Pin original inputs with SHA256, byte count, capture time and source route. Describe each stage: ingest, normalization, eligible pool, scoring/grading, portfolio selection and published output. Preserve source rows as immutable evidence.
2. Define the grain before joining: player/slate, lineup/run, contest/entry or transaction. Test uniqueness, nulls, types, currency/units, date boundaries and one-to-many joins. Retain rejected/quarantined records with explicit reasons; never silently deduplicate conflicting rows.
3. Prioritize result and grading correctness before field or ownership modeling. Reconcile counts and value totals at every boundary. An input pool is not a delivered book. A proxy sample is not faithful replay of an absent full original pool/configuration.
4. Specify idempotent keys and revisions for updates and reruns. Reject mismatched versions, overlapping input epochs or missing provenance. Keep UTC and supplied local times together.
5. Build a small isolated query or transformation against permitted inputs. Independently recompute important totals and inspect a bounded sample from every rejection category. Label synthetic rows. A test pass does not establish customer data coverage.
6. For database changes pair the existing DBA procedure: verify actual engine/version, consistent supported backup and demonstrated restore before an authorized migration. EXPLAIN ANALYZE can execute the statement; do not use it on a mutating statement as a read-only diagnostic.

Deliverable: a source-to-output lineage table, checked schemas/keys, reconciliation totals and exceptions, exact reproducible transformation, affected validation evidence and the smallest unresolved original-data request. Show requested, acquired, transformed and served states separately. State precisely what could not be replayed.

Tools: only already-permitted exports, source/file readers, supported engine tooling and isolated scripts. No private database/session access, paid data subscription, dependency download, live migration or new credentials follows from this guide. Stop on access denial, schema ambiguity or disagreement; retain known originals and report the specific missing route or artifact.

Primary references inspected2026-10-08 (verify current material requirements at execution):
- https://www.postgresql.org/docs/current/sql-explain.html
- https://www.sqlite.org/backup.html

Scope: this is expertise guidance, not a tool, native session, running model or authority grant. Use only the authenticated current workspace and permitted original conversation. Keep source/candidate, reviewed distribution, installed availability and actual native consumption separate. Original source/history and held records remain intact.
