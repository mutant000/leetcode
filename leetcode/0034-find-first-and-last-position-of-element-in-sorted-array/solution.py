from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(value: int) -> int:
            left = 0
            right = len(nums)

            while left < right:
                mid = (left + right) // 2
                if nums[mid] < value:
                    left = mid + 1
                else:
                    right = mid

            return left

        start = lower_bound(target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        end = lower_bound(target + 1) - 1
        return [start, end]
