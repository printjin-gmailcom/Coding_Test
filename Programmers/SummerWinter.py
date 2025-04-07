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