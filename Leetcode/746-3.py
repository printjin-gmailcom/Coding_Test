class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        def minCost(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = min(minCost(i - 1) + cost[i - 1], minCost(i - 2) + cost[i - 2])
            return memo[i]
        
        memo = {}
        return minCost(len(cost))
