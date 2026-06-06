# 211. Design Add and Search Words Data Structure

## 思路

用 Trie 保存所有加入过的单词。普通字符沿着对应子节点继续走，单词结束时把节点标记为完整单词。

查询时如果遇到普通字符，就只走这一条边；如果遇到 `.`，它可以匹配任意一个字符，所以对当前节点的所有子节点做 DFS。

## 复杂度

- `addWord` 时间复杂度：`O(l)`
- `search` 最坏时间复杂度：`O(26^d * l)`，`d` 是通配符数量
- 空间复杂度：`O(total characters)`
