from collections.abc import Sequence

from magicsquare.boundary.contracts import NO_SOLUTION
from magicsquare.boundary.input_validator import InputValidator
from magicsquare.domain.errors import NoMagicSolutionError
from magicsquare.domain.magic_square_resolver import MagicSquareResolver
from magicsquare.entity.grid import Grid


class SolveMagicSquareUseCase:
    def __init__(
        self,
        validator: InputValidator | None = None,
        resolver: MagicSquareResolver | None = None,
    ) -> None:
        self._validator = validator or InputValidator()
        self._resolver = resolver or MagicSquareResolver()

    def solve(self, grid: Sequence[Sequence[int]]) -> list[int] | dict[str, str]:
        validation_error = self._validator.validate(grid)
        if validation_error is not None:
            return validation_error.to_dict()

        snapshot = Grid(grid)
        try:
            return self._resolver.resolve(snapshot.clone_rows())
        except NoMagicSolutionError:
            return NO_SOLUTION.to_dict()


def solve_magic_square(grid: Sequence[Sequence[int]]) -> list[int] | dict[str, str]:
    return SolveMagicSquareUseCase().solve(grid)
