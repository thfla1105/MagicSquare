# Prompt 004 — 누적 세션 타임라인 (Chronology)

**범위**: MagicSquare 4×4 — Dual Track·PRD·문서·테스트 명세·venv·GitHub까지 이어진 사용자 요청 정리  
**관련**: `001`~`003`은 구간별 상세; 본 파일은 **전체 흐름**만 연결한다.

**관련 통합 보고**: [`report/10.Cumulative_Work_Summary_2026-04-28.md`](../report/10.Cumulative_Work_Summary_2026-04-28.md).

---

## 사용자 요청 (대화 순서·요지)

1. PRD와 첨부 슬라이드(6.1 Dual-Track, 6.2 UX/Logic·3단 매핑)를 바탕으로 Dual Track + MLOps 방향 **검토·의견**.
2. 위 컨셉을 **`docs/5.PRD_MagicSquare_4x4_TDD.md`에 반영**해 달라.
3. TO-DO 리스트를 **어떤 문서를 기준**으로 만들지 **안내**.
4. **체크리스트**를 `docs` 하위 파일로 **추가** (`docs/6.TODO_…`).
5. 지금까지 내용으로 **`README.md` 작성**.
6. **`README`에 TO-DO**를 자세히 (실행 순서·체크박스).
7. 지금까지 **Prompting → `prompting/`**, **보고서 → `report/`** 에 정리.
8. GitHub **`MagicSquare_14`** 에 작업 **전부 푸시**.
9. **`red` 브랜치** 생성.
10. 첨부 **테스트 양식**(테스트 조건·전제·성공/실패·특별 절차)에 맞춰 **문서 작성** → `docs/7`.
11. **`report/9`** 참조해 **실행 가능하도록** 보고서 **상세 재작성** (명령·22케이스 매핑 등).
12. 실행을 **가상 환경**에서 하도록 **안내** → README·`report/9`·`docs/7` 반영.
13. **모든 내용 GitHub에 올려줘** (커밋·`origin`/`magic14` 푸시).
14. **지금까지 내용을 report와 prompting에 각각 정리** (본 요청).

---

## 산출물 매핑 (요청 → 파일)

| 요청 축 | 주요 산출 |
|---------|-----------|
| PRD·Dual Track·MLOps | `docs/5.PRD_…` |
| TO-DO 체크리스트 | `docs/6.TODO_…` |
| 온보딩·venv·TO-DO 순서 | `README.md` |
| 테스트 명세 양식 | `docs/7` |
| 실행 가이드·venv·pytest | `report/9` |
| 문서 세션 요약 | `report/8` |
| 누적 인덱스 보고 | `report/10` |
| 프롬프트 구간 상세 | `001`~`003` |
| 누적 타임라인 | **본 파일 `004`** |

---

## 에이전트 쪽 메모

- **코드 변경 없음**: 문서 중심 세션 구간에서 `src/`·`tests/` 미수정; 회귀는 `pytest`로 확인.
- **`NO_SOLUTION`**: PRD §5에서 입력 검증 우선순위와 **구분** — 문서·테스트 설명 전반에 반영.
- **Git**: `red` 생성·`main` 병합·원격 푸시; 네트워크 타임아웃 시 재시도·`fetch`로 정합성 확인.

---

## 재사용 시

새 세션에서는 **`report/10`** 과 **`prompting/004`** 를 먼저 열어 범위를 맞춘 뒤, 상세는 **`003`(PRD 세션)** · **`report/9`(실행)** 을 분기한다.
