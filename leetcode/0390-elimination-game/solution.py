class Solution:
    def lastRemaining(self, n: int) -> int:
        first_remaining = 1
        step = 1
        remaining_count = n
        removing_from_left = True

        while remaining_count > 1:
            if removing_from_left or remaining_count % 2 == 1:
                first_remaining += step

            remaining_count //= 2
            step *= 2
            removing_from_left = not removing_from_left

        return first_remaining
