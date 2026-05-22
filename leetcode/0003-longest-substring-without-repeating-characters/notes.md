# 3. Longest Substring Without Repeating Characters

## 思路

滑动窗口维护当前不含重复字符的区间 `[left, right]`。用哈希表记录每个字符最近一次出现的位置。

如果当前字符在窗口内出现过，就把 `left` 移到上一次出现位置的右侧，然后更新答案长度。

## 复杂度

- Time: `O(n)`
- Space: `O(min(n, charset))`

## 边界

- 空字符串。
- 所有字符都相同。
- 重复字符出现在当前窗口左侧时不能回退 `left`。
