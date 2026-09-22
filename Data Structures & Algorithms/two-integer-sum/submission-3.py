class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i, x in enumerate(nums):
            if target - x in values: 
                return [values[target - x], i]
            values[x] = i