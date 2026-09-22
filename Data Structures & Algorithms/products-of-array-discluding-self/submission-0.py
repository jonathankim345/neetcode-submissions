class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix_arr = [1] * n
        postfix_arr = [1] * n
        prefix = 1
        postfix = 1
        for i in range(1, n):
            prefix *= nums[i - 1]
            prefix_arr[i] = prefix
        for j in range(n - 2, -1, -1):
            postfix *= nums[j + 1]
            postfix_arr[j] = postfix
        for k in range(n):
            res[k] = prefix_arr[k] * postfix_arr[k]
        return res