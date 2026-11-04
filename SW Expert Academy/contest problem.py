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


import sys
import math
import heapq
data = iter(map(int, sys.stdin.buffer.read().split()))
T = next(data)
PI = math.pi
EARTH = 6370.0
EPS = 1e-9
def dot(a, b):
    return sum(x * y for x, y in zip(a, b))
def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    )
def norm(a):
    return math.sqrt(dot(a, a))
def unit(a):
    l = norm(a)
    return tuple(x / l for x in a)
def add(a, b):
    return tuple(x + y for x, y in zip(a, b))
def scale(a, s):
    return tuple(x * s for x in a)
def get_point(lon, lat):
    lon = math.radians(lon)
    lat = math.radians(lat)
    return (
        math.cos(lat) * math.cos(lon),
        math.cos(lat) * math.sin(lon),
        math.sin(lat)
    )
def intersections(a, b, k):
    d = dot(a, b)
    if d < -1 + EPS:
        return []
    v = scale(add(a, b), k / (1 + d))
    h2 = 1 - dot(v, v)
    if h2 < -EPS:
        return []
    h = math.sqrt(max(0.0, h2))
    n = cross(a, b)
    nl = norm(n)
    if nl < EPS:
        return []
    n = scale(n, 1 / nl)
    if h < EPS:
        return [v]
    return [
        add(v, scale(n, h)),
        add(v, scale(n, -h))
    ]
def covered(p, q, airports, alpha):
    d = max(-1.0, min(1.0, dot(p, q)))
    L = math.acos(d)
    if L < EPS:
        return True
    s = math.sin(L)
    if abs(s) < EPS:
        axis = (1.0, 0.0, 0.0)
        if abs(p[0]) > 0.9:
            axis = (0.0, 1.0, 0.0)
        u = unit(cross(p, axis))
    else:
        u = scale(add(q, scale(p, -d)), 1 / s)
    intervals = []
    k = math.cos(alpha)
    for a in airports:
        A = dot(a, p)
        B = dot(a, u)
        rho = math.hypot(A, B)
        if rho < EPS or rho < k - EPS:
            continue
        ratio = max(-1.0, min(1.0, k / rho))
        gamma = math.acos(ratio)
        phase = math.atan2(B, A)
        for z in (-1, 0, 1):
            left = max(0.0, phase - gamma + 2 * PI * z)
            right = min(L, phase + gamma + 2 * PI * z)
            if left <= right + EPS:
                intervals.append((left, right))
    intervals.sort()
    reach = 0.0
    for left, right in intervals:
        if left > reach + EPS:
            return False
        reach = max(reach, right)

        if reach >= L - EPS:
            return True
    return False
def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0.0
    pq = [(0.0, start)]
    while pq:
        cost, u = heapq.heappop(pq)
        if cost > dist[u] + EPS:
            continue
        for v, w in graph[u]:
            nd = cost + w
            if nd < dist[v] - EPS:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
results = []
for case in range(1, T + 1):
    N = next(data)
    R = next(data)
    airports = [
        get_point(next(data), next(data))
        for _ in range(N)
    ]
    alpha = R / EARTH
    k = math.cos(alpha)
    points = list(airports)
    for i in range(N):
        for j in range(i + 1, N):
            points.extend(intersections(airports[i], airports[j], k))
    V = len(points)
    graph = [[] for _ in range(V)]
    for i in range(V):
        for j in range(i + 1, V):
            if covered(points[i], points[j], airports, alpha):
                angle = math.acos(
                    max(-1.0, min(1.0, dot(points[i], points[j])))
                )
                dist = angle * EARTH
                graph[i].append((j, dist))
                graph[j].append((i, dist))
    airport_dist = []
    for i in range(N):
        d = dijkstra(graph, i)
        airport_dist.append(d[:N])
    Q = next(data)
    results.append(f"Case {case}:")
    for _ in range(Q):
        s = next(data) - 1
        t = next(data) - 1
        c = next(data)
        pq = [(0.0, s)]
        dist = [float('inf')] * N
        dist[s] = 0.0
        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u] + EPS:
                continue
            if u == t:
                break
            for v in range(N):
                w = airport_dist[u][v]
                if w <= c + EPS and cost + w < dist[v] - EPS:
                    dist[v] = cost + w
                    heapq.heappush(pq, (dist[v], v))
        if math.isinf(dist[t]):
            results.append("impossible")
        else:
            results.append(f"{dist[t]:.3f}")
print("\n".join(results))


import sys
import math
input = sys.stdin.readline
T = int(input())
for tc in range(1, T + 1):
    N, px, py = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    ans = float('inf')
    for s in range(N):
        route = [(px, py)]
        for i in range(N):
            route.append(points[(s + i) % N])
        route.append((px, py))
        dist = 0
        for i in range(len(route) - 1):
            x1, y1 = route[i]
            x2, y2 = route[i + 1]
            dist += math.hypot(x2 - x1, y2 - y1)
        ans = min(ans, dist)
    print(f"#{tc} {ans:.2f}")


