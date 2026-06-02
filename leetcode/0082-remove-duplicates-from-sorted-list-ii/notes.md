# 82. Remove Duplicates from Sorted List II

## 思路

链表已经排序，重复值一定连续出现。用虚拟头节点和 `previous` 指向当前确认保留部分的尾部。

如果发现当前值重复，就跳过这一整段相同值，并把 `previous.next` 接到重复段后面；如果不重复，就正常前进。

## 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`
