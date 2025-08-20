def solution(price, money, count):
    total = 0
    for i in range(1, count + 1): 
        total += price * i 
    if total > money:  
        answer = total - money 
    else:
        answer = 0  
    return answer


def solution(arr):
    def compress(x, y, size):
        start = arr[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != start:
                    size //= 2
                    a1 = compress(x, y, size)
                    a2 = compress(x, y + size, size)
                    a3 = compress(x + size, y, size)
                    a4 = compress(x + size, y + size, size)
                    return [a1[0] + a2[0] + a3[0] + a4[0], a1[1] + a2[1] + a3[1] + a4[1]]
        if start == 0:
            return [1, 0]
        else:
            return [0, 1]
    return compress(0, 0, len(arr))


def solution(s):
    def is_valid(brackets):
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for ch in brackets:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        return not stack
    n = len(s)
    count = 0
    for i in range(n):
        rotated = s[i:] + s[:i]
        if is_valid(rotated):
            count += 1
    return count


def solution(n):
    triangle = [[0] * (i + 1) for i in range(n)]
    num = 1
    x, y = -1, 0
    
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:  
                x += 1
            elif i % 3 == 1:  
                y += 1
            else: 
                x -= 1
                y -= 1
            triangle[x][y] = num
            num += 1
    answer = []
    for row in triangle:
        answer.extend(row)
    return answer

