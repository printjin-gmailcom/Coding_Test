from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def max_crossing_sum(nums, left, mid, right):
            left_sum = float('-inf')
            total = 0
            for i in range(mid, left - 1, -1):
                total += nums[i]
                if total > left_sum:
                    left_sum = total
                    
            right_sum = float('-inf')
            total = 0
            for i in range(mid + 1, right + 1):
                total += nums[i]
                if total > right_sum:
                    right_sum = total
                    
            return left_sum + right_sum

        def max_subarray_divide_and_conquer(nums, left, right):
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            
            left_sum = max_subarray_divide_and_conquer(nums, left, mid)
            right_sum = max_subarray_divide_and_conquer(nums, mid + 1, right)
            cross_sum = max_crossing_sum(nums, left, mid, right)
            
            return max(left_sum, right_sum, cross_sum)

        return max_subarray_divide_and_conquer(nums, 0, len(nums) - 1)

# 예제 실행
sol = Solution()
print(sol.maxSubArray([2, -3, 4, -2, 2, 1, -1, 4]))  # 출력: 8
print(sol.maxSubArray([-1]))  # 출력: -1
