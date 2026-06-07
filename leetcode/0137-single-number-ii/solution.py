from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for bit in range(32):
            bit_count = 0

            for num in nums:
                bit_count += (num >> bit) & 1

            if bit_count % 3:
                result |= 1 << bit

        if result >= 1 << 31:
            result -= 1 << 32

        return result
