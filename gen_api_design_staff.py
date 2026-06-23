import json

OUT = "content/sysdesign/api-design-staff.json"


def bd(label, color="#E95420"):
    bg = f"rgba({','.join(str(int(color[i:i+2],16)) for i in (1,3,5))},0.08)"
    return f'<div style="margin-bottom:16px"><span style="display:inline-block;background:{bg};border:1px solid {color};color:{color};font:700 10px system-ui;padding:3px 10px;border-radius:99px;letter-spacing:.05em">{label}</span></div>'


def mg(items):
    r = "".join(f'<div style="background:#f8fafc;border:1.5px solid #e2e8f0;border-radius:8px;padding:14px">{item}</div>' for item in items)
    return f'<div style="margin:16px 0;display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px">{r}</div>'


def tb(hd, rows):
    th = "".join(f'<th style="padding:10px 12px;border-bottom:2px solid #e2e8f0;color:#475569;font-weight:700;text-align:left;font-size:11px">{h}</th>' for h in hd)
    tr = ""
    for i, r in enumerate(rows):
        bg = 'background:#fafafa' if i % 2 else ''
        tr += f'<tr style="border-bottom:1px solid #f1f5f9;{bg}>' + "".join(f'<td style="padding:9px 12px;font-size:12px{f";font-weight:600" if j==0 else ""}">{c}</td>' for j, c in enumerate(r)) + '</tr>'
    return f'<div style="margin:16px 0;overflow-x:auto"><table style="width:100%;border-collapse:collapse;font:12px system-ui,sans-serif"><thead><tr style="background:#f1f5f9;text-align:left">{th}</tr></thead><tbody>{tr}</tbody></table></div>'


S = []

# ---------------------------------------------------------------------------
# 1 – API Design Foundations: REST, GraphQL, gRPC & When to Use Each
# ---------------------------------------------------------------------------
S.append({
    "id": "api-design-staff-1",
    "title": "API Design Foundations: REST, GraphQL, gRPC & When to Use Each",
    "category": "api-design",
    "subcategory": "Staff+ Interviewing",
    "description": bd("FOUNDATIONS", "#E95420") + tb(
        ["Paradigm", "Strengths", "Weaknesses", "Best For"],
        [
            ["REST", "Cacheable, stateless, uniform interface", "Over-fetching, chatty, no strong typing", "CRUD-heavy, web-facing APIs"],
            ["GraphQL", "Declarative fetching, single endpoint, strong typing", "Complex caching, N+1 risk, query cost", "Dynamic UIs, aggregating sources"],
            ["gRPC", "Binary perf, streaming, strong contracts", "Browser unfriendly, tooling maturity", "Microservice <-> microservice"],
        ],
    ) + mg([
        "<strong>Staff+ Interview Tip:</strong> Never present one protocol as universally superior. Frame your answer around <em>trade-offs</em>: team expertise, ecosystem constraints, traffic patterns, and operational maturity.",
        "<strong>Hybrid Patterns:</strong> Many orgs expose REST externally and gRPC internally. GraphQL can sit as a gateway layer over both. Discuss <em>strangler fig</em> migrations when shifting between protocols.",
        "<strong>Idempotency & Safety:</strong> REST GET/HEAD/OPTIONS are safe; PUT/DELETE are idempotent; POST is not. gRPC classifies rpc types (unary, server-streaming, client-streaming, bidi). GraphQL queries are safe, mutations are not idempotent by default.",
    ]),
    "tags": ["api", "design", "staff-plus", "interview-prep"],
    "language": "text",
    "sections": [],
})

# ---------------------------------------------------------------------------
# 2 – API-First Design: Contracts, Specs & Code Generation
# ---------------------------------------------------------------------------
S.append({
    "id": "api-design-staff-2",
    "title": "API-First Design: Contracts, Specs & Code Generation",
    "category": "api-design",
    "subcategory": "Staff+ Interviewing",
    "description": bd("API-FIRST", "#2B5797") + """\
<p>API-first design means the contract is the source of truth — code is generated <em>from</em> the spec, not the other way around. This approach enables parallel development, automated testing, and self-documenting APIs that stay in sync.</p>""" + tb(
        ["Layer", "Tooling", "Purpose"],
        [
            ["Spec Authoring", "OpenAPI 3.1, AsyncAPI, GraphQL SDL, Protobuf", "Define endpoints, schemas, errors, auth flows before implementation"],
            ["Code Generation", "OpenAPI Generator, protoc, graphql-codegen", "Generate server stubs, client SDKs, typed resolvers, mocks"],
            ["Contract Testing", "Pact, Dredd, Optic, Spectral", "Enforce spec compliance, detect breaking changes in CI"],
            ["Mock Servers", "Prism, Mockoon, WireMock", "Unblock frontend & integration teams before backend is ready"],
        ],
    ) + mg([
        "<strong>Staff+ Interview Tip:</strong> Emphasize that contracts are a <em>governance boundary</em>. A spec review board (with breaking-change checklists) is a common pattern at large orgs. Discuss how you'd enforce contracts across dozens of teams.",
        "<strong>Schema Evolution:</strong> Protobuf uses field numbers (never reuse/rename). OpenAPI 3.1 uses JSON Schema 2020-12 for composable schemas. GraphQL uses deprecation directives and schema registry for gradual migration.",
        "<strong>Generation Pipelines:</strong> At Staff+ level, design a CI pipeline that: lint → breaking-change detection → mock generation → contract tests → publish to registry. This is the intersection of API design and platform engineering.",
    ]),
    "tags": ["api", "design", "staff-plus", "interview-prep"],
    "language": "text",
    "sections": [],
})

