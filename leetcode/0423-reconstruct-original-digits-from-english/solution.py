from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        character_counts = Counter(s)
        digit_counts = [0] * 10

        # 第一步：用只出现在一个数字单词中的字母确定偶数。
        digit_counts[0] = character_counts["z"]
        digit_counts[2] = character_counts["w"]
        digit_counts[4] = character_counts["u"]
        digit_counts[6] = character_counts["x"]
        digit_counts[8] = character_counts["g"]

        # 第二步：扣除已确定数字的贡献，依次恢复其余数字。
        digit_counts[3] = character_counts["h"] - digit_counts[8]
        digit_counts[5] = character_counts["f"] - digit_counts[4]
        digit_counts[7] = character_counts["s"] - digit_counts[6]
        digit_counts[1] = (
            character_counts["o"]
            - digit_counts[0]
            - digit_counts[2]
            - digit_counts[4]
        )
        digit_counts[9] = (
            character_counts["i"]
            - digit_counts[5]
            - digit_counts[6]
            - digit_counts[8]
        )

        return "".join(
            str(digit) * digit_counts[digit]
            for digit in range(10)
        )
