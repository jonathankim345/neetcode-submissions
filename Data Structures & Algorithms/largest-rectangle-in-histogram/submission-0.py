class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maximum = 0
        N = len(heights)
        stack = []
        for i in range(N): 
            idx = i
            while stack and stack[-1][1] > heights[i]:
                idx, height = stack.pop()
                area = height * (i - idx)
                maximum = max(maximum, area)
            stack.append((idx, heights[i]))
        
        for i, h in stack:
            maximum = max(maximum, h * (len(heights)- i) )

        return maximum