# ---------------------------------------------------------------------------
# 3 – Versioning Strategies: Breaking vs Non-Breaking Changes
# ---------------------------------------------------------------------------
S.append({
    "id": "api-design-staff-3",
    "title": "Versioning Strategies: Breaking vs Non-Breaking Changes",
    "category": "api-design",
    "subcategory": "Staff+ Interviewing",
    "description": bd("VERSIONING", "#7B2D8E") + tb(
        ["Strategy", "Mechanism", "Pros", "Cons"],
        [
            ["URI Path", "/v1/customers", "Explicit, cache-friendly", "Code duplication, slower evolution"],
            ["Header", "Accept: application/vnd.api+json;version=2", "Clean URLs, no duplication", "Hidden from casual inspection"],
            ["Query Param", "?version=2", "Easy to test", "Pollutes URLs, caching issues"],
            ["Content Negotiation", "Accept header with media type", "RESTful, leverages HTTP", "Complex client logic"],
        ],
    ) + mg([
        "<strong>Non-Breaking Changes:</strong> Adding optional fields, adding enum values (if clients ignore unknowns), expanding response payloads, relaxing constraints (e.g., making a required field optional). Always use <em>tolerant reader</em> / Postel's Law on the server side.",
        "<strong>Breaking Changes:</strong> Removing/renaming fields, changing field types, making optional → required, changing enum values, removing endpoints, changing auth requirements. Detect these with <em>Optic</em> or <em>Spectral</em> in CI.",
        "<strong>Staff+ Decision:</strong> Prefer <em>compatibility-first</em> versioning over aggressive version bumps. Each version is a tax — you must maintain, test, document, and support it. At big orgs, version lifetimes are measured in years. Design a deprecation policy (e.g., N-2 support, sunset headers, migration guides).",
    ]),
    "tags": ["api", "design", "staff-plus", "interview-prep"],
    "language": "text",
    "sections": [],
})

# ---------------------------------------------------------------------------
# 4 – Pagination, Filtering & Sorting at Scale
# ---------------------------------------------------------------------------
S.append({
    "id": "api-design-staff-4",
    "title": "Pagination, Filtering & Sorting at Scale",
    "category": "api-design",
    "subcategory": "Staff+ Interviewing",
    "description": bd("PAGINATION", "#C7254E") + tb(
        ["Pattern", "How It Works", "When to Use"],
        [
            ["Cursor-based", "opaque cursor + limit (cursor=abc123)", "Real-time data, infinite scroll, high consistency"],
            ["Offset-based", "offset + limit (?offset=20&limit=10)", "Simple, stable datasets, random access"],
            ["Keyset / Seek", "WHERE id > ? ORDER BY id LIMIT ?", "High throughput, no offset overhead"],
            ["Page tokens", "Encoded cursor in opaque token", "Distributed backends, hides implementation"],
        ],
    ) + """\
<p>At Staff+ level, discuss how pagination interacts with consistency. Cursor-based pagination avoids offset drift (items inserted/deleted between pages), but requires a stable sort order. Keyset pagination is the most performant for large datasets but breaks with non-unique sort columns.</p>""" + mg([
        "<strong>Filtering:</strong> Expose filters as query parameters with a consistent syntax: <code>?status=active&created_at.gt=2024-01-01</code>. For complex filtering, consider a <code>$filter</code> DSL (OData, Searchkit) but beware of SQL injection at the API layer.",
        "<strong>Sorting:</strong> Multi-field sort: <code>?sort=-created_at,name</code> (minus for descending). Limit sort fields to indexed columns to prevent full table scans. GraphQL provides <code>orderBy</code> arguments; gRPC uses a sort field enum in the request message.",
        "<strong>Edge Cases:</strong> Paginating across <em>sharded databases</em> requires scatter-gather or global index. Real-time feeds (activity logs, notifications) demand cursor-based. <strong>Ask your interviewer:</strong> \"What are the consistency requirements for this list?\" before proposing a strategy.",
    ]),
    "tags": ["api", "design", "staff-plus", "interview-prep"],
    "language": "text",
    "sections": [],
})

