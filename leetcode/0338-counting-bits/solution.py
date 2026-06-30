from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0] * (n + 1)

        for num in range(1, n + 1):
            bits[num] = bits[num >> 1] + (num & 1)

        return bits
