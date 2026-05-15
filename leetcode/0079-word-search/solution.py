from collections import Counter
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        board_counter = Counter(char for row in board for char in row)
        word_counter = Counter(word)
        for char, needed in word_counter.items():
            if board_counter[char] < needed:
                return False

        if board_counter[word[0]] > board_counter[word[-1]]:
            word = word[::-1]

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(row: int, col: int, index: int) -> bool:
            if board[row][col] != word[index]:
                return False
            if index == len(word) - 1:
                return True

            original = board[row][col]
            board[row][col] = "#"

            for delta_row, delta_col in directions:
                next_row = row + delta_row
                next_col = col + delta_col
                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and board[next_row][next_col] == word[index + 1]
                    and dfs(next_row, next_col, index + 1)
                ):
                    board[row][col] = original
                    return True

            board[row][col] = original
            return False

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and dfs(row, col, 0):
                    return True

        return False
