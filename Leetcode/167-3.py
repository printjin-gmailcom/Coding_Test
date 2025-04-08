def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1] 

numbers = [1, 2, 3, 4]
target = 3
print(two_sum(numbers, target))  
