class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for n in nums:
            temp = n 
            length = 1
            while n + 1 in nums: 
                length += 1
                n += 1
            longest = max(longest, length)
            n = temp 
        return longest
