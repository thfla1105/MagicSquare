# Prompt 001 - 초기 구현 요청 요약

## 사용자 요청 핵심

- 부분적으로 비어 있는 4x4 Magic Square를 완성하는 Python 프로젝트 구현
- Boundary(입력 계약)와 Domain(순수 로직)의 Dual-Track TDD 준수
- 고정 오류 코드/메시지와 검증 우선순위 준수
- 성공 시 `int[6]`, 실패 시 `NO_SOLUTION` 반환
- `TQ-01`, `TQ-NOSOL` 기반 검증 및 E2E/커버리지 목표 충족

## 요구된 계약(핵심)

- `INVALID_SIZE`: `Grid must be 4x4.`
- `INVALID_VALUE_RANGE`: `Each cell must be 0 or 1..16.`
- `INVALID_ZERO_COUNT`: `There must be exactly two zeros (empty cells).`
- `DUPLICATE_VALUES`: `Values 1..16 must not duplicate (excluding zeros).`
- `NO_SOLUTION`: `No placement makes a 4x4 magic square with magic sum 34.`

검증 순서:

1. `INVALID_SIZE`
2. `INVALID_VALUE_RANGE`
3. `INVALID_ZERO_COUNT`
4. `DUPLICATE_VALUES`

## 수행 결과 요약

- `src/magicsquare`에 boundary/domain/control/entity 구조 구현
- `tests/boundary`, `tests/domain`, `tests/e2e` 테스트 추가
- 전체 테스트 통과: `22 passed`
- Domain/Boundary 커버리지 목표 충족 상태 확인
