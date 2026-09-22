class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0 
        n = len(prices)
        if n == 1: 
            return max_profit 
        while right < n:
            if prices[left] <= prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
                right += 1
            else:
                left = right
        return max_profit