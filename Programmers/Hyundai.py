MOD = 1_000_000_007
def mat_mult(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        Ci = C[i]
        for k in range(n):
            aik = Ai[k]
            if aik:
                Bk = B[k]
                for j in range(n):
                    Ci[j] = (Ci[j] + aik * Bk[j]) % MOD
    return C
def mat_pow(A, exp):
    n = len(A)
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        res[i][i] = 1
    base = A
    while exp > 0:
        if exp & 1:
            res = mat_mult(res, base)
        base = mat_mult(base, base)
        exp >>= 1
    return res
def solution(grid, d, k):
    n_rows = len(grid)
    n_cols = len(grid[0])
    N = n_rows * n_cols
    L = len(d)
    def idx(r, c): return r * n_cols + c
    B_list = []
    for p in range(L):
        B_list.append([[0]*N for _ in range(N)])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for r in range(n_rows):
        for c in range(n_cols):
            u = idx(r,c)
            h_u = grid[r][c]
            for dr,dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n_rows and 0 <= nc < n_cols:
                    v = idx(nr,nc)
                    slope = grid[nr][nc] - h_u
                    for p in range(L):
                        if d[p] == slope:
                            B_list[p][u][v] = (B_list[p][u][v] + 1) % MOD
    if L == 0:
        return 0
    A = B_list[0]
    for p in range(1, L):
        A = mat_mult(A, B_list[p])
    A_k = mat_pow(A, k)
    total = 0
    Nrange = range(N)
    for i in Nrange:
        row = A_k[i]
        s = sum(row) % MOD
        total = (total + s) % MOD
    return total


from itertools import combinations_with_replacement, combinations, product
import heapq
def wait_time_for_type(requests, m):
    if not requests:
        return 0
    heap = [0]*m
    heapq.heapify(heap)
    total_wait = 0
    for a, b in requests:
        earliest = heapq.heappop(heap)
        if earliest <= a:
            start = a
            wait = 0
        else:
            start = earliest
            wait = earliest - a
        finish = start + b
        heapq.heappush(heap, finish)
        total_wait += wait
    return total_wait
def solution(k, n, reqs):
    types = [[] for _ in range(k+1)]
    for a,b,c in reqs:
        types[c].append((a,b))
    min_total = float('inf')
    comp = []
    def dfs(idx, remaining):
        nonlocal min_total
        if idx == k:
            if remaining == 0:
                total = 0
                for i in range(1, k+1):
                    total += wait_time_for_type(types[i], comp[i-1])
                    if total >= min_total:
                        break
                if total < min_total:
                    min_total = total
            return
        for x in range(1, remaining - (k - idx - 1) + 1):
            comp.append(x)
            dfs(idx+1, remaining-x)
            comp.pop()
    dfs(0, n)
    return min_total


def solution(temperature, t1, t2, a, b, onboard):
    INF = 10**15
    TMIN, TMAX = -10, 40
    N = len(onboard)
    dp = [[INF] * 51 for _ in range(N)]
    dp[0][temperature - TMIN] = 0
    for i in range(1, N):
        for temp in range(TMIN, TMAX + 1):
            prev = dp[i - 1][temp - TMIN]
            if prev == INF:
                continue
            if temp < temperature:
                nt = temp + 1
            elif temp > temperature:
                nt = temp - 1
            else:
                nt = temp
            if not onboard[i] or (t1 <= nt <= t2):
                dp[i][nt - TMIN] = min(dp[i][nt - TMIN], prev)
            for target in range(t1, t2 + 1):
                cost = b if temp == target else a
                if temp < target:
                    nt = temp + 1
                elif temp > target:
                    nt = temp - 1
                else:
                    nt = temp
                if not onboard[i] or (t1 <= nt <= t2):
                    dp[i][nt - TMIN] = min(dp[i][nt - TMIN],prev + cost)
    answer = INF
    for temp in range(TMIN, TMAX + 1):
        if not onboard[-1] or (t1 <= temp <= t2):
            answer = min(answer, dp[-1][temp - TMIN])
    return answer


import heapq
from collections import deque
def solution(n, roads):
    INF = 10**30
    g = [[] for _ in range(n+1)]
    for i, (u, v, l, t) in enumerate(roads):
        w = l + t
        g[u].append((v, w, i+1))
        g[v].append((u, w, i+1))
    def dijkstra(s):
        dist = [INF]*(n+1)
        dist[s] = 0
        pq = [(0, s)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]: continue
            for v, w, _ in g[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        return dist
    d1 = dijkstra(1)
    dn = dijkstra(n)
    best = d1[n]
    dec = set()
    for i, (u, v, l, _) in enumerate(roads):
        if d1[u] + l + dn[v] < best or d1[v] + l + dn[u] < best:
            dec.add(i+1)
    dag = [[] for _ in range(n+1)]
    rdag = [[] for _ in range(n+1)]
    indeg = [0]*(n+1)
    outdeg = [0]*(n+1)
    edge_id = {}
    for i, (u, v, l, t) in enumerate(roads):
        w = l + t
        if d1[u] + w + dn[v] == best:
            dag[u].append(v)
            rdag[v].append(u)
            indeg[v] += 1
            outdeg[u] += 1
            edge_id[(u, v)] = i+1
        if d1[v] + w + dn[u] == best:
            dag[v].append(u)
            rdag[u].append(v)
            indeg[u] += 1
            outdeg[v] += 1
            edge_id[(v, u)] = i+1
    from_start = [0]*(n+1)
    q = deque()
    from_start[1] = 1
    q.append(1)
    while q:
        u = q.popleft()
        for v in dag[u]:
            from_start[v] += from_start[u]
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    to_end = [0]*(n+1)
    q = deque()
    to_end[n] = 1
    q.append(n)
    while q:
        u = q.popleft()
        for v in rdag[u]:
            to_end[v] += to_end[u]
            outdeg[v] -= 1
            if outdeg[v] == 0:
                q.append(v)
    total = from_start[n]
    inc = set()
    for (u, v), idx in edge_id.items():
        if from_start[u] * to_end[v] == total:
            inc.add(idx)
    ans = sorted(dec | inc)
    return ans if ans else [-1]


def solution(heights):
    heights.sort()
    minusV = []
    n = len(heights)
    half = n // 2
    if n % 2 == 1:  
        for i in range(half):
            minusV.append(heights[i + half] - heights[i])
        minusV.append(heights[-1] - heights[half])
        minusV.sort()
        return minusV[1]
    else: 
        for i in range(half):
            minusV.append(heights[i + half] - heights[i])
        minusV.sort()
        return minusV[0]
