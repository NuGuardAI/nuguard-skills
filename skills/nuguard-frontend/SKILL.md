---
name: nuguard-frontend
description: Use when implementing NuGuard React and TypeScript components, hooks, validation, API adapters, permissions, or user-facing error states.
---

# NuGuard frontend

In the NuGuard app, `src/schemas.ts` owns Zod validation, `src/types.ts` owns exported frontend types, `src/adapters/` translates snake case and camel case, `src/services/api.ts` owns authenticated HTTP access, and `src/config.ts` owns service URLs. Verify paths in the target repository before editing.

- Use named functional components, one per file. Components receive data and callbacks; hooks and services own remote operations.
- Validate untrusted data at its boundary with Zod. Keep server authorization authoritative even when the UI hides actions with permission gates.
- Use the existing async and error handling helpers. Show blocking or partial load failures inline near affected content; show mutation failures in a toast; log best-effort failures with the project logger. Do not surface raw exception text or use `console.*` for diagnostics.
- Preserve dark-mode styling and accessible labels, roles, focus states, and keyboard behavior.
- Use `crypto.randomUUID()` for client-generated IDs and `Date.now()` for client timestamps where those conventions apply.

When changing a visible flow, check the API response adapter, validation schema, loading and failure states, and the nearest meaningful component or end-to-end test.
