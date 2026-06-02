# 106. Construct Binary Tree from Inorder and Postorder Traversal

## 思路

后序遍历的最后一个元素是根节点。为了快速在中序遍历中定位根节点，先建立值到下标的哈希表。

从后序数组末尾往前取根。因为后序顺序是左、右、根，倒着取时要先构建右子树，再构建左子树。

## 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`
