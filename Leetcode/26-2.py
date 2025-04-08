class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique_nums = sorted(set(nums))
        nums[:len(unique_nums)] = unique_nums
        return len(unique_nums)
