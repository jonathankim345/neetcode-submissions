class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = 1, 1
        nums_length = len(nums)
        res = [1] * nums_length
        for i in range(nums_length):
            res[i] = prefix
            prefix *= nums[i]
        for j in range(nums_length - 1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
        return res