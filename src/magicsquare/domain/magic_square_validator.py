"""4×4 완전 격자의 마방진(각 줄 합 동일) 판정."""

_MATRIX_ORDER = 4
_MAGIC_SUM = _MATRIX_ORDER * (_MATRIX_ORDER**2 + 1) // 2


def _row_sum(grid: list[list[int]], row: int) -> int:
    return sum(grid[row])


def _column_sum(grid: list[list[int]], col: int) -> int:
    return sum(grid[r][col] for r in range(_MATRIX_ORDER))


def _main_diagonal_sum(grid: list[list[int]]) -> int:
    return sum(grid[i][i] for i in range(_MATRIX_ORDER))


def _anti_diagonal_sum(grid: list[list[int]]) -> int:
    last = _MATRIX_ORDER - 1
    return sum(grid[i][last - i] for i in range(_MATRIX_ORDER))


class MagicSquareValidator:
    """`MATRIX_ORDER`×`MATRIX_ORDER` 고정; 마법 합은 표준 공식 `n(n²+1)/2`."""

    MATRIX_ORDER = _MATRIX_ORDER
    MAGIC_SUM = _MAGIC_SUM

    def is_magic_square(self, grid: list[list[int]]) -> bool:
        if any(0 in row for row in grid):
            return False

        line_sums: list[int] = []
        for r in range(self.MATRIX_ORDER):
            line_sums.append(_row_sum(grid, r))
        for c in range(self.MATRIX_ORDER):
            line_sums.append(_column_sum(grid, c))
        line_sums.append(_main_diagonal_sum(grid))
        line_sums.append(_anti_diagonal_sum(grid))

        return all(total == self.MAGIC_SUM for total in line_sums)
