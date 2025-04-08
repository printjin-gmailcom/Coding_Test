from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_from(i, memo):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]

            rob_this = nums[i] + rob_from(i + 2, memo)
            skip_this = rob_from(i + 1, memo)

            result = max(rob_this, skip_this)
            memo[i] = result
            return result

        return rob_from(0, {})

sol = Solution()

nums1 = [1, 1, 3, 3]
nums2 = [2, 9, 8, 3, 6]

print(sol.rob(nums1))  
print(sol.rob(nums2))  
