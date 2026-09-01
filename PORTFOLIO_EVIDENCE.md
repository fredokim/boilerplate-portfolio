# Frontend Architecture Boilerplate Case Study

## Project Summary

This portfolio case study explains how the Vue, React, and Next.js boilerplates were designed as a reusable frontend architecture baseline.

The goal was not to create a single demo screen. The goal was to reduce repeated setup decisions and make API contracts, state ownership, component boundaries, UI states, testing, documentation, and automation visible from the start of a project.

## Role

- Frontend architecture design
- Vue 3 boilerplate structure
- React boilerplate structure
- Next.js boilerplate structure
- Component responsibility design
- DTO-based runtime API validation
- Storybook, MSW, test, build, dependency, and bundle automation
- AI-assisted development workflow and review criteria
- NestJS + Prisma + PostgreSQL backend satisfying the frontend's existing contract
- Single-origin deployment shape and container build

## Problem Definition

The project started from recurring frontend problems:

- TypeScript types alone cannot validate real API payloads at runtime.
- Components often mix API calls, state management, filtering, label conversion, event handling, and rendering.
- Server state, client cache, URL state, local UI state, and global client state are not clearly separated.
- Loading, empty, error, and invalid-data states are implemented differently per screen.
- Storybook, MSW, tests, and CI checks are often added after the UI structure has already diverged.
- AI-generated code can make repeated implementation faster, but without boundaries it can also spread inconsistent patterns.

I defined this as an architecture problem, not just a setup problem. The boilerplate needed to make good defaults visible and repeatable.

## Component Design Method

The boilerplates split code by responsibility.

| Responsibility | React | Vue | Next.js |
| --- | --- | --- | --- |
| Route/Page | lazy route | module route | App Router page |
| Data/Orchestration | container | store/composable | server module/client wrapper |
| Pure Rendering | view | view/component | view component |
| Reusable UI | atomic UI | atomic UI | server-safe UI |
| API Contract | DTO/API client | DTO/http client | DTO/server API |
| State Ownership | TanStack Query/Zustand | Pinia/composable | Server Component/TanStack Query/Zustand/URL |

The core rule is simple:

Code that changes for different reasons should not live in the same place.

## Key Decisions

### 1. Validate API data before UI rendering

API responses pass through envelope parsing and DTO validation before they reach UI components.

Reason:

- Runtime contract drift should fail near the API boundary.
- UI components should receive trusted data.
- Errors can be classified as frontend contract, backend response, network, or auth issues.

### 2. Split state by ownership

State is divided into server data, interactive cache, URL state, local UI state, and global client state.

Reason:

- Reloads, bookmarks, and back navigation become predictable.
- UI convenience state does not pollute server data.
- Global stores stay intentionally small.

### 3. Keep views as pure as possible

Views should render props and expose callbacks. Containers, stores, server modules, and hooks handle orchestration.

Reason:

- Views can be tested and documented in Storybook.
- Refactoring UI does not require rewriting API logic.
- AI-assisted refactors are easier to review when boundaries are explicit.

### 4. Prefer server-first boundaries in Next.js

Next.js uses Server Components for initial data and stable UI. Client Components are isolated to interactive leaves.

Reason:

- Reduce unnecessary client JavaScript.
- Lower hydration risk.
- Keep auth/session checks close to server boundaries.

### 5. Include Storybook, MSW, and verification gates early

Storybook, MSW, unit tests, accessibility checks, build checks, dependency checks, and bundle budgets are treated as architecture, not afterthoughts.

Reason:

- UI states can be reviewed before backend integration.
- Edge cases are easier to reproduce.
- Quality criteria are repeatable through commands, not memory.

## Results

- React, Vue, and Next.js boilerplates with aligned architecture principles.
- Runtime DTO/API contract validation.
- Storybook-ready UI and state components.
- MSW scenarios for success, empty, invalid DTO, backend error, and timeout states.
- CI-friendly verification commands for lint, typecheck, test, build, Storybook build, dependency review, and bundle budgets.
- AI workflow documents, prompt playbook, code review checklist, and refactoring case study.
- Next.js `/ops-console` proof surface for B2B dashboard, i18n, live updates, DTO validation, release status, and performance metrics.
- A NestJS backend the existing frontend talks to unchanged, verified end to end against a hosted PostgreSQL.
- Five CI jobs: frontend, server, integration against a real PostgreSQL, consumer contract, and a container smoke test.
- 506 automated tests across both packages, plus 4 Playwright specs in a real browser.

## React Interactive Examples

The React boilerplate also contains three implementation examples with deliberately different maturity levels.

### Dashboard Builder

- 12-column draggable and resizable widget layout.
- Registry-based KPI, chart, and table widget plugins with per-widget configuration editors.
- Draft/save/cancel and undo/redo flows, JSON import/export, permission checks, and local persistence.
- Global, local, and cross-widget filters coordinated through an event bus.
- Data-source registry, refresh policies, personalization presets, Storybook scenarios, and focused unit tests.

### Visual Graph / Topology Editor

- Typed graph document and presentation resolver separated from independently streamed runtime state.
- Batched runtime updates with duplicate, stale, dropped, coalesced, and unknown-entity diagnostics.
- Node health filters, selected-node metrics and history, stale indicators, reconnect, and resync behavior.
- Mock realtime transport plus unit tests for the runtime store and controller.

