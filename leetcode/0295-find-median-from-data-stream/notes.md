# 295. Find Median from Data Stream

## 思路

维护两个堆：`small` 保存较小的一半，用负数模拟最大堆；`large` 保存较大的一半，是普通最小堆。

每次插入后保证两个条件：`small` 中的数都不大于 `large` 中的数；`small` 的元素数量要么等于 `large`，要么多一个。这样奇数个元素时中位数就是 `small` 堆顶，偶数个元素时就是两个堆顶的平均值。

## 复杂度

- `addNum` 时间复杂度：`O(log n)`
- `findMedian` 时间复杂度：`O(1)`
- 空间复杂度：`O(n)`
