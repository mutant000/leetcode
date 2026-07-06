from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        lengths = [1] * n
        previous = [-1] * n
        best_index = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and lengths[j] + 1 > lengths[i]:
                    lengths[i] = lengths[j] + 1
                    previous[i] = j
            if lengths[i] > lengths[best_index]:
                best_index = i

        answer = []
        while best_index != -1:
            answer.append(nums[best_index])
            best_index = previous[best_index]

        return answer[::-1]
