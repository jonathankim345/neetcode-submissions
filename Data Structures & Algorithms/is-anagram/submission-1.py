class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for char in range(len(s)): 
            s_dict[s[char]] = s_dict.get(s[char], 0) + 1
            t_dict[t[char]] = t_dict.get(t[char], 0) + 1
        return s_dict == t_dict