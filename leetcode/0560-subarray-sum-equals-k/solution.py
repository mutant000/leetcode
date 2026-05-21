from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        prefix_sum = 0
        total = 0

        for number in nums:
            prefix_sum += number
            total += prefix_counts[prefix_sum - k]
            prefix_counts[prefix_sum] += 1

        return total
