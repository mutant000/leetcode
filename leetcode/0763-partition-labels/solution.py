from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_positions = {character: index for index, character in enumerate(s)}
        result = []
        start = 0
        end = 0

        for index, character in enumerate(s):
            end = max(end, last_positions[character])

            if index == end:
                result.append(end - start + 1)
                start = index + 1

        return result
