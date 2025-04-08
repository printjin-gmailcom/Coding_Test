def pivotIndex(nums: list[int]) -> int:
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:]):
            return i
    return -1
