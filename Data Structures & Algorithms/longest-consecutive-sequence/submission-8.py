class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 
        seen = set(nums) 
        for num in seen:
            if num - 1 not in seen:
                length = 1
                while (num + 1) in seen:
                    length += 1
                    num += 1
                longest = max(length, longest)
        return longest
