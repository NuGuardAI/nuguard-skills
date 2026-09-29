---
name: nuguard-code-review
description: Review NuGuard code or a pull request for tenant isolation, authorization, AIBOM correctness, API contract drift, data exposure, and relevant regressions. Use for review requests, not routine implementation.
---

# NuGuard code review

Read the actual diff and surrounding code before reporting a finding. Trace the request or job identity through service and persistence boundaries. Use `nuguard-tenant-security`, `nuguard-aibom`, or `nuguard-api-contracts` for deeper context only when that area changed.

Prioritize issues that can expose another tenant's data, bypass authorization, execute hostile scan input, leak secrets or raw artifacts, corrupt graph identity, or break a public contract. For migrations, inspect tenant safety, constraints, indexes, rollout, and rollback. For frontend changes, inspect validation, error handling, and whether permission gates are backed by server checks.

Report actionable findings first. Give each finding a file and line, the failing condition, its impact, and a concrete fix. Distinguish a proven defect from a question or unverified risk. If no findings are supported, say what you inspected and what remains unverified. Do not invent findings from a checklist or claim that a test ran when it did not.
