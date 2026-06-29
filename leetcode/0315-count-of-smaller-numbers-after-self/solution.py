from typing import List


class FenwickTree:
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)

    def add(self, index: int, delta: int) -> None:
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & -index

    def query(self, index: int) -> int:
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ranks = {num: i + 1 for i, num in enumerate(sorted(set(nums)))}
        tree = FenwickTree(len(ranks))
        answer = []

        for num in reversed(nums):
            rank = ranks[num]
            answer.append(tree.query(rank - 1))
            tree.add(rank, 1)

        return answer[::-1]
