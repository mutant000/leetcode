class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        two_steps_before = 1
        one_step_before = 1

        for index in range(1, len(s)):
            current = 0

            if s[index] != "0":
                current += one_step_before

            two_digit = int(s[index - 1 : index + 1])
            if 10 <= two_digit <= 26:
                current += two_steps_before

            two_steps_before = one_step_before
            one_step_before = current

        return one_step_before
