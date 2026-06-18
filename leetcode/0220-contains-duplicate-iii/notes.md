# Contains Duplicate III

## 思路

维护一个最多包含 `indexDiff` 个元素的滑动窗口。

把数值按大小分桶，桶宽为 `valueDiff + 1`。如果两个数在同一个桶里，它们的差一定不超过 `valueDiff`；如果在相邻桶里，再单独检查差值。

每处理一个新数字，就把超出窗口范围的旧数字从桶中删除。

## 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(indexDiff)`
