class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        previous = [0] * (len(text2) + 1)

        for first_character in text1:
            current = [0] * (len(text2) + 1)
            for index, second_character in enumerate(text2, start=1):
                if first_character == second_character:
                    current[index] = previous[index - 1] + 1
                else:
                    current[index] = max(previous[index], current[index - 1])

            previous = current

        return previous[-1]
