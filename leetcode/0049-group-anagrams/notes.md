# 49. Group Anagrams

## 思路

异位词排序后会得到相同的字符序列。

遍历每个字符串，把排序后的元组作为哈希键，将原字符串加入对应分组。最后返回所有分组即可。

## 复杂度

- Time: `O(n * k log k)`，`k` 是单个字符串的最大长度。
- Space: `O(n * k)`，用于保存分组和排序键。

## 边界

- 空字符串排序后仍是合法键。
- 单个字符串会形成只包含自己的分组。
- 返回的分组顺序不影响 LeetCode 判题。

## 提交记录

- Accepted: https://leetcode.com/problems/group-anagrams/submissions/2006801819/
- Testcases: `128 / 128`
- Runtime: `7 ms`
- Memory: `22.64 MB`
