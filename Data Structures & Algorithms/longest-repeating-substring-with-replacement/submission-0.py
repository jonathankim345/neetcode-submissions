class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        longest = 0 
        charMap = {}
        for r in range(len(s)):
            charMap[s[r]] = charMap.get(s[r], 0) + 1 
            
            most_frequent = max(charMap.values())

            replacements = (r - l + 1) - most_frequent

            if replacements > k: 
                charMap[s[l]] -= 1 
                l += 1
            else: 
                longest = max(longest, r - l + 1)
        return longest