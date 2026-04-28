# MagicSquare 4×4

부분적으로 비어 있는 **4×4** 격자(빈칸은 `0`)에서 **빈칸 두 곳**에 수를 넣어 **고전 마방진**(행·열·두 대각선 10개 선의 합이 모두 **34**)을 완성할 수 있는지 판단하는 **Python** 프로젝트입니다. 요구사항·테스트 기준은 **[제품 요구사항(PRD)](docs/5.PRD_MagicSquare_4x4_TDD.md)** 에 단일화되어 있습니다.

## Dual-Track TDD

- **Boundary(API 계약)**: 입력 검증(FR-01), 정해진 `code`/`message`(§5), 검증 **우선순위**. 무효 입력에서는 Domain을 호출하지 않습니다.
- **Domain(순수 로직)**: 빈칸 탐색(FR-02), 누락 수(FR-03), 완성 판정(FR-04), 최대 두 번의 배치 시도(FR-05).
- **Control**: Boundary 통과 시 Domain을 호출하고, 성공 시 `int[6]`(좌표·값, **1-index**), 실패 시 표준 오류 dict로 매핑합니다.
- **UI**: PRD **§2.4** — 로컬 **`tkinter`** 데모(`magicsquare.gui`). **웹/서버 UI** 는 Out of Scope(§2.2). 핵심 계약은 여전히 `solve_magic_square` API이다. MLOps는 선택이며, **Ground truth**는 PRD §7.5대로 **FR·결정론적 테스트**로 둔다.

테스트는 **Boundary / Domain / E2E** 로 나누며, 시나리오는 PRD **§8.4**와 맞춥니다.

## 프로젝트 구조

| 경로 | 설명 |
|------|------|
| `src/magicsquare/boundary` | 입력 검증·오류 계약 |
| `src/magicsquare/domain` | 해 탐색·판정 로직 |
| `src/magicsquare/control` | 유스케이스 조합 |
| `src/magicsquare/gui` | **tkinter** 데스크톱 데모 (격자 입력·풀이) |
| `tests/boundary`, `tests/domain`, `tests/e2e` | 이중 트랙 + 통합 시나리오 |
| `docs/` | PRD, 구현 체크리스트 |
| `report/` | 진행·제안 문서(상세 규칙은 PRD 우선) |

## 요구 사항

- Python **3.10+**

## 설치 (가상 환경 권장)

프로젝트별로 패키지를 격리하려면 저장소 **루트**에서 가상 환경을 만든 뒤 활성화한다.

### Windows (PowerShell)

```powershell
Set-Location C:\DEV\MagicSquare
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -e ".[dev]"
```

실행 정책 오류가 나면(일회성):  
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### Windows (cmd)

```bat
cd C:\DEV\MagicSquare
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -U pip
pip install -e ".[dev]"
```

### macOS / Linux (bash 등)

```bash
cd /path/to/MagicSquare
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -e ".[dev]"
```

**비활성화**: 터미널에서 `deactivate` (가상 환경이 켜진 상태에서만).

### 가상 환경 없이 (전역 `pip`)

격리가 필요 없으면 루트에서 바로 `pip install -e ".[dev]"` 만 실행해도 된다.

## 테스트

가상 환경을 **활성화한 같은 터미널**에서 저장소 루트에서 실행한다.

```bash
python -m pytest tests
```

간단한 요약만 보려면 `python -m pytest tests -q`  
(프로젝트에 `pytest` 가 들어 있으면 `pytest` 단독 명령도 동일하게 동작한다.)

## GUI (tkinter)

패키지를 설치한 뒤(PRD §2.4):

```bash
magicsquare-gui
```

또는 모듈 실행:

```bash
python -m magicsquare.gui.tk_app
```

