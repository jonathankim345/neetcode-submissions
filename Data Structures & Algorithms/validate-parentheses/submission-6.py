class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openers = {'(': ')', '{': '}', '[': ']'}
        for char in s: 
            if char in openers: 
                stack.append(char)
            else: 
                if len(stack) == 0 or char != openers[stack.pop()]: 
                    return False
        return len(stack) == 0