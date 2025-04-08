from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        min_prices = [0] * n
        max_profits = [0] * n
        
        min_prices[0] = prices[0]
        for i in range(1, n):
            min_prices[i] = min(min_prices[i - 1], prices[i])
        
        for i in range(1, n):
            max_profits[i] = max(max_profits[i - 1], prices[i] - min_prices[i])
        
        return max_profits[-1]
