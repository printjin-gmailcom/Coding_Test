def solution(arr):
    result = []
    for num in arr:
        if not result or result[-1] != num:
            result.append(num)
    return result


def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                return False
    return len(stack) == 0


def solution(prices):
    n = len(prices)
    result = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            result[i] += 1
            if prices[i] > prices[j]:
                break
    return result


import math

def solution(progresses, speeds):
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    result = []
    current_deploy_day = days[0]
    count = 0
    for day in days:
        if day <= current_deploy_day:
            count += 1
        else:
            result.append(count)
            count = 1
            current_deploy_day = day
    result.append(count)
    return result