class EmptyCellLocator:
    def locate(self, grid: list[list[int]]) -> tuple[tuple[int, int], tuple[int, int]]:
        empty_cells = []
        for row_idx, row in enumerate(grid):
            for col_idx, value in enumerate(row):
                if value == 0:
                    empty_cells.append((row_idx, col_idx))
        return empty_cells[0], empty_cells[1]
