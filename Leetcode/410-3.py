from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def valid(mid):
            total, count = 0, 1
            for num in nums:
                if total + num > mid:
                    count += 1
                    total = num
                    if count > k:
                        return False
                else:
                    total += num
            return True
        
        left, right = max(nums), sum(nums)
        
        while left < right:
            mid = (left + right) // 2
            if valid(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
