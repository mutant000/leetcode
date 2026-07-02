from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        answer = []

        for num in nums2:
            if counts[num] > 0:
                answer.append(num)
                counts[num] -= 1

        return answer
