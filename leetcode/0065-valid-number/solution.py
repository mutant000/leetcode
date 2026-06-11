class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        seen_digit = False
        seen_dot = False
        seen_exponent = False
        digit_after_exponent = True

        for index, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
                if seen_exponent:
                    digit_after_exponent = True
            elif char in "+-":
                if index > 0 and s[index - 1] not in "eE":
                    return False
            elif char == ".":
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            elif char in "eE":
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                digit_after_exponent = False
            else:
                return False

        return seen_digit and digit_after_exponent
