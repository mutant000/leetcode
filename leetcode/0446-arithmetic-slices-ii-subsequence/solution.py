from collections import defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        subsequences = [defaultdict(int) for _ in nums]
        result = 0

        for right in range(len(nums)):
            for left in range(right):
                difference = nums[right] - nums[left]

                # 这些序列已有至少两个元素，加入 nums[right] 后才计入答案。
                extendable = subsequences[left][difference]
                result += extendable

                # 当前二元组也能成为之后继续扩展的长度为 2 的序列。
                subsequences[right][difference] += extendable + 1

        return result
