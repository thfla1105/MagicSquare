from magicsquare.domain.empty_cell_locator import EmptyCellLocator
from magicsquare.domain.magic_square_validator import MagicSquareValidator
from magicsquare.domain.missing_numbers_resolver import MissingNumbersResolver


def test_tq_nosol_both_candidate_placements_are_not_magic(
    tq_nosol_grid: list[list[int]],
) -> None:
    locator = EmptyCellLocator()
    resolver = MissingNumbersResolver()
    validator = MagicSquareValidator()

    first_empty, second_empty = locator.locate(tq_nosol_grid)
    low, high = resolver.resolve(tq_nosol_grid)

    candidate_low_high = [row[:] for row in tq_nosol_grid]
    candidate_low_high[first_empty[0]][first_empty[1]] = low
    candidate_low_high[second_empty[0]][second_empty[1]] = high

    candidate_high_low = [row[:] for row in tq_nosol_grid]
    candidate_high_low[first_empty[0]][first_empty[1]] = high
    candidate_high_low[second_empty[0]][second_empty[1]] = low

    assert not validator.is_magic_square(candidate_low_high)
    assert not validator.is_magic_square(candidate_high_low)
