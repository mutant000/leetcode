from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        lexicographical_numbers = []
        current_number = 1

        # 第一步：沿着字典树优先向下访问当前数字的十倍。
        for _ in range(n):
            lexicographical_numbers.append(current_number)

            if current_number * 10 <= n:
                current_number *= 10
                continue

            # 第二步：无法向下时回退，找到可以访问的下一个兄弟节点。
            while current_number % 10 == 9 or current_number + 1 > n:
                current_number //= 10
            current_number += 1

        return lexicographical_numbers
