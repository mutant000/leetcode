from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for _ in range(rowIndex):
            row.append(1)

            for index in range(len(row) - 2, 0, -1):
                row[index] += row[index - 1]

        return row
