class Solution:
    def deserialize(self, s: str) -> 'NestedInteger':
        if s[0] != "[":
            return NestedInteger(int(s))

        stack = []
        number_start = 0

        for i, char in enumerate(s):
            if char == "[":
                stack.append(NestedInteger())
                number_start = i + 1
            elif char in ",]":
                if i > number_start:
                    stack[-1].add(NestedInteger(int(s[number_start:i])))
                number_start = i + 1
                if char == "]" and len(stack) > 1:
                    current = stack.pop()
                    stack[-1].add(current)

        return stack[-1]
