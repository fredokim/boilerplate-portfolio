# Typed UI Boilerplate Portfolio

React, Next.js, Vue 보일러플레이트와 셋이 공유하는 NestJS 백엔드를 소개하기 위한 정적 포트폴리오
페이지입니다.

백엔드는 처음 React 보일러플레이트 안에 있었지만, 세 프론트엔드가 함께 쓰게 되면서 자기 저장소로
분리됐습니다. 다섯 번째 저장소 [BOILPLATE](https://github.com/fredokim/BOILPLATE)이 넷의 진입점이고,
공유 정책·ADR·`create-fredo-app` 생성기가 거기 있습니다.

## 포함 자료

- 아키텍처 소개 페이지: `index.html`
- 공통 아키텍처 다이어그램: `assets/architecture.svg`
- API 에러 출처 흐름 다이어그램: `assets/api-error-flow.svg`
- 포트폴리오 발표용 증빙 문서: `PORTFOLIO_EVIDENCE.md`
- 운영 콘솔 증빙 문서: `OPS_CONSOLE_EVIDENCE.md`

## 실행

HTML 파일을 직접 열어도 동작합니다.

```bash
python -m http.server 8088
```

브라우저에서 `http://127.0.0.1:8088`로 확인할 수 있습니다.
