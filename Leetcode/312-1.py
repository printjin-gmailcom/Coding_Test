class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for length in range(1, n - 1):  # Length of subarray being considered
            for i in range(1, n - length):
                j = i + length
                for k in range(i, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k + 1][j] + nums[i - 1] * nums[k] * nums[j])
        
        return dp[1][n - 1]