# ---------------------------------------------------------------------------
# 5 – Rate Limiting, Throttling & Quota Management
# ---------------------------------------------------------------------------
S.append({
    "id": "api-design-staff-5",
    "title": "Rate Limiting, Throttling & Quota Management",
    "category": "api-design",
    "subcategory": "Staff+ Interviewing",
    "description": bd("RATE LIMITING", "#D32F2F") + tb(
        ["Algorithm", "Behavior", "Use Case"],
        [
            ["Token Bucket", "Tokens refill at fixed rate, burst capacity", "General purpose, bursty traffic"],
            ["Leaky Bucket", "Requests processed at fixed rate, queue overflow", "Smoothing traffic spikes"],
            ["Sliding Window", "Count requests in rolling time window", "Precise, distributed-friendly"],
            ["Fixed Window", "Reset counter at interval boundaries", "Simple but thundering herd at reset"],
            ["Concurrency", "Max in-flight requests at once", "Protecting backend resources"],
        ],
    ) + mg([
        "<strong>Headers:</strong> Return <code>X-RateLimit-Limit</code>, <code>X-RateLimit-Remaining</code>, <code>X-RateLimit-Reset</code>. Use <code>Retry-After</code> on 429 responses. Consistency in rate-limit headers is a hallmark of production-grade APIs.",
        "<strong>Quota Management:</strong> Distinguish between <em>rate limits</em> (requests/second) and <em>quotas</em> (requests/day/month). Quotas are enforced asynchronously — track usage in a counter DB (Redis, Cassandra) and alert before hard cutoff.",
        "<strong>Distributed Rate Limiting:</strong> Use Redis Cluster + Lua scripting for atomic sliding windows. For global limits, a consensus-based approach (CRDT counters) avoids a single point of failure. Discuss <em>eventual consistency</em> trade-offs for quota enforcement.",
    ]),
    "tags": ["api", "design", "staff-plus", "interview-prep"],
    "language": "text",
    "sections": [],
})

# ---------------------------------------------------------------------------
# 6 – Authentication & Authorization Patterns (OAuth2, JWT, API Keys)
# ---------------------------------------------------------------------------
S.append({
    "id": "api-design-staff-6",
    "title": "Authentication & Authorization Patterns (OAuth2, JWT, API Keys)",
    "category": "api-design",
    "subcategory": "Staff+ Interviewing",
    "description": bd("AUTH", "#1565C0") + tb(
        ["Mechanism", "Stateless?", "Best For"],
        [
            ["API Keys (Bearer token)", "Yes (with validation)", "Server-to-server, internal tools"],
            ["JWT (self-contained)", "Yes", "Distributed systems, no session store"],
            ["OAuth2 + opaque tokens", "No (token introspection)", "Third-party delegation, user context"],
            ["Session cookie", "No", "Browser-based apps, legacy systems"],
            ["mTLS", "N/A", "Zero-trust, service mesh"],
        ],
    ) + """\
<p>At Staff+ level, design for the <em>token lifecycle</em>: issuance, refresh, revocation, and rotation. JWT has convenience but introduces key rotation, clock skew, and payload size concerns. OAuth2 with opaque tokens shifts introspection cost to the auth server but enables instant revocation.</p>""" + mg([
        "<strong>OAuth2 Flows:</strong> Authorization Code + PKCE for SPAs, Client Credentials for machine-to-machine, Device Authorization for CLI/headless. Discuss <em>token exchange</em> patterns (RFC 8693) for multi-service delegation.",
        "<strong>Authorization:</strong> RBAC (role-based) is coarse; ABAC (attribute-based) via <em>OPA/rego</em> or <em>Casbin</em> supports fine-grained policies. At scale, use a <em>PDP</em> (Policy Decision Point) separated from the <em>PEP</em> (Policy Enforcement Point) in the API gateway.",
        "<strong>Staff+ Interview Tip:</strong> Draw a sequence diagram showing: client → gateway (token validation) → PDP (policy check) → upstream service (scoped context). Discuss how you'd handle token revocation with a distributed bloom filter or a bounded revocation list.",
    ]),
    "tags": ["api", "design", "staff-plus", "interview-prep"],
    "language": "text",
    "sections": [],
})

