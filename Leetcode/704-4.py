def search(nums: list[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
