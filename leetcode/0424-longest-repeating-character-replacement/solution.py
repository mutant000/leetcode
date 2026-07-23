class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        left = 0
        max_frequency = 0
        best = 0

        for right, char in enumerate(s):
            index = ord(char) - ord("A")
            counts[index] += 1
            max_frequency = max(max_frequency, counts[index])

            while right - left + 1 - max_frequency > k:
                left_index = ord(s[left]) - ord("A")
                counts[left_index] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best
