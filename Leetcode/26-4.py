class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique_nums = []
        for num in nums:
            if len(unique_nums) == 0 or unique_nums[-1] != num:
                unique_nums.append(num)
        nums[:len(unique_nums)] = unique_nums
        return len(unique_nums)
