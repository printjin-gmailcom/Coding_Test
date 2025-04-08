from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        
        return max(dp)

# 예제 실행
sol = Solution()
print(sol.maxSubArray([2, -3, 4, -2, 2, 1, -1, 4]))  # 출력: 8
print(sol.maxSubArray([-1]))  # 출력: -1
