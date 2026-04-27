class MissingNumbersResolver:
    def resolve(self, grid: list[list[int]]) -> tuple[int, int]:
        existing_values = {value for row in grid for value in row if value != 0}
        missing = sorted(set(range(1, 17)) - existing_values)
        return missing[0], missing[1]
