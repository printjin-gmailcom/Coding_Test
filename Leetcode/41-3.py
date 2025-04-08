class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_map = {}
        smallest = 1
        
        for num in nums:
            if 1 <= num <= len(nums):
                num_map[num] = True
        
        while smallest in num_map:
            smallest += 1
        
        return smallest
