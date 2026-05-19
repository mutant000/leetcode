# 994. Rotting Oranges

## 思路

多源 BFS：一开始所有腐烂橘子同时向外扩散。

先统计新鲜橘子数量，并把所有腐烂橘子加入队列。每一轮 BFS 代表经过一分钟，只处理当前队列中的橘子，把相邻的新鲜橘子变腐烂并加入下一轮队列。

如果新鲜橘子全部变腐烂，返回经过的分钟数；否则说明有橘子永远无法被感染，返回 `-1`。

## 复杂度

- Time: `O(m * n)`。
- Space: `O(m * n)`。

## 边界

- 一开始没有新鲜橘子时答案为 `0`。
- 新鲜橘子被空格隔开无法接触腐烂橘子时返回 `-1`。
- 多个腐烂源需要同时扩散，所以按层 BFS 计时。

## 提交记录

- Accepted: https://leetcode.com/problems/rotting-oranges/submissions/2006801793/
- Testcases: `307 / 307`
- Runtime: `4 ms`
- Memory: `19.32 MB`
