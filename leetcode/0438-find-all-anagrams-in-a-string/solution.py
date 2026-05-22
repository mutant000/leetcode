from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        need = Counter(p)
        window = Counter(s[: len(p)])
        result = []

        if window == need:
            result.append(0)

        for right in range(len(p), len(s)):
            left = right - len(p)
            outgoing = s[left]
            incoming = s[right]

            window[outgoing] -= 1
            if window[outgoing] == 0:
                del window[outgoing]
            window[incoming] += 1

            if window == need:
                result.append(left + 1)

        return result
