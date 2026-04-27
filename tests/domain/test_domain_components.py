import pytest

from magicsquare.domain.empty_cell_locator import EmptyCellLocator
from magicsquare.domain.errors import NoMagicSolutionError
from magicsquare.domain.magic_square_resolver import MagicSquareResolver
from magicsquare.domain.magic_square_validator import MagicSquareValidator
from magicsquare.domain.missing_numbers_resolver import MissingNumbersResolver


def test_d12_empty_cell_locator_scans_row_major(tq_01_grid: list[list[int]]) -> None:
    first, second = EmptyCellLocator().locate(tq_01_grid)
    assert first == (2, 2)
    assert second == (3, 3)


def test_d01_missing_numbers_resolver_returns_sorted_pair(
    tq_01_grid: list[list[int]],
) -> None:
    assert MissingNumbersResolver().resolve(tq_01_grid) == (1, 6)


def test_d13_missing_numbers_for_nosol_fixture(tq_nosol_grid: list[list[int]]) -> None:
    assert MissingNumbersResolver().resolve(tq_nosol_grid) == (15, 16)


def test_d14_magic_square_validator_true_on_complete_magic_square() -> None:
    complete = [
        [16, 2, 3, 13],
        [5, 11, 10, 8],
        [9, 7, 6, 12],
        [4, 14, 15, 1],
    ]
    assert MagicSquareValidator().is_magic_square(complete)


def test_pi01_magic_square_validator_false_when_any_line_breaks() -> None:
    broken = [
        [16, 3, 2, 13],
        [5, 11, 10, 8],
        [9, 7, 6, 12],
        [4, 14, 15, 1],
    ]
    assert not MagicSquareValidator().is_magic_square(broken)


def test_d11_resolver_tries_two_placements_and_finds_solution_on_second_attempt(
    tq_01_grid: list[list[int]],
) -> None:
    result = MagicSquareResolver().resolve(tq_01_grid)
    assert result == [3, 3, 6, 4, 4, 1]


def test_d11_resolver_raises_when_both_attempts_fail(tq_nosol_grid: list[list[int]]) -> None:
    with pytest.raises(NoMagicSolutionError):
        MagicSquareResolver().resolve(tq_nosol_grid)
