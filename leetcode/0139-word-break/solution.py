from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        max_length = max((len(word) for word in words), default=0)
        can_break = [False] * (len(s) + 1)
        can_break[0] = True

        for end in range(1, len(s) + 1):
            for length in range(1, min(max_length, end) + 1):
                start = end - length
                if can_break[start] and s[start:end] in words:
                    can_break[end] = True
                    break

        return can_break[-1]
