class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        # prefix_arr = [1] * n
        # postfix_arr = [1] * n
        prefix = 1
        postfix = 1
        for i in range(1, n):
            prefix *= nums[i - 1]
            res[i] = prefix
        for j in range(n - 2, -1, -1):
            postfix *= nums[j + 1]
            res[j] *= postfix
        return res