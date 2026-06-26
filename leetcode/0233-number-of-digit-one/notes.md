# Number of Digit One

## 思路

按每一位分别统计数字 `1` 出现多少次。

设当前位权是 `factor`，把 `n` 拆成高位 `high`、当前位 `current`、低位 `low`：

- `current == 0`：这一位出现 `1` 的次数是 `high * factor`
- `current == 1`：次数是 `high * factor + low + 1`
- `current > 1`：次数是 `(high + 1) * factor`

把所有位的贡献相加。

## 复杂度

- 时间复杂度：`O(log n)`
- 空间复杂度：`O(1)`
