from __future__ import annotations

from collections.abc import Sequence


class Grid:
    def __init__(self, rows: Sequence[Sequence[int]]) -> None:
        self._rows = tuple(tuple(int(value) for value in row) for row in rows)

    def clone_rows(self) -> list[list[int]]:
        return [list(row) for row in self._rows]

    def as_tuple(self) -> tuple[tuple[int, ...], ...]:
        return self._rows
