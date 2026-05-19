# 1143. Longest Common Subsequence

## 思路

用动态规划比较两个字符串的前缀。

`dp[i][j]` 表示 `text1[:i]` 和 `text2[:j]` 的最长公共子序列长度。如果当前两个字符相同，就继承左上角状态并加一；否则从“丢掉 `text1` 当前字符”和“丢掉 `text2` 当前字符”两种状态中取较大值。

实现中只保留上一行和当前行，把空间压缩到一维行数组。

## 复杂度

- Time: `O(m * n)`。
- Space: `O(n)`，`n` 是 `text2` 的长度。

## 边界

- 两个字符串完全相同，答案是字符串长度。
- 没有公共字符时答案为 `0`。
- 公共子序列不要求连续，只要求相对顺序一致。

## 提交记录

- Accepted: https://leetcode.com/problems/longest-common-subsequence/submissions/2006799803/
- Testcases: `47 / 47`
- Runtime: `202 ms`
- Memory: `19.23 MB`
