from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answer = []
        path = []

        def backtrack(start: int, remaining_count: int, remaining_sum: int) -> None:
            if remaining_count == 0:
                if remaining_sum == 0:
                    answer.append(path[:])
                return

            for number in range(start, 10):
                if number > remaining_sum:
                    break
                path.append(number)
                backtrack(number + 1, remaining_count - 1, remaining_sum - number)
                path.pop()

        backtrack(1, k, n)

        return answer
