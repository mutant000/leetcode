from functools import lru_cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(None)
        def dfs(left: str, right: str) -> bool:
            if left == right:
                return True

            if sorted(left) != sorted(right):
                return False

            for split in range(1, len(left)):
                if dfs(left[:split], right[:split]) and dfs(left[split:], right[split:]):
                    return True

                if dfs(left[:split], right[-split:]) and dfs(left[split:], right[:-split]):
                    return True

            return False

        return dfs(s1, s2)
