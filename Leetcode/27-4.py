class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        filtered_nums = list(filter(lambda x: x != val, nums))
        nums[:len(filtered_nums)] = filtered_nums
        return len(filtered_nums)
