from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev1 = nums[0]
        prev2 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            current = max(prev2, nums[i] + prev1)
            prev1 = prev2
            prev2 = current

        return prev2

solution = Solution()

nums1 = [1, 1, 3, 3]
nums2 = [2, 9, 8, 3, 6]

print(solution.rob(nums1))
print(solution.rob(nums2))
