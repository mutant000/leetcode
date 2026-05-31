# 28. Find the Index of the First Occurrence in a String

## 思路

直接查找 `needle` 在 `haystack` 中第一次出现的位置。

Python 的 `find` 找到时返回起始下标，找不到时返回 `-1`，正好符合题目要求。

## 复杂度

- 时间复杂度：`O(n * m)`，取决于底层字符串匹配实现
- 空间复杂度：`O(1)`
