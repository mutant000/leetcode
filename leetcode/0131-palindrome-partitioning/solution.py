from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

        for start in range(n - 1, -1, -1):
            for end in range(start, n):
                if s[start] == s[end] and (end - start <= 2 or is_palindrome[start + 1][end - 1]):
                    is_palindrome[start][end] = True

        result: List[List[str]] = []
        path: List[str] = []

        def dfs(start: int) -> None:
            if start == n:
                result.append(path.copy())
                return

            for end in range(start, n):
                if not is_palindrome[start][end]:
                    continue
                path.append(s[start : end + 1])
                dfs(end + 1)
                path.pop()

        dfs(0)
        return result
