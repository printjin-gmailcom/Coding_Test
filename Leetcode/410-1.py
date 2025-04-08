from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        def range_sum(i, j):
            return prefix_sum[j + 1] - prefix_sum[i]
        
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        for j in range(1, k + 1):
            for i in range(j, n + 1):
                for m in range(j - 1, i):
                    dp[i][j] = min(dp[i][j], max(dp[m][j - 1], range_sum(m, i - 1)))
        
        return dp[n][k]
