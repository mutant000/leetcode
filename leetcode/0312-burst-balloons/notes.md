# Burst Balloons

## 思路

区间动态规划。直接想第一个戳哪个气球比较难，因为旁边的气球会变化；反过来想每个区间里最后戳哪个气球。

给数组两边补上 `1`。`dp[left][right]` 表示只戳开区间 `(left, right)` 里面的气球时，最多能得到多少硬币。

如果 `last` 是这个区间最后被戳的气球，那么它旁边一定是 `left` 和 `right`：

```text
values[left] * values[last] * values[right]
```

再加上左右两个子区间的最优值。

## 复杂度

- 时间复杂度：`O(n^3)`
- 空间复杂度：`O(n^2)`
