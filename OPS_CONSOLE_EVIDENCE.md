# Next.js Ops Console Portfolio Evidence

## Summary

Added `/ops-console` to the Next.js boilerplate and reflected it in the portfolio case study.

This addition is designed as a hiring-signal proof surface for senior frontend roles, especially roles asking for
Next.js, TypeScript, i18n, runtime API validation, monitoring, performance ownership, release visibility, and B2B
operations UI experience.

## Hiring Signals Covered

- Next.js App Router + TypeScript
- Runtime DTO/API envelope validation
- i18n with typed dictionaries
- Client-side realtime event feed
- B2B operations dashboard UI
- Core Web Vitals, error rate, latency, and release monitoring
- Design-system reuse through existing Card, Button, and DataTable components

## Main Files

- `next-boilerplate/src/app/ops-console/page.tsx`
- `next-boilerplate/src/features/ops/dto/OpsConsole.dto.ts`
- `next-boilerplate/src/features/ops/server/opsConsole.server.ts`
- `next-boilerplate/src/features/ops/i18n/opsDictionary.ts`
- `next-boilerplate/src/features/ops/components/LiveIncidentFeed.client.tsx`
- `next-boilerplate/src/features/ops/views/OpsConsoleView.tsx`

## Verification

```bash
npm run lint
npm run typecheck
npm run test
npm run build
```

All commands passed after the addition.
