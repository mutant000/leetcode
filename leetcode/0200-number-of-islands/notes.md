# 200. Number of Islands

## 思路

从每个未访问过的陆地格子出发，做一次 DFS，把同一个岛上的所有陆地都标记成水。

外层遍历遇到新的 `"1"` 时，说明发现一个新岛屿，答案加一。DFS 用栈迭代处理上下左右四个方向，并在入栈前把格子改成 `"0"`，避免重复访问。

## 复杂度

- Time: `O(m * n)`。
- Space: `O(m * n)`，最坏情况下栈会保存整片陆地。

## 边界

- 全是水时答案为 `0`。
- 全是陆地时整张图只会被一次 DFS 覆盖。
- 斜向相邻不算连通，只检查上下左右。

## 提交记录

- Accepted: https://leetcode.com/problems/number-of-islands/submissions/2006802671/
- Testcases: `49 / 49`
- Runtime: `249 ms`
- Memory: `21.46 MB`
