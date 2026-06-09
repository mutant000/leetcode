class Solution:
    def myAtoi(self, s: str) -> int:
        index = 0
        n = len(s)
        int_min = -(1 << 31)
        int_max = (1 << 31) - 1

        while index < n and s[index] == " ":
            index += 1

        sign = 1
        if index < n and s[index] in "+-":
            if s[index] == "-":
                sign = -1
            index += 1

        number = 0
        while index < n and s[index].isdigit():
            number = number * 10 + ord(s[index]) - ord("0")
            index += 1

            if sign == 1 and number > int_max:
                return int_max
            if sign == -1 and -number < int_min:
                return int_min

        return sign * number
