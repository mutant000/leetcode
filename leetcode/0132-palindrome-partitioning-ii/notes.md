# Palindrome Partitioning II

## 思路

先预处理 `is_palindrome[left][right]`，表示子串 `s[left:right+1]` 是否是回文。

再用动态规划计算最少切割次数：

- 如果 `s[0:right+1]` 本身是回文，切割次数是 0。
- 否则枚举最后一段回文子串的起点 `left`，用 `cuts[left - 1] + 1` 更新答案。

## 复杂度

- 时间复杂度：`O(n^2)`
- 空间复杂度：`O(n^2)`