- **풀이**: 현재 격자를 읽어 `solve_magic_square` 호출 — 성공 시 빈 칸 두 곳에 값을 채우고, 오류·`NO_SOLUTION` 은 대화상자·상태줄에 **PRD §5** 문구 그대로 표시.
- **예시(해 있음/없음)**: E2E·`conftest` 와 동일한 격자를 불러온다.
- **Windows**: Python 설치 시 **tcl/tk** 포함 여부를 확인한다. (공식 python.org 설치본은 보통 포함.)

## 문서

| 문서 | 내용 |
|------|------|
| [docs/5.PRD_MagicSquare_4x4_TDD.md](docs/5.PRD_MagicSquare_4x4_TDD.md) | FR, 오류 계약, API, NFR, Dual-Track 전략, MLOps 역할(§7.5) |
| [docs/6.TODO_MagicSquare_4x4_Checklist.md](docs/6.TODO_MagicSquare_4x4_Checklist.md) | 구현·테스트 **체크리스트** (PRD 추적용) |

## TO-DO 리스트 (실행 순서)

**근거**: [PRD](docs/5.PRD_MagicSquare_4x4_TDD.md)가 단일 기준이다. 아래는 **권장 작업 순서**와 **완료의 의미**를 정리한 것이고, 항목별 `[ ]`는 README에서도 쓰되 **세부 체크·갱신**은 [체크리스트 문서](docs/6.TODO_MagicSquare_4x4_Checklist.md)와 함께 두는 것을 권장한다.

**원칙**

- **로직(Domain) 테스트**와 **경계(Boundary) 테스트**는 서로 최소한만 알게 유지한다(PRD §3 독립성).
- 테스트·할 일로 옮길 때는 PRD **§8.0**처럼 **판단 결과가 명확한** 요구만 쓴다(애매한 문장은 추적서만).
- **`NO_SOLUTION`**(PRD §5)은 입력 검증 우선순위가 아니라, **유효 격자**에 대해 두 배치 시도가 모두 실패했을 때의 **도메인 결과**다.

### 0단계 — 부트스트랩

개발 환경과 패키지 경로를 고정한 뒤 TDD로 들어간다.

- [ ] Python **3.10+** , `pip install -e ".[dev]"` 로 편집 가능 설치 및 `pytest` 실행 확인
- [ ] `src/magicsquare/{boundary,domain,control,entity}` 와 `tests/{boundary,domain,e2e}` 가 PRD §10과 일치하는지 확인
- [ ] (선택) 커버리지 도구·`pytest` 설정을 CI 목표(NFR-01·02)에 맞게 준비

### 1단계 — Logic Track (Domain 중심, FR-02 ~ FR-05)

**먼저** “격자가 이미 유효하다”는 가정 하에 수학·배치 규칙을 검증하면, 테스트가 단순해지고 Boundary와 섞이지 않는다.

- [ ] **FR-02**: 빈칸(`0`) 두 칸의 좌표를 **행 우선(row-major)** 순으로 찾는다
- [ ] **FR-03**: 이미 채워진 `1..16` 을 빼서 **누락된 두 수** `{a,b}` 를 구한다
- [ ] **FR-04**: `0` 이 없는 완전 격자에 대해 **4행·4열·주·부대각선** 합이 모두 **34** 인지 판정한다
- [ ] **FR-05**: 누락 두 수에 대해 (1) 작은 수→첫 빈칸·큰 수→둘째 빈칸, (2) 그 반대 — **최대 두 번**만 시도하고, 성공 시 좌표·값을 반환한다
- [ ] **FR-05**: 두 시도 모두 실패하면 **해 없음**을 명확한 방식(예외·`Result`·플래그)으로 표현한다(Control이 `NO_SOLUTION` dict로 매핑)
- [ ] **NFR-04**: Domain 함수들이 **인자로 받은 `grid` 를 수정하지 않는다**(복사·불변 사용)
- [ ] **Domain 테스트**: 위 항목별 단위 테스트 + PRD **TQ-NOSOL**(두 시도 모두 실패하는 입력 증명/ fixture)

