from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Need to return a list of lists? So have to make it into a list format
        # Hashmap where key is count and value is list
        hashmap = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in range(len(s)):
                count[ord(s[c]) - ord('a')] += 1
            hashmap[tuple(count)].append(s)
        return list(hashmap.values())
            