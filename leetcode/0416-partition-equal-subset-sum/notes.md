# 416. Partition Equal Subset Sum

## 思路

两个子集和相等，等价于是否能从数组中选出若干数凑成总和的一半。

如果总和是奇数，必然无法平分。否则做 0/1 背包：`possible[x]` 表示是否能选出一些数凑出和 `x`。遍历每个数字时，从 `target` 倒序更新，避免同一个数字在一轮中被重复使用。

## 复杂度

- Time: `O(n * target)`。
- Space: `O(target)`。

## 边界

- 总和为奇数直接返回 `False`。
- 某个前缀已经凑出 `target` 时可以提前返回。
- 每个数字只能使用一次，所以必须倒序更新。

## 提交记录

- Accepted: https://leetcode.com/problems/partition-equal-subset-sum/submissions/2006799258/
- Testcases: `147 / 147`
- Runtime: `455 ms`
- Memory: `19.30 MB`
