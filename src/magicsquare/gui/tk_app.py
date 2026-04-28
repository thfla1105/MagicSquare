"""4×4 마방진 풀이 데모 — tkinter."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk

from magicsquare import solve_magic_square

# tests/conftest tq_01_grid (PRD·E2E와 동일)
EXAMPLE_SOLVABLE: list[list[int]] = [
    [16, 2, 3, 13],
    [5, 11, 10, 8],
    [9, 7, 0, 12],
    [4, 14, 15, 0],
]

# tests/conftest tq_nosol_grid
EXAMPLE_NO_SOLUTION: list[list[int]] = [
    [0, 3, 2, 13],
    [5, 11, 10, 8],
    [9, 7, 6, 12],
    [4, 14, 0, 1],
]


class MagicSquareTkApp:
    def __init__(self, root: tk.Tk) -> None:
        self._root = root
        root.title("Magic Square 4×4")
        root.minsize(420,380)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)

        hdr = ttk.Frame(root, padding=8)
        hdr.grid(row=0, column=0, sticky="ew")
        ttk.Label(
            hdr,
            text="빈 칸은 0 (또는 비움=0). 1..16은 중복 없이, 0은 정확히 두 칸.",
            wraplength=400,
        ).pack(anchor="w")

        grid_fr = ttk.Frame(root, padding=8)
        grid_fr.grid(row=1, column=0, sticky="nsew")
        self._cells: list[list[tk.Entry]] = []
        for r in range(4):
            row_widgets: list[tk.Entry] = []
            ttk.Label(grid_fr, text=str(r + 1), width=2).grid(row=r + 1, column=0, padx=2, pady=2)
            for c in range(4):
                if r == 0:
                    ttk.Label(grid_fr, text=str(c + 1), width=4).grid(row=0, column=c + 1, padx=2, pady=2)
                e = tk.Entry(grid_fr, width=4, justify="center")
                e.grid(row=r + 1, column=c + 1, padx=2, pady=2, sticky="ew")
                row_widgets.append(e)
            self._cells.append(row_widgets)
        for c in range(4):
            grid_fr.columnconfigure(c + 1, weight=1)

        btn_fr = ttk.Frame(root, padding=8)
        btn_fr.grid(row=2, column=0, sticky="ew")
        ttk.Button(btn_fr, text="풀이", command=self._on_solve).pack(side="left", padx=4)
        ttk.Button(btn_fr, text="초기화", command=self._clear).pack(side="left", padx=4)
        ttk.Button(btn_fr, text="예시(해 있음)", command=lambda: self._load_grid(EXAMPLE_SOLVABLE)).pack(
            side="left", padx=4
        )
        ttk.Button(btn_fr, text="예시(해 없음)", command=lambda: self._load_grid(EXAMPLE_NO_SOLUTION)).pack(
            side="left", padx=4
        )

        self._status = tk.StringVar(value="준비됨")
        ttk.Label(root, textvariable=self._status, padding=6, relief="sunken", anchor="w").grid(
            row=3, column=0, sticky="ew"
        )

    def _read_grid(self) -> tuple[list[list[int]] | None, str | None]:
        g: list[list[int]] = []
        for r in range(4):
            row: list[int] = []
            for c in range(4):
                raw = self._cells[r][c].get().strip()
                if raw == "":
                    row.append(0)
                    continue
                try:
                    row.append(int(raw))
                except ValueError:
                    return None, f"({r+1},{c+1}) 칸: 정수만 입력해 주세요."
            g.append(row)
        return g, None

    def _load_grid(self, grid: list[list[int]]) -> None:
        for r in range(4):
            for c in range(4):
                self._cells[r][c].delete(0, tk.END)
                v = grid[r][c]
                if v != 0:
                    self._cells[r][c].insert(0, str(v))
        self._status.set("격자를 불러왔습니다. 「풀이」를 누르세요.")

    def _clear(self) -> None:
        for r in range(4):
            for c in range(4):
                self._cells[r][c].delete(0, tk.END)
        self._status.set("초기화됨")

    def _on_solve(self) -> None:
        grid, parse_err = self._read_grid()
        if parse_err:
            messagebox.showwarning("입력 오류", parse_err)
            self._status.set(parse_err)
            return

        result = solve_magic_square(grid)
        if isinstance(result, dict):
            code = result.get("code", "")
            msg = result.get("message", "")
            self._status.set(f"[{code}] {msg}")
            messagebox.showinfo("결과", f"{code}\n\n{msg}")
            return

        r1, c1, n1, r2, c2, n2 = result
        self._cells[r1 - 1][c1 - 1].delete(0, tk.END)
        self._cells[r1 - 1][c1 - 1].insert(0, str(n1))
        self._cells[r2 - 1][c2 - 1].delete(0, tk.END)
        self._cells[r2 - 1][c2 - 1].insert(0, str(n2))
        self._status.set(
            f"완료 — ({r1},{c1})={n1}, ({r2},{c2})={n2} (좌표 1-index)"
        )
        messagebox.showinfo("완료", f"배치: ({r1},{c1}) ← {n1}, ({r2},{c2}) ← {n2}")


def main() -> None:
    root = tk.Tk()
    MagicSquareTkApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
