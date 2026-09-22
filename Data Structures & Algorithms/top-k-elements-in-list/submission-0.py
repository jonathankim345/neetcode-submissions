class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for _ in range(len(nums))]
        res = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for key in freq:
            bucket[freq[key] - 1].append(key)
        for arr in bucket[::-1]:
            for num in arr: 
                res.append(num)
        return res[:k]
            