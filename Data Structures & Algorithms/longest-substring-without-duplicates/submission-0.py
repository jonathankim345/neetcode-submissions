class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0 
        left, right = 0, 1
        n = len(s)
        seen = set()
        if s == "":
            return 0
        if n == 0 or n == 1: 
            return 1
        while right < n:
            seen.clear()
            seen.add(s[left])
            right = left + 1
            length = 1
            while right < n and s[right] not in seen: 
                seen.add(s[right])
                length += 1
                right += 1
            left += 1
            longest = max(longest, length)
        return longest