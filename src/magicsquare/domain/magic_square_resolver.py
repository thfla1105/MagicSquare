from .empty_cell_locator import EmptyCellLocator
from .errors import NoMagicSolutionError
from .magic_square_validator import MagicSquareValidator
from .missing_numbers_resolver import MissingNumbersResolver


class MagicSquareResolver:
    def __init__(
        self,
        locator: EmptyCellLocator | None = None,
        missing_numbers: MissingNumbersResolver | None = None,
        validator: MagicSquareValidator | None = None,
    ) -> None:
        self._locator = locator or EmptyCellLocator()
        self._missing_numbers = missing_numbers or MissingNumbersResolver()
        self._validator = validator or MagicSquareValidator()

    def resolve(self, grid: list[list[int]]) -> list[int]:
        first_empty, second_empty = self._locator.locate(grid)
        low, high = self._missing_numbers.resolve(grid)

        attempts = [(low, high), (high, low)]
        for first_value, second_value in attempts:
            candidate = [row[:] for row in grid]
            candidate[first_empty[0]][first_empty[1]] = first_value
            candidate[second_empty[0]][second_empty[1]] = second_value
            if self._validator.is_magic_square(candidate):
                return [
                    first_empty[0] + 1,
                    first_empty[1] + 1,
                    first_value,
                    second_empty[0] + 1,
                    second_empty[1] + 1,
                    second_value,
                ]

        raise NoMagicSolutionError()
