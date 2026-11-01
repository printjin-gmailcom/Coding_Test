T = int(input())
for test_case in range(1, T + 1):
    n = input()
    if "9" in n:
        print(f"#{test_case} Yes")
    else:
        print(f"#{test_case} No")


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    total = 0
    for _ in range(N):
        L, R = map(int, input().split())
        total += R - L + 1
    print(f"#{test_case} {total}")
  

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    s = set()
    for _ in range(n):
        x = int(input())
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    print(f"#{tc} {len(s)}")


from itertools import permutations
INF = 10 ** 18
T = int(input())
for tc in range(1, T + 1):
    N, M, R = map(int, input().split())
    towns = list(map(int, input().split()))
    dist = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        dist[i][i] = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        if c < dist[a][b]:
            dist[a][b] = c
            dist[b][a] = c
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    ans = INF
    for order in permutations(towns):
        total = 0
        for i in range(R - 1):
            total += dist[order[i]][order[i + 1]]
        ans = min(ans, total)
    print(f"#{tc} {ans}")



import sys
import heapq
input = sys.stdin.readline
def simulate(a, b, turn):
    a = a[:]
    b = b[:]
    heapq.heapify(a)
    heapq.heapify(b)
    while a and b:
        if turn == 0:
            if -a[0] > -b[0]:
                heapq.heappop(b)
                if not b:
                    return 0
            elif len(a) >= 2:
                x = heapq.heappop(a)
                y = heapq.heappop(a)
                heapq.heappush(a, x + y)
            turn = 1
        else:
            if -b[0] > -a[0]:
                heapq.heappop(a)
                if not a:
                    return 1
            elif len(b) >= 2:
                x = heapq.heappop(b)
                y = heapq.heappop(b)
                heapq.heappush(b, x + y)
            turn = 0
    return 0 if a else 1
def solve(a, b):
    a = [-x for x in a]
    b = [-x for x in b]
    heapq.heapify(a)
    heapq.heapify(b)
    if -a[0] > -b[0]:
        na = a[:]
        nb = b[:]
        heapq.heappop(nb)
        if not nb:
            return 0
        if simulate(na, nb, 1) == 0:
            return 0
    if len(a) >= 2:
        na = a[:]
        nb = b[:]
        x = heapq.heappop(na)
        y = heapq.heappop(na)
        heapq.heappush(na, x + y)
        if simulate(na, nb, 1) == 0:
            return 0
    if -a[0] <= -b[0] and len(a) < 2:
        return simulate(a, b, 1)
    return 1
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = solve(a, b)
    if result == 0:
        print(f"#{tc} Takeover Incorporated")
    else:
        print(f"#{tc} Buyout Limited")


import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    stacks = []
    all_plates = []
    for _ in range(N):
        data = list(map(int, input().split()))
        h = data[0]
        plates = data[1:1 + h]
        stacks.append(plates)
        all_plates.extend(plates)
    all_plates.sort()
    K = N
    for plates in stacks:
        for i in range(len(plates) - 1):
            a = plates[i]
            b = plates[i + 1]
            left = bisect_right(all_plates, a)
            right = bisect_left(all_plates, b)
            if left < right:
                K += 1
    answer = 2 * K - N - 1
    print(f"#{tc} {answer}")


