class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

        for right in range(n):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 2 or is_palindrome[left + 1][right - 1]):
                    is_palindrome[left][right] = True

        cuts = [0] * n

        for right in range(n):
            if is_palindrome[0][right]:
                cuts[right] = 0
            else:
                cuts[right] = right

                for left in range(1, right + 1):
                    if is_palindrome[left][right]:
                        cuts[right] = min(cuts[right], cuts[left - 1] + 1)

        return cuts[-1]
