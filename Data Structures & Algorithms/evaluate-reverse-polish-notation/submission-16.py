class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []
        for t in tokens:
            if len(stack) < 2 or t not in operators:
                stack.append(t)
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                if t == '+':
                    first += second
                elif t == '-':
                    first -= second
                elif t == '*':
                    first *= second
                else:
                    first = int(first / second)
                stack.append(first)
        return int(stack[-1])