def solution(n, times):
    left, right = 1, max(times) * n
    answer = right
    while left <= right:
        mid = (left + right) // 2
        total = sum(mid // t for t in times)  
        if total >= n:  
            answer = mid
            right = mid - 1 
        else:
            left = mid + 1  
    return answer


def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 1, distance
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        removed = 0
        prev = 0
        for rock in rocks:
            if rock - prev < mid:
                removed += 1
            else:
                prev = rock
        if removed <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer
