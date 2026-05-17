# 105. Construct Binary Tree from Preorder and Inorder Traversal

## 思路

前序遍历的顺序是：根节点、左子树、右子树。

所以每次从 `preorder` 里取出的下一个值，就是当前子树的根节点。再用这个根节点去 `inorder` 中定位：
- 根节点左边是左子树。
- 根节点右边是右子树。

为了快速找到根节点在中序数组中的位置，先用哈希表保存 `值 -> 下标`。

## 复杂度

- Time: `O(n)`
- Space: `O(n)`

## 边界

- 只有一个节点。
- 树完全偏左或完全偏右。
- 前序和中序长度为 1。
