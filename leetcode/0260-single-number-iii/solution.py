from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for num in nums:
            xor_all ^= num

        low_bit = xor_all & -xor_all
        first = 0
        second = 0

        for num in nums:
            if num & low_bit:
                first ^= num
            else:
                second ^= num

        return [first, second]
