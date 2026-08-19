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

## Retrospective

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

This is currently an initial browser-side experiment, not a production streaming implementation.

- Progressive MP4 playback with basic player state display.
- Mock realtime chat behind an adapter interface with connection-state feedback.
- A composed Storybook view for the video and chat layout.
- HLS/LL-HLS, QoE observability, high-volume chat processing, synchronization, and recovery logic are not yet implemented in the repository.

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
- `Frontend_Architecture_Boilerplate_Case_Study.pdf`
