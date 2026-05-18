class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        previous = list(range(len(word2) + 1))

        for row, char1 in enumerate(word1, 1):
            current = [row] + [0] * len(word2)
            for column, char2 in enumerate(word2, 1):
                if char1 == char2:
                    current[column] = previous[column - 1]
                else:
                    current[column] = 1 + min(
                        previous[column],
                        current[column - 1],
                        previous[column - 1],
                    )
            previous = current

        return previous[-1]
