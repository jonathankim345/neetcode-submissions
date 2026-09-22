import operator 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        for token in tokens: 
            if token not in operators: 
                stack.append(token)
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                result = operators[token](first, second)
                print(result)
                stack.append(result)
        return int(stack[0])
