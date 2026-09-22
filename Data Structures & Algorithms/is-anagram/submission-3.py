class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        if len_s != len_t: 
            return False
        s_map, t_map = {}, {}
        for i in range(len_s):
            s_map[s[i]] = s_map.get(s[i], 0) + 1
            t_map[t[i]] = t_map.get(t[i], 0) + 1
        return s_map == t_map