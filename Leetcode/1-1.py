def two_sum_hashmap(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i

nums = [3, 4, 5, 6]
target = 7
print(two_sum_hashmap(nums, target)) 
