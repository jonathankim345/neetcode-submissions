class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []
        for t in tokens:
            if len(stack) < 2 or t not in operators:
                stack.append(int(t))
            else:
                second = stack.pop()
                first = stack.pop()
                if t == '+':
                    first += second
                elif t == '-':
                    first -= second
                elif t == '*':
                    first *= second
                else:
                    first = int(first / second)
                stack.append(first)
        return stack[-1]