def pivotIndex(nums: list[int]) -> int:
    left_sum, right_sum = 0, sum(nums)
    
    for i, num in enumerate(nums):
        right_sum -= num
        if left_sum == right_sum:
            return i
        left_sum += num
    
    return -1
