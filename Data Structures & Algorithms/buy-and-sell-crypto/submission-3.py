class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        min_buy = prices[0]
        profit = prices[1] - min_buy
        for i in range(1, n):
            min_buy = min(min_buy, prices[i])
            profit = max(profit, prices[i] - min_buy)
        return profit