import random
from collections import defaultdict
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.indices_by_value = defaultdict(list)

        # 第一步：预先收集每个数字出现的全部下标。
        for index, value in enumerate(nums):
            self.indices_by_value[value].append(index)

    def pick(self, target: int) -> int:
        # 第二步：在目标对应的下标中等概率随机选择一个。
        return random.choice(self.indices_by_value[target])
