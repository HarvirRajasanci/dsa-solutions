class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {')' : '(', ']' : '[', '}' : '{'}
        stack = []

        for c in s:
            if c not in openToClose:
                stack.append(c)
            else:
                if stack and stack[-1] == openToClose.get(c):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

