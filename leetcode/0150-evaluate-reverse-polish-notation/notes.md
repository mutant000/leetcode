# 150. Evaluate Reverse Polish Notation

## 思路

逆波兰表达式可以用栈求值。遇到数字就入栈，遇到运算符就弹出右操作数和左操作数，计算后把结果放回栈。

除法题目要求向零截断，Python 中用 `int(left / right)` 可以得到这个效果。

## 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`
