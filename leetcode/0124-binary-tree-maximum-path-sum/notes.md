# 124. Binary Tree Maximum Path Sum

## 思路

对每个节点计算“向父节点能贡献的最大路径和”。一条向上的路径只能选择左子树或右子树其中一边，所以返回 `node.val + max(left_gain, right_gain)`。

但答案路径可以在当前节点处拐弯，同时连接左、当前、右，因此用 `node.val + left_gain + right_gain` 更新全局最大值。负贡献会拖累结果，所以左右贡献小于 `0` 时直接当作 `0`。

## 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(h)`，`h` 是递归深度
