class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0 
        n = len(s)
        left, right = 0, 0
        seen = set()

        if n == 0 or n == 1: 
            return n
        
        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest = max(longest, right - left + 1)
        return longest