def containsDuplicate(nums: list[int]) -> bool:
    nums.sort()
    left, right = 0, 1
    while right < len(nums):
        if nums[left] == nums[right]:
            return True
        left += 1
        right += 1
    return False
