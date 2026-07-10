from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        continuation_bytes = 0

        for byte in data:
            if continuation_bytes > 0:
                if byte >> 6 != 0b10:
                    return False
                continuation_bytes -= 1
                continue

            if byte >> 7 == 0:
                continue
            if byte >> 5 == 0b110:
                continuation_bytes = 1
            elif byte >> 4 == 0b1110:
                continuation_bytes = 2
            elif byte >> 3 == 0b11110:
                continuation_bytes = 3
            else:
                return False

        return continuation_bytes == 0
