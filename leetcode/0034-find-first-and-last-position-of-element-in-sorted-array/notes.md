# 34. Find First and Last Position of Element in Sorted Array

## 思路

用两次二分查找。

`lower_bound(x)` 找到第一个大于等于 `x` 的位置：
- 第一次找 `target`，得到目标值第一次出现的位置。
- 第二次找 `target + 1`，得到第一个大于 `target` 的位置，再往前一格就是最后一次出现的位置。

如果第一次找到的位置越界，或者该位置不是 `target`，说明目标不存在。

## 复杂度

- Time: `O(log n)`
- Space: `O(1)`

## 边界

- 空数组。
- 目标只出现一次。
- 目标在数组开头或结尾。
