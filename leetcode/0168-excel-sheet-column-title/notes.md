# Excel Sheet Column Title

## 思路

Excel 列名相当于没有 0 的 26 进制。

每轮先把 `columnNumber` 减 1，再取模 26 得到当前末尾字母：

```text
0 -> A, 1 -> B, ..., 25 -> Z
```

然后整除 26 继续处理前面的位。

## 复杂度

- 时间复杂度：`O(log columnNumber)`
- 空间复杂度：`O(log columnNumber)`
