def findDisappearedNumbers(nums: list[int]) -> list[int]:
    missing_nums = []
    bitmask = 0
    for num in nums:
        bitmask |= 1 << num
    
    for i in range(1, len(nums) + 1):
        if not bitmask & (1 << i):
            missing_nums.append(i)
    
    return missing_nums
