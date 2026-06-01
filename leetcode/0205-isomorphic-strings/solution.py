class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for left, right in zip(s, t):
            if left in s_to_t and s_to_t[left] != right:
                return False
            if right in t_to_s and t_to_s[right] != left:
                return False

            s_to_t[left] = right
            t_to_s[right] = left

        return True
