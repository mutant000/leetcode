from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        answer = nums[0]

        for number in nums[1:]:
            if number < 0:
                current_max, current_min = current_min, current_max

            current_max = max(number, current_max * number)
            current_min = min(number, current_min * number)
            answer = max(answer, current_max)

        return answer
