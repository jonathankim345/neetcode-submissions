class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        result = [0] * len(temperatures)
        for i in range(len(temperatures)): 
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                popped = stack.pop()
                result[popped] = i - popped
            stack.append(i)
        return result