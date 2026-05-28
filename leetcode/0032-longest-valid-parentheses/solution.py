class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        best = 0

        for index, char in enumerate(s):
            if char == "(":
                stack.append(index)
            else:
                stack.pop()

                if not stack:
                    stack.append(index)
                else:
                    best = max(best, index - stack[-1])

        return best