# ---------------------------------------------------------------------------
# 7 – Error Handling & Idempotency
# ---------------------------------------------------------------------------
S.append({
    "id": "api-design-staff-7",
    "title": "Error Handling & Idempotency",
    "category": "api-design",
    "subcategory": "Staff+ Interviewing",
    "description": bd("ERRORS", "#C62828") + tb(
        ["Status Code", "Semantics", "Retryable?"],
        [
            ["400 Bad Request", "Client error (validation, bad body)", "No — fix request first"],
            ["401 / 403", "Unauthenticated / Unauthorized", "No (refresh token if 401)"],
            ["404 Not Found", "Resource doesn't exist", "No"],
            ["409 Conflict", "Version mismatch, duplicate", "Maybe — depends on cause"],
            ["429 Too Many Requests", "Rate limit exceeded", "Yes — with Retry-After"],
            ["500 Internal Server Error", "Server-side fault", "Yes — with exponential backoff"],
            ["502 / 503 / 504", "Gateway / unavailable / timeout", "Yes — with backoff & jitter"],
        ],
    ) + mg([
        "<strong>Standard Error Body:</strong> <code>{&quot;error&quot;: {&quot;code&quot;: &quot;VALIDATION_ERROR&quot;, &quot;message&quot;: &quot;...&quot;, &quot;details&quot;: [...], &quot;trace_id&quot;: &quot;...&quot;}}</code>. Include a machine-readable <code>code</code>, human-readable <code>message</code>, and a <code>trace_id</code> for debugging.",
        "<strong>Idempotency Key:</strong> Use <code>Idempotency-Key</code> header for POST/PATCH. The server deduplicates within a TTL window (e.g., 24h). Store the key → response mapping in a durable DB. Return the original response on replay — critical for payment APIs.",
        "<strong>Staff+ Design:</strong> Error codes should be <em>hierarchical</em>: <code>PAYMENT.DECLINED.INSUFFICIENT_FUNDS</code>. Publish a machine-readable error catalog. For idempotency, consider <em>optimistic concurrency</em> via <code>If-Match</code> / <code>ETag</code> alongside idempotency keys.",
    ]),
    "tags": ["api", "design", "staff-plus", "interview-prep"],
    "language": "text",
    "sections": [],
})

# ---------------------------------------------------------------------------
# 8 – API Security: Input Validation, Rate Limits, CORS & Beyond
# ---------------------------------------------------------------------------
S.append({
    "id": "api-design-staff-8",
    "title": "API Security: Input Validation, Rate Limits, CORS & Beyond",
    "category": "api-design",
    "subcategory": "Staff+ Interviewing",
    "description": bd("SECURITY", "#B71C1C") + tb(
        ["Layer", "Control", "Implementation"],
        [
            ["Transport", "TLS 1.3, HSTS, Certificate pinning", "Enforce at load balancer / gateway"],
            ["Input", "Schema validation, allow-listing, length limits", "Validate JSON against OpenAPI spec (e.g., express-validator, jsonschema)"],
            ["Auth", "Rate-limit login endpoints, account lockout", "Per-IP + per-account rate limiting"],
            ["Output", "Response filtering, no stack traces", "Strip internal fields, normalize error payloads"],
            ["CORS", "Allow-list origins, not wildcard", "Validate Origin header, preflight caching"],
        ],
    ) + mg([
        "<strong>Input Validation Depth:</strong> Validate at the API gateway (syntactic) AND the service (semantic). Guard against <em>mass assignment</em> (use DTOs, never bind directly to entities). Limit request body size (e.g., 10 MB) and field depth (e.g., max 6 levels of nesting).",
        "<strong>OWASP Top 10 for APIs:</strong> Broken object-level authorization (BOLA/IDOR), excessive data exposure, mass assignment, injection, security misconfiguration. API-specific tooling: <em>42Crunch</em>, <em>Salt Security</em>, <em>APISec</em>.",
        "<strong>Staff+ Strategy:</strong> Design a <em>defense-in-depth</em> posture: WAF → gateway auth → rate limiting → schema validation → service authorization → output sanitization. Every layer fails closed. Implement a security <em>chaos engineering</em> practice (fuzz endpoints, inject faults).",
    ]),
    "tags": ["api", "design", "staff-plus", "interview-prep"],
    "language": "text",
    "sections": [],
})

