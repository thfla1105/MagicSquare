from magicsquare import solve_magic_square


def test_e2e_ok_01_returns_int6_for_valid_solvable_grid(tq_01_grid: list[list[int]]) -> None:
    result = solve_magic_square(tq_01_grid)
    assert result == [3, 3, 6, 4, 4, 1]


def test_e2e_no_01_returns_no_solution_code_for_unsolved_grid(
    tq_nosol_grid: list[list[int]],
) -> None:
    result = solve_magic_square(tq_nosol_grid)
    assert result == {
        "code": "NO_SOLUTION",
        "message": "No placement makes a 4x4 magic square with magic sum 34.",
    }


def test_e2e_err_01_invalid_size() -> None:
    result = solve_magic_square([[1, 2], [3, 4]])
    assert result == {"code": "INVALID_SIZE", "message": "Grid must be 4x4."}


def test_e2e_err_02_invalid_value_range() -> None:
    grid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 0, 99],
    ]
    result = solve_magic_square(grid)
    assert result == {
        "code": "INVALID_VALUE_RANGE",
        "message": "Each cell must be 0 or 1..16.",
    }


def test_e2e_err_03_invalid_zero_count() -> None:
    grid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    result = solve_magic_square(grid)
    assert result == {
        "code": "INVALID_ZERO_COUNT",
        "message": "There must be exactly two zeros (empty cells).",
    }


def test_e2e_err_04_duplicate_values() -> None:
    grid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 10, 12],
        [13, 14, 0, 0],
    ]
    result = solve_magic_square(grid)
    assert result == {
        "code": "DUPLICATE_VALUES",
        "message": "Values 1..16 must not duplicate (excluding zeros).",
    }


def test_nfr_03_solver_is_deterministic(tq_01_grid: list[list[int]]) -> None:
    first = solve_magic_square(tq_01_grid)
    second = solve_magic_square(tq_01_grid)
    assert first == second


def test_nfr_04_input_grid_is_not_mutated(
    tq_01_grid: list[list[int]],
    deep_copy,
) -> None:
    original = deep_copy(tq_01_grid)
    _ = solve_magic_square(tq_01_grid)
    assert tq_01_grid == original
