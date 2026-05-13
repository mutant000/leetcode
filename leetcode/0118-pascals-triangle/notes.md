# 118. Pascal's Triangle

## 思路

杨辉三角每一行的两边都是 `1`，中间每个数字来自上一行相邻两个数字之和。

例如：

```text
row[col] = 上一行[col - 1] + 上一行[col]
```

逐行生成即可。

## 复杂度

- Time: `O(numRows^2)`
- Space: `O(numRows^2)`

## 边界

- `numRows = 1` 时只返回 `[[1]]`。
- 每行第一个和最后一个数字不需要计算。