# ---------------------------------------------------------------------------
# 9 – Performance: Caching, Compression, Connection Pooling
# ---------------------------------------------------------------------------
S.append({
    "id": "api-design-staff-9",
    "title": "Performance: Caching, Compression, Connection Pooling",
    "category": "api-design",
    "subcategory": "Staff+ Interviewing",
    "description": bd("PERFORMANCE", "#00838F") + tb(
        ["Technique", "Mechanism", "Impact"],
        [
            ["HTTP Caching", "Cache-Control, ETag, If-None-Match", "Reduces origin load, improves latency"],
            ["CDN Caching", "Edge caching for GET responses", "Global latency reduction, shield origin"],
            ["Application Cache", "Redis / Memcached for computed data", "Sub-millisecond reads for hot data"],
            ["Compression", "gzip / brotli (accept-encoding)", "60-80% bandwidth reduction"],
            ["Connection Pooling", "HTTP keep-alive, DB connection pool", "Reduces handshake overhead, TCP port reuse"],
            ["Batching", "GraphQL batching, gRPC streaming", "Fewer round-trips, amortizes overhead"],
        ],
    ) + mg([
        "<strong>Cache Invalidation:</strong> The hardest problem in computer science. Use <em>TTL-based</em> (time-based) + <em>event-driven</em> (cache-aside with write-through). For distributed caches, consider <em>write-behind</em> with a queue for high throughput.",
        "<strong>GraphQL Caching:</strong> POST requests are not cacheable by default. Use <em>Automatic Persisted Queries</em> (APQ) to turn queries into GET requests. Consider a CDN cache for persisted query IDs. Use a <em>DataLoader</em> to batch and cache at the resolver level.",
        "<strong>Staff+ Design:</strong> Measure first — profile P50/P95/P99 latencies. Use <em>latency budgets</em> per API call. At scale, implement <em>hedged requests</em> (race two backends) or <em>request coalescing</em> (deduplicate concurrent identical requests at the proxy layer).",
    ]),
    "tags": ["api", "design", "staff-plus", "interview-prep"],
    "language": "text",
    "sections": [],
})

# ---------------------------------------------------------------------------
# 10 – API Observability: Metrics, Tracing, Logging
# ---------------------------------------------------------------------------
S.append({
    "id": "api-design-staff-10",
    "title": "API Observability: Metrics, Tracing, Logging",
    "category": "api-design",
    "subcategory": "Staff+ Interviewing",
    "description": bd("OBSERVABILITY", "#00695C") + tb(
        ["Pillar", "What It Tells You", "Tooling"],
        [
            ["Metrics (RED)", "Rate, Errors, Duration", "Prometheus + Grafana dashboards"],
            ["Distributed Tracing", "Request flow across services, bottlenecks", "OpenTelemetry + Jaeger / Tempo"],
            ["Structured Logging", "Debugging, audit trail, pattern analysis", "JSON logs, ELK / Loki + Grafana"],
            ["Profiling", "CPU, memory, I/O hot spots", "py-spy, pprof, async-profiler"],
            ["Alerting", "Anomaly detection, SLO burn rate", "Alertmanager, PagerDuty, OpsGenie"],
        ],
    ) + mg([
        "<strong>Correlation IDs:</strong> Every request gets a <code>X-Request-ID</code> (client-generated) or <code>X-Trace-ID</code> (gateway-generated). Propagate via headers (W3C Trace-Context format). This connects logs, traces, and metrics for a single request lifecycle.",
        "<strong>SLO / SLI / SLA:</strong> Define <em>Service Level Indicators</em> (e.g., latency P99 < 500ms), <em>Objectives</em> (99.9% of requests), and <em>Agreements</em> (contractual). Use <em>burn-rate alerting</em> to detect SLO violations early.",
        "<strong>Staff+ Interview Tip:</strong> Draw the three pillars and show how they connect: a Prometheus metric alert → links to a Grafana dashboard → drill into a trace in Jaeger → view structured logs for that trace_id. This closed-loop observability is expected at Staff+ level.",
    ]),
    "tags": ["api", "design", "staff-plus", "interview-prep"],
    "language": "text",
    "sections": [],
})

# ---------------------------------------------------------------------------
# 11 – GraphQL Deep Dive: Schema Design, N+1, DataLoader Patterns
# ---------------------------------------------------------------------------
S.append({
    "id": "api-design-staff-11",
    "title": "GraphQL Deep Dive: Schema Design, N+1, DataLoader Patterns",
    "category": "api-design",
    "subcategory": "Staff+ Interviewing",
    "description": bd("GRAPHQL", "#E535AB") + tb(
        ["Concept", "Pattern", "Why It Matters"],
        [
            ["Schema-first", "SDL defines types, queries, mutations first", "Contract-driven, self-documenting, tooling (GraphiQL, introspection)"],
            ["DataLoader", "Batch + cache function per entity type", "Eliminates N+1 — coalesces DB/DATA requests per tick"],
            ["Cursor Connections", "Relay spec: edges, node, pageInfo", "Standardized pagination, stable cursors, totalCount?"],
            ["Dataloader per-request", "New DataLoader per HTTP request", "Isolates cache to request lifecycle, prevents stale data"],
            ["Query Cost Analysis", "Complexity limit, depth limit, rate limiting", "Prevents abusive queries that overload the backend"],
        ],
    ) + mg([
        "<strong>N+1 Problem:</strong> Resolver fetches a list, then each item triggers a separate fetch. DataLoader coalesces these into a single batch. At Staff+ level, discuss <em>lookahead</em> patterns — use <code>info</code> to precompute join paths and avoid lazy loading entirely.",
        "<strong>Schema Design Heuristics:</strong> Prefer <em>connections</em> for lists (Relay spec), <em>unions</em> for polymorphic results, <em>interfaces</em> for shared fields. Mutations return a <code>MutationResponse</code> union with <code>success</code> and <code>errors</code> for client-side handling.",
        "<strong>Federation:</strong> Apollo Federation v2 / GraphQL Mesh for composing schemas across services. Discuss entity resolution (<code>@key</code>), computed fields (<code>@requires</code>), and cross-service auth context propagation. This is a GraphQL microservice architecture.",
    ]),
    "tags": ["api", "design", "staff-plus", "interview-prep"],
    "language": "text",
    "sections": [],
})

