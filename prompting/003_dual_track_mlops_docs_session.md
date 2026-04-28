# Prompt 003 — Dual Track UI·Logic · MLOps · PRD · README 세션

## 사용자 요청 요지 (시간 순)

1. **PRD 기반 의견**: `docs/5.PRD_MagicSquare_4x4_TDD.md`와 첨부 슬라이드(6.1 Dual-Track UI+Logic, 6.2 UX/Logic 언어·3단 매핑)를 바탕으로 Dual Track + MLOps 방향에 대한 검토.
2. **PRD 업데이트**: 위 정리를 `5.PRD_MagicSquare_4x4_TDD.md`에 반영(§2.3, §3 확장, §5 `NO_SOLUTION` 구분, §7.5 MLOps, §8 재구성·§8.4 표, §11 링크 등).
3. **TO-DO 참조 안내**: 체크리스트를 어떤 문서 기준으로 둘지 안내(PRD 단일 기준, §10 경로, §7.5 MLOps).
4. **`docs/6.TODO_…` 추가**: 체크박스 포함 상세 TO-DO·체크리스트 파일 생성, PRD §11에 링크.
5. **README 보강**: Dual-Track·구조·설치·테스트·문서 표 이후, **상세 TO-DO 리스트(실행 순서·원칙·0~6단계)** 작성.
6. **본 요청**: 지금까지의 **Prompting**을 `prompting/` 아래 정리, **`report/`** 에 **보고서**로 요약.

## 에이전트 응답·산출 요약

- Dual Track: **Boundary(API 계약) ≈ 무GUI UX Contract**, **Domain = Logic Track**; UI는 PRD Out of Scope이나 §8.5·§2.3으로 향후 확장 원칙 명시.
- **MLOps**: Ground truth는 **FR·결정론적 테스트**; ML이 최종 판정을 대체하지 않음(§7.5).
- PRD에 **NO_SOLUTION**을 입력 검증 우선순위와 분리하는 문단 추가.
- `docs/6.TODO_MagicSquare_4x4_Checklist.md`: 부트스트랩, 구현(도메인/경계/컨트롤), 테스트 3트랙, §8.4, AC, NFR·CI, 문서, MLOps·UI 선택.
- `README.md`: 문서 표 다음에 **TO-DO 리스트 (실행 순서)** 섹션(원칙 + 0~6단계 체크박스).

## 코드 변경 범위

- 본 세션에서 **애플리케이션 코드(`src/`)·테스트(`tests/`)는 수정하지 않음** (문서 중심).
- 문서·README만 갱신.

## 산출물 경로 (003 세션)

| 경로 | 설명 |
|------|------|
| `docs/5.PRD_MagicSquare_4x4_TDD.md` | Dual Track·MLOps·§8.4 등 반영본 |
| `docs/6.TODO_MagicSquare_4x4_Checklist.md` | 체크리스트 |
| `README.md` | TO-DO(실행 순서) 포함 |
| `prompting/003_dual_track_mlops_docs_session.md` | 본 파일 |
| `report/8.Session_Report_Documentation_DualTrack_2026-04-28.md` | 세션 보고서 |

## 프롬프트 작성 시 재사용 팁

- 요구를 **FR / AC / §8 트랙**으로만 쪼개면 PRD와 바로 정렬된다.
- “UI 테스트”는 Scope 밖이면 **API Boundary** 문구로만 요청한다.
- MLOps는 **§7.5**와 충돌하지 않게 “보조·실험·배포”로 한정한다.
