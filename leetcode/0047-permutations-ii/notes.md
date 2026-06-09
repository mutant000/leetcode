# Permutations II

## 思路

先排序，再用回溯生成排列。

`used[index]` 表示当前数字是否已经放进路径。为了避免重复排列，遇到相同数字时，只允许先使用前一个相同数字，再使用后一个。

这个剪枝条件是：

```text
nums[index] == nums[index - 1] and not used[index - 1]
```

## 复杂度

- 时间复杂度：`O(n * n!)`
- 空间复杂度：`O(n)`，不计返回结果
