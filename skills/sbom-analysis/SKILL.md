---
name: sbom-analysis
description: Use to read or explain a NuGuard AI-SBOM JSON file, its components, relationships, dependency inventory, and structural attack surface. Do not infer confirmed exploits from the graph alone.
---

# Interpret a NuGuard AI-SBOM

Use the current package schema (`nuguard/sbom/schemas/aibom.schema.json`) when available. A NuGuard document has `schema_version`, `target`, `nodes`, `edges`, `deps`, and `summary`. Its shape is versioned; do not assume a specific version number or a field's presence in every document.

Nodes use `id`, `name`, `component_type`, `metadata`, and `evidence`. Common types include `AGENT`, `MODEL`, `TOOL`, `DATASTORE`, `GUARDRAIL`, `PROMPT`, `API_ENDPOINT`, and `MCP_SERVER`. Read provider and other open-ended fields from `metadata.extras` when they are not first-class metadata fields. Edges use `source`, `target`, and `relationship_type`; `ACCESSES` edges may include `access_type` (`read`, `write`, `readwrite`). Resolve endpoints by node ID before describing a path.

For an inventory question, group nodes by component type and use edges to show what each agent calls or accesses. For data-access questions, combine `DATASTORE` classification with incoming `ACCESSES` edges and reachable auth or guardrail nodes. Flag `sql_injectable`, `ssrf_possible`, `high_privilege`, `no_auth_required`, untrusted MCP servers, or high `injection_risk_score` only when those values actually appear. A missing edge or field may mean incomplete extraction, not proof that a control is absent.

For a security verdict, run `nuguard analyze --sbom <path>` when requested and available. Keep SBOM observations separate from analysis findings and live test results. Redact prompt excerpts, source snippets, secrets, and personal data before sharing the document or report.
