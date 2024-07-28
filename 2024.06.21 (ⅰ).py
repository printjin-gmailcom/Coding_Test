def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_recursive(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

def is_palindrome(s):
    cleaned_s = ''.join(e for e in s if e.isalnum()).lower()
    return cleaned_s == cleaned_s[::-1]


def find_max(arr):
    if not arr:
        raise ValueError("The list is empty")
    max_value = arr[0]
    for num in arr[1:]:
        if num > max_value:
            max_value = num
    return max_value

def find_max(nums):
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value
def process_storage(storage, num):
    clean_storage = []
    clean_num = []
    for i in range(len(storage)):
        if storage[i] in clean_storage:
            pos = clean_storage.index(storage[i])
            clean_num[pos] += num[i]
        else:
            clean_storage.append(storage[i])
            clean_num.append(num[i])
     max_num

import math
def coordinates(r1, r2):
    answer = 0
    for x in range(-r2, r2+1):
        max_y_r2 = math.floor(math.sqrt(r2**2 - x**2))
        min_y_r1 = math.ceil(math.sqrt(r1**2 - x**2)) if x**2 < r1**2 else 0
        answer += (max_y_r2 - min_y_r1 + 1) * 2
        if min_y_r1 == 0:
            answer -= 1
    return answer

## def 

def count(order):
    prices = {
        "iceamericano": 4500,
        "americano": 4500,
        "icecafelatte": 5000,
        "cafelatteice": 5000,
        "hotcafelatte": 5000,
        "cafelattehot": 5000,
        "cafelatte": 5000,
        "anything": 4500
    }
    answer = 0
    for item in order:
        answer += prices[item]
    return answer
