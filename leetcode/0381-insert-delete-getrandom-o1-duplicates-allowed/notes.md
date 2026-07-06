# 381. Insert Delete GetRandom O(1) - Duplicates allowed

## 思路

用数组保存所有值，方便 `getRandom`。同时用哈希表记录每个值出现在哪些下标。

删除时取出一个下标，把数组最后一个值搬到这个下标，再同步更新哈希表里的下标集合。

## 复杂度

- `insert` / `remove` / `getRandom` 平均时间复杂度：`O(1)`
- 空间复杂度：`O(n)`
