from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]
        
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum

# 예제 실행
sol = Solution()
print(sol.maxSubArray([2, -3, 4, -2, 2, 1, -1, 4]))  # 출력: 8
print(sol.maxSubArray([-1]))  # 출력: -1
