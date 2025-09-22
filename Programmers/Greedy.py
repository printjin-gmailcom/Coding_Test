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


def solution(n, costs):
    costs.sort(key=lambda x: x[2]) 
    connected = set([0])  
    total = 0
    while len(connected) < n:
        for a, b, c in costs:
            if a in connected and b not in connected:
                connected.add(b)
                total += c
                break
            elif b in connected and a not in connected:
                connected.add(a)
                total += c
                break
    return total


def solution(routes):
    routes.sort(key=lambda x: x[1]) 
    cameras = []
    count = 0
    for route in routes:
        if not cameras or cameras[-1] < route[0]:  
            cameras.append(route[1])  
            count += 1
    return count


