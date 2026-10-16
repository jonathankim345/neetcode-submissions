class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = 1, 1
        nums_length = len(nums)
        res = [1] * nums_length
        postfix_arr = [1] * nums_length
        for i in range(1, nums_length):
            res[i] = nums[i - 1] * prefix
            prefix = res[i]
        for j in range(nums_length - 2, -1, -1):
            postfix_arr[j] = nums[j + 1] * postfix
            postfix = postfix_arr[j]
        for k in range(nums_length):
            res[k] = res[k] * postfix_arr[k]
        return res