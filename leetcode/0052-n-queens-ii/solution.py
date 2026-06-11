class Solution:
    def totalNQueens(self, n: int) -> int:
        full_mask = (1 << n) - 1

        def backtrack(columns: int, diagonals: int, anti_diagonals: int) -> int:
            if columns == full_mask:
                return 1

            count = 0
            available = full_mask & ~(columns | diagonals | anti_diagonals)

            while available:
                position = available & -available
                available -= position
                count += backtrack(
                    columns | position,
                    (diagonals | position) << 1,
                    (anti_diagonals | position) >> 1,
                )

            return count

        return backtrack(0, 0, 0)
