class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_start = 0
        best_end = 0

        def expand(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for center in range(len(s)):
            left, right = expand(center, center)
            if right - left > best_end - best_start:
                best_start, best_end = left, right

            left, right = expand(center, center + 1)
            if right - left > best_end - best_start:
                best_start, best_end = left, right

        return s[best_start : best_end + 1]