# ---------------------------------------------------------------------------
# 12 – gRPC & Protobuf: Streaming, Bidirectional, Interceptors
# ---------------------------------------------------------------------------
S.append({
    "id": "api-design-staff-12",
    "title": "gRPC & Protobuf: Streaming, Bidirectional, Interceptors",
    "category": "api-design",
    "subcategory": "Staff+ Interviewing",
    "description": bd("gRPC", "#00B96B") + tb(
        ["RPC Type", "Direction", "Use Case"],
        [
            ["Unary", "Client → Server → Client", "Standard request-response"],
            ["Server Streaming", "Client sends one, server streams back", "Event feeds, log tailing, progress updates"],
            ["Client Streaming", "Client streams, server responds once", "File upload, telemetry batches"],
            ["Bidirectional", "Both sides stream independently", "Real-time chat, collaborative editing, live dashboards"],
        ],
    ) + mg([
        "<strong>Protobuf Best Practices:</strong> Never reuse field numbers. Reserve deleted fields with <code>reserved</code>. Use <code>google.protobuf.Timestamp</code> (not string). Enums should have a <code>UNSPECIFIED = 0</code> sentinel. Use <code>wrappers.proto</code> for nullable primitives (though optional is now proto3 native).",
        "<strong>Interceptors:</strong> gRPC middleware — auth (JWT extraction), logging (request/response payloads), rate limiting, circuit breaking, tracing. Implement as <em>unary interceptors</em> (simple) and <em>stream interceptors</em> (stream wrapping). At scale, interceptors replace API gateway functions for service-to-service calls.",
        "<strong>gRPC Gateway:</strong> Expose gRPC services as REST/JSON via <code>grpc-gateway</code> or <code>envoy</code>. Annotations in protos generate REST endpoints. This is the <em>single source of truth</em> approach — write once (proto) and publish multiple protocol faces.",
    ]),
    "tags": ["api", "design", "staff-plus", "interview-prep"],
    "language": "text",
    "sections": [],
})

# ---------------------------------------------------------------------------
# 13 – Event-Driven APIs: Webhooks, SSE, Event Sourcing
# ---------------------------------------------------------------------------
S.append({
    "id": "api-design-staff-13",
    "title": "Event-Driven APIs: Webhooks, SSE, Event Sourcing",
    "category": "api-design",
    "subcategory": "Staff+ Interviewing",
    "description": bd("EVENT-DRIVEN", "#E65100") + tb(
        ["Pattern", "Direction", "Delivery", "Use Case"],
        [
            ["Webhooks", "Server → Client (push)", "HTTP POST to registered URL, retry with backoff", "Async notifications: payment success, CI complete, deploy status"],
            ["Server-Sent Events (SSE)", "Server → Client (stream)", "Single long-lived HTTP connection, auto-reconnect", "Live feeds: notifications, stock ticker, log tailing"],
            ["Event Sourcing", "Append-only event log", "Events are the source of truth; current state is derived", "Audit trails, temporal queries, undo/replay"],
            ["WebSocket", "Bidirectional full-duplex", "Persistent TCP connection after HTTP upgrade", "Real-time collaboration, gaming, live dashboards"],
        ],
    ) + mg([
        "<strong>Webhook Reliability:</strong> Implement at-least-once delivery with idempotency keys (<code>X-Idempotency-Key</code>). Exponential backoff (1s, 2s, 4s... max 1h). Dead-letter queue after N retries. Webhook signatures (HMAC-SHA256) for authenticity.",
        "<strong>Event Sourcing + CQRS:</strong> Commands → Event Store (append-only, e.g., EventStoreDB, Kafka) → Projections (materialized views). APIs read from projections. At Staff+ level, discuss <em>event versioning</em> (schema registry for events), <em>tolerance for replay</em>, and <em>eventual consistency</em> semantics.",
        "<strong>Staff+ Trade-off Discussion:</strong> Webhooks vs polling — webhooks push (real-time, less load) but add delivery complexity; polling pull (simpler server, client-driven). SSE is simpler than WebSockets for one-way server-to-client. Choose based on client complexity tolerance and volume.",
    ]),
    "tags": ["api", "design", "staff-plus", "interview-prep"],
    "language": "text",
    "sections": [],
})

