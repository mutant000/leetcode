# 446. Arithmetic Slices II - Subsequence

## 思路

令 `subsequences[i][difference]` 表示以 `nums[i]` 结尾、公差为 `difference`、长度至少为 `2` 的子序列数量。

枚举前一个位置 `left` 和当前位置 `right`：

- `subsequences[left][difference]` 中的每个序列加入 `nums[right]` 后，长度至少为 `3`，可以加入答案。
- `nums[left]` 和 `nums[right]` 本身形成一个新的长度为 `2` 的序列。它暂时不计入答案，但可以被后面的数字继续扩展。

## 复杂度

- 时间复杂度：`O(n^2)`
- 空间复杂度：`O(n^2)`
