def solution(people, limit):
    answer = 0
    people.sort()
    i, j = 0, len(people) - 1 
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1  
        answer += 1  
    return answer


def solution(n, lost, reserve):
    real_lost = sorted(set(lost) - set(reserve))
    real_reserve = sorted(set(reserve) - set(lost))
    answer = n - len(real_lost)
    for lo in real_lost:
        if lo - 1 in real_reserve:
            real_reserve.remove(lo - 1)
            answer += 1
        elif lo + 1 in real_reserve:
            real_reserve.remove(lo + 1)
            answer += 1
    return answer


def solution(number, k):
    stack = []
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    return ''.join(stack[:len(number) - k])


