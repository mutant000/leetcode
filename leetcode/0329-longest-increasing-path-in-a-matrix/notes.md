# 329. Longest Increasing Path in a Matrix

## 思路

把每个格子当作起点，向上下左右更大的格子走。

同一个格子的最长路径会被重复用到，所以用缓存记住 `dfs(row, col)` 的结果。

## 复杂度

- 时间复杂度：`O(mn)`
- 空间复杂度：`O(mn)`
