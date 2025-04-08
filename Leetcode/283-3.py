def moveZeroes(nums: list[int]) -> None:
    zero_count = nums.count(0)
    nums[:] = [num for num in nums if num != 0]
    nums.extend([0] * zero_count)
