from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        reachable_jumps = {stone: set() for stone in stones}
        reachable_jumps[0].add(0)

        # 第一步：记录到达每块石头时可能使用的上一跳长度。
        for stone in stones:
            for previous_jump in reachable_jumps[stone]:
                # 第二步：从上一跳长度扩展出 k - 1、k、k + 1。
                for jump in (
                    previous_jump - 1,
                    previous_jump,
                    previous_jump + 1,
                ):
                    if jump <= 0:
                        continue

                    next_stone = stone + jump
                    if next_stone in reachable_jumps:
                        reachable_jumps[next_stone].add(jump)

        return bool(reachable_jumps[stones[-1]])
