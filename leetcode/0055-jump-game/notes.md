# 55. Jump Game

## 思路

贪心维护当前能到达的最远下标 `farthest`。

从左到右扫描数组，如果当前下标已经超过 `farthest`，说明这个位置无法到达，直接返回 `False`。否则用 `index + nums[index]` 更新最远可达位置；一旦覆盖最后一个下标，就可以返回 `True`。

## 复杂度

- Time: `O(n)`。
- Space: `O(1)`。

## 边界

- 只有一个元素时已经在终点。
- 起点为 `0` 且长度大于 `1` 时无法前进。
- 中间的 `0` 只有在最远覆盖断掉时才会导致失败。

## 提交记录

- Accepted: https://leetcode.com/problems/jump-game/submissions/2006802886/
- Testcases: `178 / 178`
- Runtime: `11 ms`
- Memory: `20.31 MB`
