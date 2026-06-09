class Solution:
    def countAndSay(self, n: int) -> str:
        current = "1"

        for _ in range(n - 1):
            pieces = []
            index = 0

            while index < len(current):
                start = index

                while index < len(current) and current[index] == current[start]:
                    index += 1

                pieces.append(str(index - start))
                pieces.append(current[start])

            current = "".join(pieces)

        return current
