class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current = []
        repeat = 0

        for char in s:
            if char.isdigit():
                repeat = repeat * 10 + int(char)
            elif char == "[":
                stack.append((current, repeat))
                current = []
                repeat = 0
            elif char == "]":
                previous, count = stack.pop()
                current = previous + current * count
            else:
                current.append(char)

        return "".join(current)
