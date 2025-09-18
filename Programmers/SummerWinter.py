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
