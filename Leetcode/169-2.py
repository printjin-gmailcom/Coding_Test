def majorityElement(nums: list[int]) -> int:
    nums.sort()
    return nums[len(nums) // 2]
