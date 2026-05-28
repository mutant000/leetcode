from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        left = 0
        best_left = 0
        best_length = float("inf")

        for right, char in enumerate(s):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            while missing == 0:
                window_length = right - left + 1
                if window_length < best_length:
                    best_left = left
                    best_length = window_length

                left_char = s[left]
                need[left_char] += 1
                if need[left_char] > 0:
                    missing += 1
                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_left:best_left + best_length]
