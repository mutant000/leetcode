class Solution:
    def firstUniqChar(self, s: str) -> int:
        character_counts = [0] * 26

        for character in s:
            character_counts[ord(character) - ord("a")] += 1

        for index, character in enumerate(s):
            if character_counts[ord(character) - ord("a")] == 1:
                return index

        return -1
