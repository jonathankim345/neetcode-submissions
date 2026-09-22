class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        # Mapping numbers to frequencies 
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        # Mapping to buckets
        for key, value in freq.items():
            buckets[value].append(key)
        # Append to the result
        res = []
        for b in buckets[::-1]:
            for elem in b: 
                res.append(elem)
                if len(res) == k:
                    return res