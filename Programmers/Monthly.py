def solution(n, m, x, y, queries):
    min_row, max_row = x, x
    min_col, max_col = y, y
    for command, dx in reversed(queries):
        if command == 0: 
            max_col = min(m - 1, max_col + dx)
            if min_col != 0:
                min_col += dx
        elif command == 1:  
            min_col = max(0, min_col - dx)
            if max_col != m - 1:
                max_col -= dx
        elif command == 2:  
            max_row = min(n - 1, max_row + dx)
            if min_row != 0:
                min_row += dx
        elif command == 3:  
            min_row = max(0, min_row - dx)
            if max_row != n - 1:
                max_row -= dx
        if min_row >= n or max_row < 0 or min_col >= m or max_col < 0:
            return 0
    return (max_row - min_row + 1) * (max_col - min_col + 1)


def solution(n, left, right):
    result = []
    for idx in range(left, right + 1):
        row = idx // n
        col = idx % n
        result.append(max(row, col) + 1)
    return result


def solution(absolutes, signs):
    return sum(absolutes[i] if signs[i] else -absolutes[i] for i in range(len(absolutes)))


def solution(numbers):
    all_numbers = set(range(10))
    missing_numbers = all_numbers - set(numbers)
    return sum(missing_numbers)


def solution(n):
    answer = 0
    for i in range(1, n):
        if n % i == 1:
            answer = i
            break
    return answer


def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += int(a[i]*b[i])
    return answer


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        ans = 0
        for j in range(1, i + 1): 
            if i % j == 0: 
                ans += 1  
        if ans % 2 == 0: 
            answer += i 
        else:
            answer -= i
    return answer


def solution(s):
    count = 0 
    zero = 0 
    while s != "1": 
        zero += s.count('0') 
        s = s.replace('0', '') 
        s = bin(len(s))[2:] 
        count += 1  
    return [count, zero]  


def solution(n):
    ternary = ""
    while n > 0:
        n, r = divmod(n, 3) 
        ternary += str(r)    
    return int(ternary, 3) 


from itertools import combinations
def solution(numbers):
    answer = set()  
    for a, b in combinations(numbers, 2):
        answer.add(a + b)
    return sorted(answer)


def solution(numbers): 
    return [((num ^ (num+1)) >> 2) + num + 1 for num in numbers]
