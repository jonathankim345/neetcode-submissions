class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        prefix[0] = prefix_max = height[0] 
        for i in range(1, len(height)):
            prefix[i] = max(height[i], prefix_max)
            prefix_max = max(height[i], prefix_max)
        suffix[-1] = suffix_max = height[-1]
        for i in range(len(height) - 2, -1, -1):
            suffix[i] = max(height[i], suffix_max)
            suffix_max = max(height[i], suffix_max)
        total_water = 0
        for i in range(len(height)):
            water = min(prefix[i], suffix[i]) - height[i]
            total_water += water
        return total_water
