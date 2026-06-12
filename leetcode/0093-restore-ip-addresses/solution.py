from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        path = []

        def valid(segment: str) -> bool:
            if len(segment) > 1 and segment[0] == "0":
                return False
            return int(segment) <= 255

        def backtrack(index: int) -> None:
            if len(path) == 4:
                if index == len(s):
                    result.append(".".join(path))
                return

            remaining_parts = 4 - len(path)
            remaining_chars = len(s) - index
            if remaining_chars < remaining_parts or remaining_chars > remaining_parts * 3:
                return

            for length in range(1, 4):
                if index + length > len(s):
                    break

                segment = s[index : index + length]
                if valid(segment):
                    path.append(segment)
                    backtrack(index + length)
                    path.pop()

        backtrack(0)
        return result
