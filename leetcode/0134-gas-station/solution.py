from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        current_tank = 0
        start = 0

        for index, (gallon, price) in enumerate(zip(gas, cost)):
            diff = gallon - price
            total_tank += diff
            current_tank += diff

            if current_tank < 0:
                start = index + 1
                current_tank = 0

        if total_tank < 0:
            return -1

        return start
