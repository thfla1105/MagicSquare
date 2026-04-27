from collections.abc import Sequence

from .contracts import (
    DUPLICATE_VALUES,
    INVALID_SIZE,
    INVALID_VALUE_RANGE,
    INVALID_ZERO_COUNT,
    ErrorResponse,
)


class InputValidator:
    def validate(self, grid: Sequence[Sequence[int]]) -> ErrorResponse | None:
        if len(grid) != 4 or any(len(row) != 4 for row in grid):
            return INVALID_SIZE

        flat_values = [value for row in grid for value in row]
        if any((not isinstance(value, int)) or value < 0 or value > 16 for value in flat_values):
            return INVALID_VALUE_RANGE

        if flat_values.count(0) != 2:
            return INVALID_ZERO_COUNT

        non_zero_values = [value for value in flat_values if value != 0]
        if len(non_zero_values) != len(set(non_zero_values)):
            return DUPLICATE_VALUES

        return None
