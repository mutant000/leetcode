class Solution:
    def longestPalindrome(self, s: str) -> int:
        unpaired_characters = set()
        palindrome_length = 0

        for character in s:
            if character in unpaired_characters:
                unpaired_characters.remove(character)
                palindrome_length += 2
            else:
                unpaired_characters.add(character)

        if unpaired_characters:
            palindrome_length += 1

        return palindrome_length
