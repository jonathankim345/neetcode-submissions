class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs: 
            array = [0]*26
            for c in s:
                array[ord(c) - ord('a')] += 1
            array = tuple(array)
            if array in seen: 
                seen[array].append(s)
            else:
                seen[array] = [s]
        return list(seen.values())