from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0

        while read < len(chars):
            group_end = read

            while (
                group_end < len(chars)
                and chars[group_end] == chars[read]
            ):
                group_end += 1

            chars[write] = chars[read]
            write += 1
            count = group_end - read

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

            read = group_end

        return write
