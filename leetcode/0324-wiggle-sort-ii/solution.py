from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        sorted_nums = sorted(nums)
        half = (len(nums) + 1) // 2
        small = sorted_nums[:half][::-1]
        large = sorted_nums[half:][::-1]

        nums[::2] = small
        nums[1::2] = large
