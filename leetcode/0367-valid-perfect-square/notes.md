# 367. Valid Perfect Square

## 思路

在 `1` 到 `num` 之间二分查找平方根。

如果某个 `mid * mid` 等于 `num`，说明是完全平方数；否则按大小移动左右边界。

## 复杂度

- 时间复杂度：`O(log num)`
- 空间复杂度：`O(1)`
