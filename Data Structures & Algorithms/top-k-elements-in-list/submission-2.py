class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        buckets = [[] for _ in range(len(nums) + 1)] 
        res = []
        for n in nums: 
            hashmap[n] = hashmap.get(n, 0) + 1
        for item, frequency in hashmap.items():
            buckets[frequency].append(item)
        for freq in buckets[::-1]:
            for n in freq: 
                res.append(n)
                k -= 1
                if k == 0: 
                    return res