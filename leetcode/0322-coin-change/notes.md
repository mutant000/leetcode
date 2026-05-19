# 322. Coin Change

## 思路

这是完全背包问题，每种硬币可以使用任意次。

`dp[x]` 表示凑出金额 `x` 所需的最少硬币数。初始化 `dp[0] = 0`，其他金额设成一个不可能的较大值。遍历每个硬币后，从该硬币面额开始向上更新金额：如果先凑出 `x - coin`，再加一枚当前硬币，就能得到 `x`。

最终如果 `dp[amount]` 仍然不可达，返回 `-1`。

## 复杂度

- Time: `O(amount * c)`，`c` 是硬币种类数。
- Space: `O(amount)`。

## 边界

- `amount = 0` 时答案为 `0`。
- 没有任何组合能凑出目标金额时返回 `-1`。
- 硬币顺序不影响最优值。

## 提交记录

- Accepted: https://leetcode.com/problems/coin-change/submissions/2006797674/
- Testcases: `189 / 189`
- Runtime: `431 ms`
- Memory: `19.60 MB`
