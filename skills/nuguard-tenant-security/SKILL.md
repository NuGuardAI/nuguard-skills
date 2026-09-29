---
name: nuguard-tenant-security
description: Use when implementing or reviewing NuGuard tenant-scoped reads, writes, jobs, integrations, authentication, authorization, or sensitive scan data.
---

# NuGuard tenant security

Derive tenant context from verified authentication or a trusted server-side job identity. A request body, query parameter, URL, or client-selected tenant ID never establishes the authorization boundary. When tenant context is uncertain, fail closed.

## Check each boundary

1. Authenticate every non-public endpoint. Authorize mutations and sensitive reads for role and resource ownership on the server.
2. Constrain every tenant-scoped read, update, delete, aggregate, cache key, and background job to the verified tenant. Check related resources belong to that tenant before linking or exporting them.
3. Validate IDs, pagination, URLs, uploads, webhook payloads, and integration settings at entry. Canonicalize paths and reject traversal, private-network targets, and unexpected URL schemes when fetching external resources.
4. Use ORM queries or bound SQL parameters. Apply tenant-aware constraints and indexes to the actual access pattern. RLS can add defense in depth but does not replace application authorization.
5. Keep secrets and sensitive artifacts out of source, logs, traces, exception text, and client responses. Use approved secret storage and structured, redacted diagnostics.
6. Give external calls explicit timeouts. Retry only safe transient failures with bounds; make callbacks and durable jobs idempotent where delivery can repeat.

## Verification

Exercise authorized access, cross-tenant denial, insufficient-role denial, malformed input, and dependency failure at the closest meaningful level. Review error text and logs for sensitive values. Do not disable auth, RBAC, audit, validation, rate limits, or other controls to make a test pass.
