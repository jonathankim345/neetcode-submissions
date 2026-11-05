class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Want to push two values in to the stack
        # Indices? 
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                res[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i, t))
        return res
        # Possibly go back 
        # (30, 0), (38,1), (30, 2), (36, 3), (35, 4)