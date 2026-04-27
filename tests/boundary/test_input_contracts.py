from magicsquare.boundary.input_validator import InputValidator


def test_u01_invalid_size_returns_invalid_size_first() -> None:
    grid = [[1, 2], [3, 4]]

    result = InputValidator().validate(grid)

    assert result is not None
    assert result.to_dict() == {"code": "INVALID_SIZE", "message": "Grid must be 4x4."}


def test_u02_invalid_value_range_returns_invalid_value_range() -> None:
    grid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 17, 12],
        [13, 14, 0, 0],
    ]

    result = InputValidator().validate(grid)

    assert result is not None
    assert result.to_dict() == {
        "code": "INVALID_VALUE_RANGE",
        "message": "Each cell must be 0 or 1..16.",
    }


def test_u03_invalid_zero_count_returns_invalid_zero_count() -> None:
    grid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]

    result = InputValidator().validate(grid)

    assert result is not None
    assert result.to_dict() == {
        "code": "INVALID_ZERO_COUNT",
        "message": "There must be exactly two zeros (empty cells).",
    }


def test_u04_duplicate_values_returns_duplicate_values() -> None:
    grid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 10, 12],
        [13, 14, 0, 0],
    ]

    result = InputValidator().validate(grid)

    assert result is not None
    assert result.to_dict() == {
        "code": "DUPLICATE_VALUES",
        "message": "Values 1..16 must not duplicate (excluding zeros).",
    }


def test_u05_validation_priority_size_then_range_then_zero_then_duplicate() -> None:
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 99],
    ]

    result = InputValidator().validate(grid)

    assert result is not None
    assert result.to_dict() == {"code": "INVALID_SIZE", "message": "Grid must be 4x4."}
