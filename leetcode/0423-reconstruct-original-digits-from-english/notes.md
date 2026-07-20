# 423. Reconstruct Original Digits from English

## 思路

统计所有字母出现次数。部分字母只出现在一个数字单词中，可以直接确定对应数字：`z -> zero`、`w -> two`、`u -> four`、`x -> six`、`g -> eight`。

确定这些数字后，从相关字母次数中扣除它们的贡献，再依次得到 `three`、`five`、`seven`、`one` 和 `nine`。最后按数字从小到大的顺序重复输出。

## 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`，字母和数字种类固定
