from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        indexes = deque()
        result = []

        for right, num in enumerate(nums):
            while indexes and indexes[0] <= right - k:
                indexes.popleft()

            while indexes and nums[indexes[-1]] <= num:
                indexes.pop()

            indexes.append(right)

            if right >= k - 1:
                result.append(nums[indexes[0]])

        return result
