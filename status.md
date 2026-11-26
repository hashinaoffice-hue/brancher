# 지금의 brancher — 한눈에

> 2026.11.26 기준. 새로 시작할 때는 이 문서부터 읽는다. 결정의 이유는 [`decisions.md`](decisions.md), 기준은 [`brand/brand-book.md`](brand/brand-book.md).

## 브랜드

| 항목 | 지금 |
|---|---|
| 이름 | `brancher \| 브랜처` — branch(가지) + -er(사람) |
| 정체 | **가지를 뻗는 사람** ('1인 개발 브랜드'는 설명이 필요할 때만) |
| 태도 | **편리하고 즐거운 서비스를 만듭니다.** |
| 브랜드 문장 | **Branch out. Build ventures.** — 새로운 가지를 뻗고, 사업으로 키운다. |
| 슬로건 | **Every branch is a venture.** (웹 이름 장면에서만) |
| 원칙 | Branch out · **Ship with care** · Merge what works |
| 톤 | 정성스럽게, 그러나 단정하게. 짧고 사실로 |
| 비유 | 고객에게는 **정원**(나뭇가지), 만드는 사람에게는 **Git**(브랜치) |
| 세계관 | **브랜처의 정원** — 사람들이 필요한 것을 골라 일상 곁에 두는 곳. 정원은 늘 '브랜처의' 것 |
| 청중 | 고객 > 협업 상대·동료 개발자 > 광고·제휴 파트너 |
| 운영 | 1인, 이름 비공개 |

## 시각

- **로고:** 심볼(줄기 + 45° 가지 + 그린 스퀘어)과 워드마크(`brancher.`). 둘을 붙이지 않는다.
  - 그린 스퀘어 모서리: 심볼 약 16%, 워드마크 마침표 약 24%(글자 획 모서리와 같은 반경). 원본 그대로 — 2026.11.26 워드마크 원본 교체.
  - 심볼 줄기 = 워드마크 b의 줄기 × 1.97.
  - 슈퍼그래픽: 심볼 원본을 크게 잘라 배경으로 써도 된다 (자체 채널만).
- **컬러:** Black `#0F1110` · White · Green `#4FB88A`(결과물의 색, 결과물 장면은 면으로) · Green Deep `#2E7D5B`(제안).
- **서체:** Pretendard 700 / 600 / 400, 숫자는 고정폭.
- **형태:** 직선과 45°, 대각 라운드(왼쪽 위·오른쪽 아래), 그림자·그라데이션 없음, 주요 덩어리는 가운데.
- **정원 그림:** 웹 '정원' 장면에서만, 브랜드 잎 모양 하나로.

## 채널

| 채널 | 상태 | 할 일 |
|---|---|---|
| 인스타 `@brancher.dev` | 게시물 001–003 이미지 완성 | **프로필 소개를 바꾸기:** 가지를 뻗는 사람 / 편리하고 즐거운 서비스를 만듭니다. / brancher.lab@gmail.com |
| 메일 | `brancher.lab@gmail.com` | — |
| 도메인 | `brancher.kr`로 결정 (`brancher.dev`는 다른 사람 소유) | **구입 확인** |

## 웹

- **콘셉트:** 로고 안을 걷는 홈페이지 — [`channels/web-concept-v4.md`](channels/web-concept-v4.md)
- **시안 A (v4.12):** https://claude.ai/artifact/FBwWKj9Jxavz52zkwMe2t5 — 지금 '링크가 있는 누구나 볼 수 있음'
- **시안 B (v4.14):** https://claude.ai/artifact/8u6WQKJ7sbiqVVtanqALk2 — 비공개. A와 카피는 같고 시각 · 연출 · 길이만 다름. 전환을 늘리고 화면이 스크롤을 살짝 늦게 따라옴 → [`channels/web/prototype-b/`](channels/web/prototype-b/README.md). **A/B 결정 대기 (Q17)**
- **장면:** 서명 → 이름 → 줄기 → 가지 → 마침표 → 정원 → 문의 → 물러남 (A 약 14.6화면 · B 약 13화면)
- **카피 확정본:** [`channels/web-copy.md`](channels/web-copy.md)
- **원본:** [`channels/web/prototype/src.html`](channels/web/prototype/README.md) · 다시 뽑기 `python3 tools/build-web-prototype.py`
- **관리자 모드:** 시안 안에 있음(예시 데이터). 디자인은 v3 그대로 — 다시 만들 차례
- **아직 확인 못 한 것:** 아이폰 사파리, 인스타 앱 안 브라우저

## 가지

| 번호 | 이름 | 상태 | 남은 것 |
|---|---|---|---|
| `branch 01` | 핸드머니 | `open` · 출시 준비 중 | **merge 기준을 출시 전에 정하기** (지표 · 목표 · 기한) |

## 결정 대기

| # | 질문 | 컨설턴트 제안 |
|---|---|---|
| Q17 | 웹 시안 A(v4.12)와 B(v4.14) 중 어느 쪽으로 | B — 그린 진입 · 정원 톤 · 길이를 고친 쪽 |
| Q10 | 운영 웹 코드를 어디에 두나 | 이 저장소 `web/` |
| Q8 | 인사이트를 직접 만드나 | 분석 도구 + 관리자 화면 한 장 |
| Q3 | 닫은 가지를 공개하나 | 공개 — 정원의 '가지치기'로 |
| Q4 | 가지 오픈 주기 | 목표 주기 하나를 정해 공개 |
| Q5 | 제품 안에 "by brancher" 표기 | 가볍게 표기 |

## 다음 할 일 — 제안 순서

1. 시안을 아이폰 · 인스타 앱 안에서 확인
2. Q10 · 도메인 → **운영 v0**: 공개 페이지만 `brancher.kr`에, 공유 미리보기 이미지와 방문 통계 포함
3. 핸드머니 merge 기준 확정 (출시 전)
4. 관리자 모드를 v4 톤으로 다시 만들고 인사이트 연결 (Q8)
5. Q3 · Q4 · Q5

## 문서 지도

| 알고 싶은 것 | 문서 |
|---|---|
| 브랜드 기준 전부 | `brand/brand-book.md` |
| 소개 문구 | `brand/intro.md` |
| 로고 파일과 쓰는 법 | `brand/logo/README.md` |
| 왜 그렇게 정했나 | `decisions.md` |
| 웹 콘셉트 · 버전 기록 | `channels/web-concept-v4.md` · B안 차이 `channels/web/prototype-b/README.md` |
| 웹 문구 | `channels/web-copy.md` |
| 관리자 · 인사이트 · 숫자의 정의 | `channels/web.md` |
| 인스타 | `channels/instagram.md` |
| 가지 목록 · 기록 양식 | `branches/README.md` |
| 지난 문서 (기록용) | `brand/review-v1.md` · `brand/name-check.md` · `channels/web-direction.md` |