# ---------------------------------------------------------------------------
# 14 – Internal vs External APIs: Design for Different Consumers
# ---------------------------------------------------------------------------
S.append({
    "id": "api-design-staff-14",
    "title": "Internal vs External APIs: Design for Different Consumers",
    "category": "api-design",
    "subcategory": "Staff+ Interviewing",
    "description": bd("INTERNAL v EXTERNAL", "#37474F") + tb(
        ["Concern", "Internal API", "External (Public) API"],
        [
            ["Versioning", "Semver with rapid iteration", "Calendar versioning, extended support windows"],
            ["Auth", "mTLS, service tokens, VPC", "OAuth2, API keys, rate-limited per customer"],
            ["Contract", "Protobuf, Thrift, internal OpenAPI", "Stable OpenAPI, SDK generation, changelogs"],
            ["SLA", "Best-effort or internal SLOs", "Contractual SLAs with penalties"],
            ["Deprecation", "1 quarter notice", "12-18 months notice, sunset headers, migration guides"],
            ["Documentation", "Proto docs, in-house wiki", "Public developer portal, tutorials, Postman collections"],
        ],
    ) + mg([
        "<strong>BFF Pattern (Backend for Frontend):</strong> A dedicated API layer per client type (web BFF, mobile BFF, IoT BFF). Each BFF owns the contract for its consumer. This prevents shared APIs from being contaminated by client-specific concerns (e.g., mobile needing sparse fields, web needing rich fragments).",
        "<strong>API Products:</strong> Treat external APIs as products. Assign a <em>product manager</em>, publish a <em>roadmap</em>, maintain a <em>changelog</em>, and provide <em>support channels</em>. Implement a <em>developer portal</em> (SwaggerHub, Redocly, Backstage) for onboarding.",
        "<strong>Staff+ Governance:</strong> Design an <em>API review board</em> process: spec review → breaking change assessment → security audit → developer experience review → publish. Automate compliance checks in CI. Balance speed (internal) vs stability (external) with a <em>tiered API maturity model</em>.",
    ]),
    "tags": ["api", "design", "staff-plus", "interview-prep"],
    "language": "text",
    "sections": [],
})

# ---------------------------------------------------------------------------
# 15 – API Gateway & Service Mesh Patterns
# ---------------------------------------------------------------------------
S.append({
    "id": "api-design-staff-15",
    "title": "API Gateway & Service Mesh Patterns",
    "category": "api-design",
    "subcategory": "Staff+ Interviewing",
    "description": bd("GATEWAY", "#0D47A1") + tb(
        ["Pattern", "Responsibilities", "Examples"],
        [
            ["API Gateway (sidecar)", "Auth, rate limit, routing, transformation, caching", "Kong, Tyk, Apigee, AWS API Gateway, Zuul"],
            ["Service Mesh (sidecar)", "Service-to-service: mTLS, retry, circuit break, tracing", "Istio, Linkerd, Consul Connect, Envoy"],
            ["Ingress Gateway", "External entry point into mesh", "Istio Ingress, Contour, Traefik"],
            ["BFF Gateway", "Per-client aggregation and transformation", "GraphQL gateway, custom BFF layer"],
        ],
    ) + mg([
        "<strong>Gateway Responsibilities:</strong> Authentication (OAuth2 / JWT validation), rate limiting, request/response transformation, routing to upstream services, caching (GET responses), CORS enforcement, request logging, and circuit breaking. A gateway offloads cross-cutting concerns from services.",
        "<strong>Service Mesh Value:</strong> Provides <em>mTLS</em> (zero-trust encryption), <em>traffic splitting</em> (canary, blue-green), <em>circuit breaking</em> (envoy outlier detection), <em>distributed tracing</em> (OpenTelemetry), and <em>telemetry</em> (TCP-level metrics). Sidecar proxies manage this transparently.",
        "<strong>Staff+ Architecture Decision:</strong> Gateway vs Mesh — gateways handle north-south traffic (external → internal), meshes handle east-west (service → service). You need both at scale. Discuss <em>gateway chaining</em> (ingress → BFF → mesh → service) and <em>latency overhead</em> of proxy hops.",
    ]),
    "tags": ["api", "design", "staff-plus", "interview-prep"],
    "language": "text",
    "sections": [],
})

