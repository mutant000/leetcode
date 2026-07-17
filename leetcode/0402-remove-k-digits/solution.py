class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        increasing_digits = []

        # 第一步：遇到更小数字时，删除前面较大的数字。
        for digit in num:
            while (
                k > 0
                and increasing_digits
                and increasing_digits[-1] > digit
            ):
                increasing_digits.pop()
                k -= 1
            increasing_digits.append(digit)

        # 第二步：若仍需删除，去掉单调栈末尾最大的若干位。
        if k > 0:
            increasing_digits = increasing_digits[:-k]

        result = "".join(increasing_digits).lstrip("0")
        return result or "0"
