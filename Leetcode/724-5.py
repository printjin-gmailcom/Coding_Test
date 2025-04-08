def pivotIndex(nums: list[int]) -> int:
    total_sum = sum(nums)
    for i, num in enumerate(nums):
        if 2 * sum(nums[:i]) + num == total_sum:
            return i
    return -1
