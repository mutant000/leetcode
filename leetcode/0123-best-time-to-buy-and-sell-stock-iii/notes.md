# Best Time to Buy and Sell Stock III

## 思路

最多做两次交易，可以把过程拆成四个状态：

- `first_buy`：第一次买入后手上的最大收益。
- `first_sell`：第一次卖出后手上的最大收益。
- `second_buy`：第二次买入后手上的最大收益。
- `second_sell`：第二次卖出后手上的最大收益。

每天用当前价格更新这四个状态。最后 `second_sell` 就是最多两次交易后的最大利润。

## 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`
