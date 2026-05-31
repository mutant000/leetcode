from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows = len(board)
        columns = len(board[0])
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1),
        ]

        for row in range(rows):
            for column in range(columns):
                live_neighbors = 0

                for row_delta, column_delta in directions:
                    next_row = row + row_delta
                    next_column = column + column_delta

                    if 0 <= next_row < rows and 0 <= next_column < columns:
                        if board[next_row][next_column] in (1, 2):
                            live_neighbors += 1

                if board[row][column] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[row][column] = 2
                elif live_neighbors == 3:
                    board[row][column] = -1

        for row in range(rows):
            for column in range(columns):
                if board[row][column] == 2:
                    board[row][column] = 0
                elif board[row][column] == -1:
                    board[row][column] = 1
