from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(max_sum):
            current_sum, count = 0, 1
            for num in nums:
                if current_sum + num > max_sum:
                    count += 1
                    current_sum = num
                    if count > k:
                        return False
                else:
                    current_sum += num
            return True
        
        left, right = max(nums), sum(nums)
        
        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
