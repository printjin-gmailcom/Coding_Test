def moveZeroes(nums: list[int]) -> None:
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            if i != j:
                nums[i] = 0
            j += 1
