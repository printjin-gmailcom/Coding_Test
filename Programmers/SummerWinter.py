def solution(d, budget):
    d.sort() 
    answer = 0  
    total = 0  
    for cost in d:
        if total + cost > budget: 
            break
        total += cost
        answer += 1
    return answer


def solution(n):
    return bin(n).count('1')


from itertools import combinations
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        addv = sum(i)
        if is_prime(addv):
            answer += 1
    return answer


def solution(n, words):
    word_history = [] 
    for i in range(len(words)):
        if i > 0 and words[i-1][-1] != words[i][0]:
            return [(i % n) + 1, (i // n) + 1] 
        if words[i] in word_history:
            return [(i % n) + 1, (i // n) + 1] 
        word_history.append(words[i])
    return [0, 0] 


def solution(sticker):
    n = len(sticker)
    if n == 1: 
        return sticker[0]
    dp1 = [0] * n
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    for i in range(2, n-1):  
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
    dp2 = [0] * n
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
    return max(dp1[n-2], dp2[n-1])


def solution(dirs):
    x, y = 0, 0
    his = set()
    moves = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
    for d in dirs:
        dx, dy = moves[d]
        nx, ny = x + dx, y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            his.add(((x, y), (nx, ny)))
            his.add(((nx, ny), (x, y)))
            x, y = nx, ny
    return len(his) // 2


def solution(A, B):
    A.sort()
    B.sort()
    i = j = 0
    n = len(A)
    wins = 0
    while i < n and j < n:
        if B[j] > A[i]:
            wins += 1
            i += 1
            j += 1
        else:
            j += 1
    return wins


import math
def solution(w, h):
    return w * h - (w + h - math.gcd(w, h))


def solution(cookie):
    n = len(cookie)
    answer = 0
    for m in range(n - 1):  
        left = m
        right = m + 1
        left_sum = cookie[left]
        right_sum = cookie[right]
        while True:
            if left_sum == right_sum:
                answer = max(answer, left_sum)
            
            if left > 0 and left_sum <= right_sum:
                left -= 1
                left_sum += cookie[left]
            elif right < n - 1 and right_sum <= left_sum:
                right += 1
                right_sum += cookie[right]
            else:
                break    
    return answer


import math
def solution(N, stations, W):
    answer = 0
    cover = 2 * W + 1
    last = 0  
    for s in stations:
        start = s - W 
        if start > last + 1: 
            length = start - (last + 1)
            answer += math.ceil(length / cover)
        last = s + W
    if last < N:  
        length = N - last
        answer += math.ceil(length / cover)
    return answer

