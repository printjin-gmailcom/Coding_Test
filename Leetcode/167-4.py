def two_sum(numbers, target):
    num_to_index = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement] + 1, i + 1]  # Convert to 1-indexed
        num_to_index[num] = i

numbers = [1, 2, 3, 4]
target = 3
print(two_sum(numbers, target)) 
