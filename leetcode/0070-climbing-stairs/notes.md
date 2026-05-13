# 70. Climbing Stairs

## 思路

到达第 `n` 阶的最后一步只有两种情况：

- 从第 `n - 1` 阶走 1 步上来。
- 从第 `n - 2` 阶走 2 步上来。

所以：

```python
ways[n] = ways[n - 1] + ways[n - 2]
```

只需要保存前两项，不需要完整数组。

## 复杂度

- Time: `O(n)`
- Space: `O(1)`
