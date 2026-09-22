class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openers = {'(': ')', '{': '}', '[': ']'}
        for char in s: 
            if char in openers: 
                stack.append(char)
            else: 
                if len(stack) == 0: 
                    return False
                popped = stack.pop()
                if char != openers[popped]:
                    return False
        return len(stack) == 0