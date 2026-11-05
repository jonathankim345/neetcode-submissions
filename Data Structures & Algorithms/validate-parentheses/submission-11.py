class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s: 
            if char not in mapping:
                stack.append(char)
            if char in mapping:
                if stack:
                    end = stack.pop()
                    if mapping[char] != end:
                        return False
                else:
                    return False
        return True if not stack else False