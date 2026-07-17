from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        possible_times = []

        for hour in range(12):
            for minute in range(60):
                if hour.bit_count() + minute.bit_count() == turnedOn:
                    possible_times.append(f"{hour}:{minute:02d}")

        return possible_times
