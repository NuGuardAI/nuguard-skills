---
name: nuguard-api-contracts
description: Use when changing NuGuard service endpoints, request or response models, gateway routes, API clients, integration callbacks, or contract tests.
---

# NuGuard API contracts

Find the owning service, its mounted route, and gateway rewrite before changing a URL. Direct service paths and gateway paths may differ. In the NuGuard app, GitHub AIBOM scans go through `POST /api/assets/scans/github` at the gateway; they are not data-service scans. Compliance endpoints belong to the assessment service.

## Change the whole contract

- Update route validation, request and response models, adapters, frontend types, API client, and affected tests together.
- Prefer additive changes. If a field or enum changes meaning, version or deliberately deprecate it and update every consumer.
- Use verified server-side tenant identity for authorization, even if an older request schema still carries a `tenant_id` for compatibility.
- Validate IDs, bounds, upload content, remote URLs, and webhook signatures as appropriate. Give integration calls bounded timeouts and sanitized failures.
- Keep frontend service URLs in its central configuration and HTTP access in its API service. Do not scatter raw fetches through components.

## Verify

Cover valid and invalid payloads, missing auth, insufficient role, cross-tenant resources, and external dependency failures when affected. Check route behavior both through the service and gateway when the rewrite or prefix changes. Read the repository's current route definitions and schemas before treating a documented example as current.
