from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        repeated = set()

        for index in range(len(s) - 9):
            sequence = s[index:index + 10]
            if sequence in seen:
                repeated.add(sequence)
            else:
                seen.add(sequence)

        return list(repeated)
