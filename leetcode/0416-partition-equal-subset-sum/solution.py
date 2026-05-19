from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        possible = [False] * (target + 1)
        possible[0] = True

        for number in nums:
            for current_sum in range(target, number - 1, -1):
                possible[current_sum] = (
                    possible[current_sum] or possible[current_sum - number]
                )

            if possible[target]:
                return True

        return possible[target]
