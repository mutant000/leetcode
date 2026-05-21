from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for number, count in counts.items():
            buckets[count].append(number)

        result = []
        for count in range(len(buckets) - 1, 0, -1):
            for number in buckets[count]:
                result.append(number)
                if len(result) == k:
                    return result

        return result
