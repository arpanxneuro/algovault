class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping.values():
                stack.append(char)
            else:
                if not stack or stack[-1] != mapping.get(char):
                    return False
                else:
                    stack.pop()

        return len(stack) == 0
