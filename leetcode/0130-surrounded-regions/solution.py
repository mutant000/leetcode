from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        def mark_safe(row: int, col: int) -> None:
            if board[row][col] != "O":
                return

            board[row][col] = "S"
            queue = deque([(row, col)])

            while queue:
                current_row, current_col = queue.popleft()

                for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = current_row + delta_row
                    next_col = current_col + delta_col

                    if 0 <= next_row < rows and 0 <= next_col < cols and board[next_row][next_col] == "O":
                        board[next_row][next_col] = "S"
                        queue.append((next_row, next_col))

        for row in range(rows):
            mark_safe(row, 0)
            mark_safe(row, cols - 1)

        for col in range(cols):
            mark_safe(0, col)
            mark_safe(rows - 1, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "S":
                    board[row][col] = "O"