### 2단계 — Boundary (FR-01, 오류 계약 §5)

경계는 **외부 계약**만 본다. **문자열은 PRD 표와 완전 일치**해야 하며, 여러 규칙이 동시에 깨지면 **우선순위**대로 하나의 `code` 만 나와야 한다.

- [ ] 4×4 가 아니면 `INVALID_SIZE` + 지정 `message`
- [ ] 셀이 `0` 또는 `1..16` 이 아니면 `INVALID_VALUE_RANGE`
- [ ] `0` 의 개수가 정확히 2가 아니면 `INVALID_ZERO_COUNT`
- [ ] `0` 을 제외하고 `1..16` 중복이 있으면 `DUPLICATE_VALUES`
- [ ] 검증 순서: **SIZE → RANGE → ZERO_COUNT → DUPLICATE**
- [ ] 무효 입력이면 **Domain(해결 로직)을 호출하지 않는다**(mock/spy·구조로 검증)
- [ ] **Boundary 테스트**: 오류별·우선순위·미호출 AC-01

### 3단계 — Control (유스케이스 연결)

공개 진입점 하나에서 Boundary → Domain → 응답 형식을 맞춘다.

- [ ] Boundary 통과 후에만 Domain 호출
- [ ] 성공 시 **`list[int]` 길이 6**, `[r1,c1,n1,r2,c2,n2]` **1-index**(PRD §6.2)
- [ ] Domain “해 없음” → `code` / `message` 가 PRD **§5 `NO_SOLUTION`** 과 정확히 일치하는 `dict`
- [ ] Boundary에서 이미 거른 오류는 그대로 `dict` 반환; 성공 시에만 `list` 반환

### 4단계 — E2E 및 §8.4 시나리오

트랙을 나눈 뒤, **같은 사용자 시나리오**가 끝까지 맞는지 통합한다.

- [ ] 유효 입력·해 존재 → `int[6]` (**E2E-OK**, AC-02)
- [ ] 유효 입력·해 없음 → `NO_SOLUTION` (**E2E-NO**, AC-03)
- [ ] 무효 입력 → 해당 계약 오류, 해 형태 아님 (**E2E-ERR**, AC-01)
- [ ] 동일 입력 두 번 호출 시 **동일 출력**(AC-04, NFR-03)
- [ ] 호출 후 원본 `grid` **비변형**(AC-04, NFR-04)
- [ ] PRD **§8.4** 네 가지 줄(검증 실패 / 해 있음 / `NO_SOLUTION` / 재호출)마다 대응 테스트가 있는지 점검

### 5단계 — 품질 게이트·문서

- [ ] **NFR-01**: Domain 라인 커버리지 ≥ **95%**
- [ ] **NFR-02**: Boundary 라인 커버리지 ≥ **85%**
- [ ] CI(또는 로컬 스크립트)에서 `pytest` + 커버리지 **임계치 실패 시 빌드 실패**
- [ ] FR·AC·테스트 함수에 **TC-ID** 또는 이슈 링크로 추적표 유지(§11)
- [ ] API **입출력 예시**를 PRD 또는 부록에 추가

### 6단계 — 선택

- [ ] **MLOps**(§7.5): 실험·모델 버전 정책 등 — **최종 정답은 FR·골든 테스트**가 정의 (ML이 대체하지 않음)
- [ ] **웹 UI**(PRD §2.2): 브라우저 프론트 추가 시 PRD §8.4 와 동일 시나리오를 UX 테스트로 복제

---

## 범위 (요약)

**In scope**: 4×4 고정, 값 `0` 또는 `1..16`, 빈칸 정확히 2개, 마방진 합 34, 두 배치 시도 규칙(PRD **FR-05**), **로컬 tkinter 데모**(PRD **§2.4**).

**Out of scope**: N×N 일반화, **웹·SPA·서버 중심 UI**, DB, 임의 퍼즐 생성기(PRD §2.2).
