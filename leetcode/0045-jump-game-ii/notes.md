# 45. Jump Game II

## 思路

把每一次跳跃能覆盖的下标区间看成一层 BFS。

遍历当前层的所有位置时，不断更新下一层能到达的最远下标 `farthest`。当扫描到当前层边界 `current_end` 时，说明必须完成一次跳跃，并把下一层边界更新为 `farthest`。

题目保证一定能到达最后一个位置，所以遍历到倒数第二个下标即可。

## 复杂度

- Time: `O(n)`。
- Space: `O(1)`。

## 边界

- 数组长度为 `1` 时不需要跳跃。
- 一次跳跃已经覆盖终点时，答案为 `1`。
- 中间有 `0` 也没关系，只要当前层中其他位置能继续扩展。

## 提交记录

- Accepted: https://leetcode.com/problems/jump-game-ii/submissions/2006801877/
- Testcases: `110 / 110`
- Runtime: `7 ms`
- Memory: `19.91 MB`
