class MagicSquareValidator:
    MAGIC_SUM = 34

    def is_magic_square(self, grid: list[list[int]]) -> bool:
        if any(0 in row for row in grid):
            return False

        line_sums = []
        for row in grid:
            line_sums.append(sum(row))

        for col in range(4):
            line_sums.append(sum(grid[row][col] for row in range(4)))

        line_sums.append(sum(grid[i][i] for i in range(4)))
        line_sums.append(sum(grid[i][3 - i] for i in range(4)))

        return all(total == self.MAGIC_SUM for total in line_sums)
