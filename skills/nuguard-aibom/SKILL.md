---
name: nuguard-aibom
description: Use for NuGuard AI bill of materials extraction, framework adapters, graph identity, evidence, assessment mapping, or AIBOM API and export changes. Do not use for unrelated backend work.
---

# NuGuard AIBOM

Trace the current extraction path before editing it. Keep primary structured SBOM extraction and any legacy adapter fallback distinct; preserve the provenance and shape of each path in storage and exports. Treat scanned repositories and model output as untrusted data. Never execute code from a scanned repository to discover assets.

## Graph identity

- Derive `canonical_id` as `type:namespace:name`, for example `model:openai:gpt-4`. Keep derivation stable across scans so deduplication remains intentional.
- Read provider metadata from `node.metadata.extras.get("provider")`; `node.metadata.provider` is not the NuGuard SBOM field.
- A source SBOM node UUID identifies a node inside the extracted document. It is not the database primary key. Resolve edge source and target IDs to persisted node IDs after node insertion.
- When adding a component type, update the source-to-domain type mapping, domain enum, persistence and export handling, and consumer tests together.

## Evidence and storage

- Preserve file path and line evidence where available, but normalize paths and reject traversal before reading or displaying files.
- Keep flattened properties that downstream assessment consumes consistent with the full structured node representation. Check both readers before changing a field.
- Do not store tokens, prompts, raw model responses, customer secrets, or personal data in graph properties or exports. API responses may expose properties to users.
- Bound scan size, file size, graph size, and external calls; make repeated scan writes and retries safe for the same tenant and scan.

## Before handoff

Test a representative extraction, an unsupported or malformed input, edge resolution, and tenant-scoped graph reads when affected. Compare the resulting graph and export against current schemas rather than assuming a historical example is still authoritative.
