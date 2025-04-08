def two_sum_two_pointers(nums, target):
    nums_with_index = [(num, i) for i, num in enumerate(nums)]
    nums_with_index.sort()
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums_with_index[left][0] + nums_with_index[right][0]
        if current_sum == target:
            return sorted([nums_with_index[left][1], nums_with_index[right][1]])
        elif current_sum < target:
            left += 1
        else:
            right -= 1

# Example usage:
nums = [3, 4, 5, 6]
target = 7
print(two_sum_two_pointers(nums, target))  # Output: [0, 1]
