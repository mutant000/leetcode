from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        character_counts = Counter(s)

        # 出现次数不足 k 的字符不可能属于有效子串，用它分割问题。
        for character, count in character_counts.items():
            if count < k:
                return max(
                    self.longestSubstring(part, k)
                    for part in s.split(character)
                )

        return len(s)
