# 54. Spiral Matrix

## 思路

用四个边界表示还没遍历的矩形：`top`、`bottom`、`left`、`right`。每一轮依次走上边、右边、下边、左边，然后收缩对应边界。

走下边和左边前需要再次检查边界，避免单行或单列时重复加入元素。

## 复杂度

- Time: `O(mn)`
- Space: `O(1)` extra, not counting output

## 边界

- 只有一行。
- 只有一列。
- 非正方形矩阵。
