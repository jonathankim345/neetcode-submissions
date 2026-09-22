class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            if len(s) < len(prefix):
                prefix = prefix[0:len(s)]
            for char in range(len(s)):
                if char >= len(prefix) or s[char] != prefix[char]:
                    prefix = prefix[0:char]
                    break
        return prefix