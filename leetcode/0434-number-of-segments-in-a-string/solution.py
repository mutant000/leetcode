class Solution:
    def countSegments(self, s: str) -> int:
        segments = 0

        for index, char in enumerate(s):
            if char != " " and (index == 0 or s[index - 1] == " "):
                segments += 1

        return segments
