from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate_one = None
        candidate_two = None
        count_one = 0
        count_two = 0

        for num in nums:
            if num == candidate_one:
                count_one += 1
            elif num == candidate_two:
                count_two += 1
            elif count_one == 0:
                candidate_one = num
                count_one = 1
            elif count_two == 0:
                candidate_two = num
                count_two = 1
            else:
                count_one -= 1
                count_two -= 1

        answer = []
        for candidate in (candidate_one, candidate_two):
            if candidate is not None and nums.count(candidate) > len(nums) // 3:
                answer.append(candidate)

        return answer
