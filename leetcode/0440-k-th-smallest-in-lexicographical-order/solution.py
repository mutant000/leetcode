class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(first: int, next_prefix: int) -> int:
            steps = 0

            while first <= n:
                steps += min(n + 1, next_prefix) - first
                first *= 10
                next_prefix *= 10

            return steps

        current = 1
        k -= 1

        while k > 0:
            # 第一步：计算 current 前缀子树包含多少个合法数字。
            steps = count_steps(current, current + 1)

            if steps <= k:
                # 第二步：跳过整棵子树，移动到下一个兄弟前缀。
                current += 1
                k -= steps
            else:
                # 目标在当前子树中，进入第一个子节点。
                current *= 10
                k -= 1

        return current
