# Frontend Architecture Boilerplate Case Study

## Project Summary

Vue 3, React, Next.js 환경에서 확장 가능한 프론트엔드 개발 기반을 설계한 개인 프로젝트입니다. 단일 화면 구현보다 API 계약 안정성, UI와 로직의 책임 분리, 서버/클라이언트 경계, 상태관리 전략, 반복 작업 자동화, Storybook 기반 UI 문서화에 초점을 두었습니다.

## Role

- Frontend architecture 설계
- Vue 3 boilerplate 구성
- React boilerplate 구성
- Next.js boilerplate 구성
- Atomic UI component 구조 정리
- DTO 기반 API validation 계층 구성
- Storybook, MSW, test, build automation 구성

## Problem

- TypeScript 타입은 런타임 API 응답의 안정성을 보장하지 못합니다.
- UI 컴포넌트에 API, 상태 관리, routing 로직이 섞이면 재사용과 테스트가 어려워집니다.
- 매 프로젝트마다 Storybook, test, mock API, lint, build 설정을 반복하면 초기 세팅 비용이 커집니다.

## Solution

- API 응답을 envelope와 DTO class로 검증하는 통신 계층을 구성했습니다.
- React 버전은 View, Container, hook, HOC로 책임을 분리했습니다.
- Vue 버전은 Pinia, composable, lazy route, Atomic Design 구조를 적용했습니다.
- Next.js 버전은 Server Component, Client Component, Server Action, Zustand, TanStack Query의 책임을 상태 소유권 기준으로 분리했습니다.
- Storybook, MSW, Vitest, Playwright config, bundle analysis script를 기본 구성에 포함했습니다.
- `npm run check:ci` 명령으로 lint, typecheck, test, build, Storybook build를 한 번에 검증하도록 구성했습니다.

## Next.js State Strategy

- Initial route data: Server Component / server function
- Client-side refresh/cache: TanStack Query
- Global UI state: Zustand
- Auth/session source: httpOnly cookie + server session
- Mutation: Server Action
- Shareable filter state: URL `searchParams`
- Hydration-safe date UI: `SafeDate` / `useHydratedDate`

## Verified Result

React boilerplate 기준:

```bash
npm run check:ci
npm audit --audit-level=moderate
```

결과:

- lint 통과
- typecheck 통과
- test 통과
- production build 통과
- Storybook build 통과
- moderate 이상 취약점 0개

## Portfolio Assets

- `index.html`: 제출용 케이스 스터디 페이지
- `assets/architecture.svg`: 공통 아키텍처 다이어그램
- `assets/api-error-flow.svg`: API 에러 출처 구분 흐름
- `Frontend_Architecture_Boilerplate_Case_Study.pdf`: PDF 제출본
