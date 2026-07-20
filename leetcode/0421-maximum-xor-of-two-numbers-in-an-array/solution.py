from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maximum_xor = 0
        prefix_mask = 0

        # 从最高位到最低位，依次判断当前位能否设为 1。
        for bit in range(30, -1, -1):
            prefix_mask |= 1 << bit
            prefixes = {number & prefix_mask for number in nums}
            candidate = maximum_xor | (1 << bit)

            if any(
                candidate ^ prefix in prefixes
                for prefix in prefixes
            ):
                maximum_xor = candidate

        return maximum_xor