### Live Streaming + Realtime Chat

Chat now runs against a real WebSocket gateway rather than a mock transport.

- Progressive MP4 playback with basic player state display.
- Sending goes over HTTP and receiving over the socket, so the permission check, the idempotency key, and the rate limit have one implementation rather than two that must agree.
- Ordering, de-duplication, retention bounds, and batched flushing stay in the store; the transport only moves bytes.
- Reconnect resumes from the last applied sequence instead of refetching the room.
- HLS/LL-HLS, QoE observability, and load baselines are still not implemented.

## Backend Extension

The React boilerplate ran on MSW mocks. Those mocks described a contract; the backend implements it. The constraint was that the frontend must not change, so the server had to satisfy the existing DTOs, the shared response envelope, and the exact error code the API client branches on.

- **Authentication.** Argon2id password hashing, rotating refresh tokens stored as SHA-256 hashes, and family revocation when an already-used token is presented. Login equalises response time by hashing discarded random bytes for accounts that do not exist, so timing does not disclose which emails are registered.
- **Concurrency.** Dashboard writes use optimistic locking on a version column, so a second writer is rejected with a conflict rather than silently overwriting the first.
- **Schemaless data.** Versioned JSON is validated on write *and* on read, so a bad row already in the database cannot reach the screen.
- **Realtime.** Two WebSocket gateways authenticate during the handshake, disconnect slow consumers instead of growing a queue, and replay from a client's last sequence — falling back to a resync instruction when the gap exceeds retention.
- **Contract.** A 32-path OpenAPI document is generated from the code, and CI fails when the committed copy drifts from it.

Scale: 15 tables, 5 migrations, 226 server unit tests, 109 server e2e tests.

## What the Green Gates Did Not Prove

Every gate was passing — tests, typecheck, build, bundle budget, e2e — while four things were broken. None surfaced until the application ran against a real PostgreSQL in a browser. This section is the more useful half of the case study, because the fix in each case was to the *gate*, not only to the code.

1. **An endpoint nobody implemented.** The dashboard had always requested a user list; no route answered it. The contract test listed only endpoints that existed, so it agreed with itself. It now derives the list from the frontend source and compares path shapes, and the change was verified by deleting the path from the spec and watching the test fail.
2. **The data-mode switch did not reach the realtime features.** Two server transports were written and unit-tested but never imported: the wiring modules constructed the mock transports unconditionally. Server mode rendered generated messages and a fabricated event stream while the UI displayed "Connected".
3. **Token refresh was never wired.** A single-flight refresh helper existed, fully tested, and nothing called it, so sessions ended silently at the access token's lifetime. After wiring it, four parallel 401s were observed producing exactly one refresh — with a rotating token, four would have been read as replay and revoked the session family.
4. **A CI step that reported success without running.** The seed returned early when optional environment variables were absent, so the step passed while leaving most of the file unexecuted. It now runs in full, twice, because idempotence is a property only a second run demonstrates.

## Deployment Shape

The refresh token is an HttpOnly cookie with `sameSite: lax`. Hosting the client on a different origin from the API means the browser never sends it: sign-in succeeds and the session then ends without explanation. The WebSocket gateways fail the same way behind a rewrite layer. So the client and the API ship as one image and share an origin, which is also what the development proxy has been emulating.

- The SPA fallback returns index.html for navigations but hands anything under `/api` back to the router, so a missing route stays a JSON 404 rather than becoming a 200 full of HTML.
- `index.html` is served no-cache and hashed assets immutable.
- A production start refuses to boot when the cookie's secure flag is off.
- CI builds the image and smoke-tests the container: liveness answers without a database, readiness does not, the client is served, deep links reach the SPA, and unknown API paths still return 404.

Not yet done: nothing has been deployed to a hosting platform, and no load baseline has been measured.

## Retrospective

What worked:

- The boilerplate became a record of technical decisions, not just a file template.
- DTO validation and state ownership rules made the architecture easier to explain.
- Storybook/MSW made UI edge cases visible.
- AI-assisted development became safer when paired with review checklists and verification gates.

Trade-offs:

- The strict structure has upfront cost.
- Small MVPs may not need every layer from day one.
- DTOs, stories, and tests must be maintained to keep their value.

Next improvements:

- Split templates into lightweight, standard, and strict modes.
- Add token generation from a single design-token source.
- Expand auth, permission, feature flag, and observability examples.
- Add more E2E and accessibility examples for complex table/form flows.

## Related Files

- `next-boilerplate/DESIGN_RATIONALE.md`
- `react-boilerplate/DESIGN_RATIONALE.md`
- `vue-boilerplate/DESIGN_RATIONALE.md`
- `next-boilerplate/AI_REFACTORING_CASE_STUDY.md`
- `react-boilerplate/AI_REFACTORING_CASE_STUDY.md`
- `vue-boilerplate/AI_REFACTORING_CASE_STUDY.md`
- `react-boilerplate/server/ARCHITECTURE.md`
- `react-boilerplate/server/DEPLOYMENT.md`
- `react-boilerplate/API_CONTRACT.md`
- `Frontend_Architecture_Boilerplate_Case_Study.pdf`
