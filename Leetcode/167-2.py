def two_sum(numbers, target):
    def binary_search(left, right, value):
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] == value:
                return mid
            elif numbers[mid] < value:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    for i in range(len(numbers)):
        complement = target - numbers[i]
        j = binary_search(i + 1, len(numbers) - 1, complement)
        if j != -1:
            return [i + 1, j + 1] 

numbers = [1, 2, 3, 4]
target = 3
print(two_sum(numbers, target))  