# ---------------------------------------------------------------------------
# 16 – API Design Interview Rubric & Sample Questions
# ---------------------------------------------------------------------------
S.append({
    "id": "api-design-staff-16",
    "title": "API Design Interview Rubric & Sample Questions",
    "category": "api-design",
    "subcategory": "Staff+ Interviewing",
    "description": bd("INTERVIEW RUBRIC", "#4527A0") + tb(
        ["Dimension", "Bar (Staff)", "Strong (Senior Staff)"],
        [
            ["Requirements Gathering", "Asks clarifying questions, defines scope", "Challenges ambiguous requirements, identifies implicit constraints, prioritizes by impact"],
            ["Trade-off Analysis", "Compares 2-3 options", "Systematic trade-off matrix, cites real-world examples from well-known APIs"],
            ["Schema Design", "Logical resource model, standard naming", "Evolvable schema, versioning strategy, backward compatibility baked in"],
            ["Protocol Choice", "Justifies REST / GraphQL / gRPC choice", "Hybrid protocol strategy, migration path, consumer-specific interfaces"],
            ["Security & Auth", "Covers authN/Z basics", "Defense-in-depth, token lifecycle, OWASP API-specific threats"],
            ["Scalability", "Mentions caching, pagination, rate limits", "Quantified load estimates, bottleneck analysis, horizontal scaling strategy"],
            ["Error Handling", "Standard error format, status codes", "Idempotency, retry strategy, error catalog, client guidance"],
            ["Communication", "Clear explanations, whiteboard sketches", "Structured thinking, adapts to interviewer signals, asks for feedback"],
        ],
    ) + mg([
        "<strong>Sample Question 1:</strong> \"Design a REST API for a collaborative document editing service (like Google Docs).\" Focus on resource model (docs, revisions, comments, presence), real-time sync (WebSocket + operational transforms), permissions, and conflict resolution.",
        "<strong>Sample Question 2:</strong> \"Design a payment processing API.\" Cover idempotency keys, webhooks (async confirmation), error handling (insufficient funds, declined), idempotency replay protection, and PCI compliance scope.",
        "<strong>Sample Question 3:</strong> \"Design a rate-limiting service API.\" Discuss configurable rate limit policies (per-consumer, per-endpoint), token bucket vs sliding window, multi-region replication, and coordination between gateway and services.",
        "<strong>Sample Question 4:</strong> \"Design a notification API.\" Cover push (FCM/APNS), pull (polling/SSE), webhooks, template management, delivery guarantees (at-least-once), unsubscribes, and delivery status tracking.",
    ]),
    "tags": ["api", "design", "staff-plus", "interview-prep"],
    "language": "text",
    "sections": [],
})

# ---------------------------------------------------------------------------
# 17 – References & Further Reading
# ---------------------------------------------------------------------------
S.append({
    "id": "api-design-staff-17",
    "title": "References & Further Reading",
    "category": "api-design",
    "subcategory": "Staff+ Interviewing",
    "description": bd("REFERENCES", "#212121") + mg([
        """<strong>Books:</strong> <em>API Design Patterns</em> (JJ Geewax), <em>The Design of Web APIs</em> (Arnaud Lauret), <em>RESTful Web APIs</em> (Richardson & Amundsen), <em>Building Microservices</em> (Sam Newman).""",
        """<strong>Specifications:</strong> OpenAPI 3.1 (https://spec.openapis.org/oas/v3.1.0), AsyncAPI 2.x (https://www.asyncapi.com), GraphQL June 2018 Spec (https://spec.graphql.org), Protocol Buffers v3 (https://protobuf.dev).""",
        """<strong>Standards & RFCs:</strong> HTTP Semantics (RFC 9110), HTTP Caching (RFC 9111), OAuth 2.0 (RFC 6749), JWT (RFC 7519), Idempotency (RFC 7231 §4.2.2), Problem Details (RFC 9457).""",
        """<strong>Tools:</strong> OpenAPI Generator, Stoplight Spectral, Optic, Prism, GraphiQL, Apollo Studio, grpcurl, Envoy, Istio, Kong, Tyk, OpenTelemetry, Prometheus, Grafana, Jaeger.""",
    ]),
    "tags": ["api", "design", "staff-plus", "interview-prep"],
    "language": "text",
    "sections": [],
})

# ---------------------------------------------------------------------------
# Write output
# ---------------------------------------------------------------------------
with open(OUT, 'w') as f:
    json.dump({"id": "api-design-staff", "title": "API Design for Staff+ Engineers", "sections": S}, f, indent=2)
