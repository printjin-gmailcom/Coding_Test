def containsDuplicate(nums: list[int]) -> bool:
    for i in range(len(nums)):
        if nums[i] in nums[i+1:]:
            return True
    return False
