class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        different_character_code = 0

        for character in s + t:
            different_character_code ^= ord(character)

        return chr(different_character_code)
