from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        max_length = max(map(len, words))

        @lru_cache(None)
        def dfs(index: int) -> List[str]:
            if index == len(s):
                return [""]

            sentences = []

            for end in range(index + 1, min(len(s), index + max_length) + 1):
                word = s[index:end]

                if word in words:
                    for suffix in dfs(end):
                        if suffix:
                            sentences.append(word + " " + suffix)
                        else:
                            sentences.append(word)

            return sentences

        return dfs(0)
