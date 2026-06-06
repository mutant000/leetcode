from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(row: int, col: int, node: TrieNode) -> None:
            char = board[row][col]

            if char not in node.children:
                return

            next_node = node.children[char]

            if next_node.word:
                result.append(next_node.word)
                next_node.word = None

            board[row][col] = "#"

            for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row = row + delta_row
                next_col = col + delta_col

                if 0 <= next_row < rows and 0 <= next_col < cols and board[next_row][next_col] != "#":
                    dfs(next_row, next_col, next_node)

            board[row][col] = char

            if not next_node.children and next_node.word is None:
                node.children.pop(char)

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root)

        return result
