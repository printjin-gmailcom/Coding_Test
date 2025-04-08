def two_sum_set(nums, target):
    seen = set()
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [nums.index(complement), i]
        seen.add(num)

nums = [3, 4, 5, 6]
target = 7
print(two_sum_set(nums, target))  