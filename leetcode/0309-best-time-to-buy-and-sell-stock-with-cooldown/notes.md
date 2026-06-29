# 309. Best Time to Buy and Sell Stock with Cooldown

## 思路

每天维护三种状态：

- `hold`：手里持有股票。
- `sold`：今天刚卖出。
- `rest`：今天不持股，也没有刚卖出。

买入只能从 `rest` 来，卖出只能从 `hold` 来，冷冻期通过 `sold` 到下一天的 `rest` 表达。

## 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`
