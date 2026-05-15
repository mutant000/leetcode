from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result: List[List[str]] = []
        placements = [-1] * n
        used_columns = set()
        used_diag_sum = set()
        used_diag_diff = set()

        def build_board() -> List[str]:
            board = []

            for row, column in enumerate(placements):
                board.append("." * column + "Q" + "." * (n - column - 1))

            return board

        def backtrack(row: int) -> None:
            if row == n:
                result.append(build_board())
                return

            for column in range(n):
                diag_sum = row + column
                diag_diff = row - column

                if column in used_columns:
                    continue
                if diag_sum in used_diag_sum:
                    continue
                if diag_diff in used_diag_diff:
                    continue

                placements[row] = column
                used_columns.add(column)
                used_diag_sum.add(diag_sum)
                used_diag_diff.add(diag_diff)

                backtrack(row + 1)

                used_columns.remove(column)
                used_diag_sum.remove(diag_sum)
                used_diag_diff.remove(diag_diff)
                placements[row] = -1

        backtrack(0)
        return result
