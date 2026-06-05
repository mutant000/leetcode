from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        queue = deque([(1, 0)])
        visited = {1}

        while queue:
            square, moves = queue.popleft()

            if square == target:
                return moves

            for next_square in range(square + 1, min(square + 6, target) + 1):
                row, col = self.square_to_position(next_square, n)
                destination = board[row][col]

                if destination != -1:
                    next_square = destination

                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        return -1

    def square_to_position(self, square: int, n: int) -> tuple[int, int]:
        quotient, remainder = divmod(square - 1, n)
        row = n - 1 - quotient

        if quotient % 2 == 0:
            col = remainder
        else:
            col = n - 1 - remainder

        return row, col
