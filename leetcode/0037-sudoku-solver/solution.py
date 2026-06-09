from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        for row in range(9):
            for col in range(9):
                value = board[row][col]

                if value == ".":
                    empty_cells.append((row, col))
                else:
                    rows[row].add(value)
                    cols[col].add(value)
                    boxes[(row // 3) * 3 + col // 3].add(value)

        def backtrack(index: int) -> bool:
            if index == len(empty_cells):
                return True

            best = index
            best_options = None

            for candidate in range(index, len(empty_cells)):
                row, col = empty_cells[candidate]
                box = (row // 3) * 3 + col // 3
                options = [str(num) for num in range(1, 10) if str(num) not in rows[row] and str(num) not in cols[col] and str(num) not in boxes[box]]

                if best_options is None or len(options) < len(best_options):
                    best = candidate
                    best_options = options

                if best_options == []:
                    break

            if not best_options:
                return False

            empty_cells[index], empty_cells[best] = empty_cells[best], empty_cells[index]
            row, col = empty_cells[index]
            box = (row // 3) * 3 + col // 3

            for value in best_options:
                board[row][col] = value
                rows[row].add(value)
                cols[col].add(value)
                boxes[box].add(value)

                if backtrack(index + 1):
                    return True

                rows[row].remove(value)
                cols[col].remove(value)
                boxes[box].remove(value)
                board[row][col] = "."

            empty_cells[index], empty_cells[best] = empty_cells[best], empty_cells[index]
            return False

        backtrack(0)
