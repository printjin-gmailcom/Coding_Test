import sys
input = sys.stdin.readline
TC = int(input())
queries = []
mx = 0
for _ in range(TC):
    n = int(input())
    queries.append(n)
    mx = max(mx, n)
A = [0] * (max(2, mx + 1))
A[0] = 1
if mx >= 1:
    A[1] = 1
for i in range(2, mx + 1):
    forbid = set()
    for k in range(1, i // 2 + 1):
        x = 2 * A[i - k] - A[i - 2 * k]
        if x > 0:
            forbid.add(x)
    cur = 1
    while cur in forbid:
        cur += 1
    A[i] = cur
for n in queries:
    print(A[n])


import sys
input = sys.stdin.readline
TC = int(input())
for _ in range(TC):
    input()
    N = int(input())
    S = [input().strip() for _ in range(N)]
    ans = 0
    for d in range(N):
        ok = True
        for x in range(N):
            if not ok:
                break
            for y in range(N):
                if S[x][y] != S[(y + d) % N][(x - d) % N]:
                    ok = False
                    break
        if ok:
            ans += N
    print(ans)


###
import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline
N, Q = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)
parent = [-1]*N
size = [1]*N
order = [0]
for u in order:
    for v in g[u]:
        if v != parent[u]:
            parent[v]=u
            order.append(v)
for u in reversed(order[1:]):
    size[parent[u]] += size[u]
sets = set()
sets.add(N)
for u in range(1,N):
    sets.add(size[u])
    sets.add(N-size[u])
print(len(sets))


###
import sys
input = sys.stdin.readline
def solve():
    TC = int(input())
    out = []
    for _ in range(TC):
        N, Q, M = map(int, input().split())
        edges = []
        for _ in range(M):
            u, v, w = map(int, input().split())
            edges.append((w, u-1, v-1))
        edges.sort()
        parent = list(range(N))
        size = [1]*N
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a,b):
            a=find(a)
            b=find(b)
            if a==b:
                return False
            if size[a]<size[b]:
                a,b=b,a
            parent[b]=a
            size[a]+=size[b]
            return True
        mst = 0
        cnt = 0
        for w,u,v in edges:
            if union(u,v):
                mst += w
                cnt += 1
        ans=[]
        for i in range(2,Q+2):
            ans.append(str((i-1)*mst))
        out.append(" ".join(ans))
    print("\n".join(out))


import sys
from collections import defaultdict
input = sys.stdin.readline
TC = int(input())
ans = []
for _ in range(TC):
    N, S = input().split()
    cnt = defaultdict(int)
    cnt[(0, 0)] = 1
    a = 0
    c = 0
    res = 0
    for ch in S:
        if ch == 'A':
            a += 1
        elif ch == 'T':
            a -= 1
        elif ch == 'C':
            c += 1
        else:  # G
            c -= 1
        key = (a, c)
        res += cnt[key]
        cnt[key] += 1
    ans.append(str(res))
print("\n".join(ans))


import sys
sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline
TC = int(input())
for _ in range(TC):
    N, M, K = map(int, input().split())
    color = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    ans = 0
    def dfs(now, depth, used_color, visited):
        nonlocal_ans[0] += 1
        if depth == K - 1:
            return
        for nxt in graph[now]:
            if nxt in visited:
                continue
            c = color[nxt]
            if used_color & (1 << c):
                continue
            visited.add(nxt)
            dfs(
                nxt,
                depth + 1,
                used_color | (1 << c),
                visited
            )
            visited.remove(nxt)
    for start in range(1, N + 1):
        nonlocal_ans = [0]
        dfs(
            start,
            1,
            1 << color[start],
            {start}
        )
        ans += nonlocal_ans[0] - 1
    print(ans)
    

import sys
import math
input = sys.stdin.readline
def fft(a, invert):
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    length = 2
    while length <= n:
        ang = 2 * math.pi / length
        if invert:
            ang = -ang
        wlen = complex(math.cos(ang), math.sin(ang))
        for i in range(0, n, length):
            w = 1
            half = length // 2
            for j in range(i, i + half):
                u = a[j]
                v = a[j + half] * w
                a[j] = u + v
                a[j + half] = u - v
                w *= wlen
        length *= 2
    if invert:
        for i in range(n):
            a[i] /= n
def multiply(a, b):
    n = 1
    while n < len(a) + len(b):
        n <<= 1
    fa = list(map(complex, a)) + [0] * (n - len(a))
    fb = list(map(complex, b)) + [0] * (n - len(b))
    fft(fa, False)
    fft(fb, False)
    for i in range(n):
        fa[i] *= fb[i]
    fft(fa, True)
    return [int(round(x.real)) for x in fa]
TC = int(input())
OFFSET = 30000
SIZE = 60001
answer = []
for _ in range(TC):
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    K = int(input())
    C = list(map(int, input().split()))
    freqA = [0] * SIZE
    freqC = [0] * SIZE
    for x in A:
        freqA[x + OFFSET] += 1
    for x in C:
        freqC[x + OFFSET] += 1
    conv = multiply(freqA, freqC)
    result = 0
    for b in B:
        target = 2 * b
        idx = target + 60000
        if 0 <= idx < len(conv):
            result += conv[idx]
    answer.append(str(result))
print("\n".join(answer))


import sys
input = sys.stdin.readline
TC = int(input())
for _ in range(TC):
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans = max(ans, (j - i) * (A[i] + A[j]))
    print(ans)


import sys
from functools import lru_cache
input = sys.stdin.readline
TC = int(input())
masks = [i for i in range(1, 16)]
idx = {m: i for i, m in enumerate(masks)}
adj = [0] * 15
for i, a in enumerate(masks):
    for j, b in enumerate(masks):
        if a & b:
            adj[i] |= 1 << j
independent = [False] * (1 << 15)
independent[0] = True
for s in range(1, 1 << 15):
    b = (s & -s).bit_length() - 1
    t = s ^ (1 << b)
    independent[s] = independent[t] and ((adj[b] & t) == 0)
for _ in range(TC):
    while True:
        line = input().strip()
        if line:
            break
    N, K = map(int, line.split())
    belong = [0] * (N + 1)
    for i in range(K):
        arr = list(map(int, input().split()))
        for v in arr[1:]:
            belong[v] |= 1 << i
    w = [0] * 15
    for v in range(1, N + 1):
        if belong[v]:
            w[idx[belong[v]]] += 1
    @lru_cache(None)
    def solve(state):
        if state == tuple(w):
            return 0
        rem = []
        mask = 0
        for i in range(15):
            if state[i] < w[i]:
                rem.append(i)
                mask |= 1 << i
        ans = 10 ** 9
        sub = mask
        while sub:
            if independent[sub]:
                nxt = list(state)
                x = sub
                while x:
                    b = (x & -x).bit_length() - 1
                    nxt[b] += 1
                    x ^= 1 << b
                ans = min(ans, 1 + solve(tuple(nxt)))
            sub = (sub - 1) & mask
        return ans
    print(solve((0,) * 15))


###
import sys
from collections import defaultdict
input = sys.stdin.buffer.readline
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            self.p[b] = a
def solve():
    N = int(input())
    pos = []
    for _ in range(N):
        x, y, z = map(int, input().split())
        pos.append([x, y, z])
    M = int(input())
    edges = []
    adj = [[] for _ in range(N)]
    for i in range(M):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edges.append([u, v, w, 0]) 
        adj[u].append(i)
        adj[v].append(i)
    K = int(input())
    weather = []
    for _ in range(K):
        v, d = map(int, input().split())
        weather.append((v - 1, d))
    alive = [True] * M
    def check(e):
        u, v, w, _ = edges[e]
        dx = pos[u][0] - pos[v][0]
        dy = pos[u][1] - pos[v][1]
        dz = pos[u][2] - pos[v][2]
        return dx*dx + dy*dy + dz*dz <= w*w
    removed = defaultdict(list)
    for day, (v, d) in enumerate(weather, 1):
        pos[v][2] += d
        for ei in adj[v]:
            if alive[ei] and not check(ei):
                alive[ei] = False
                edges[ei][3] = day
                removed[day].append(ei)
    Q = int(input())
    queries = []
    for i in range(Q):
        a, b = map(int, input().split())
        queries.append((a-1, b-1))
    ans = []
    states = []
    for day in range(K + 1):
        dsu = DSU(N)
        for idx, (u, v, w, dead) in enumerate(edges):
            if dead == 0 or dead > day:
                dsu.union(u, v)
        states.append(dsu)
    for a, b in queries:
        ret = K
        for day in range(K + 1):
            if states[day].find(a) != states[day].find(b):
                ret = day - 1
                break
        ans.append(str(ret))
    print("\n".join(ans))


T = int(input())
for _ in range(T):
    while True:
        line = input().strip()
        if line:
            X, Y = map(int, line.split())
            break
    A = (X + Y) // 2
    B = (X - Y) // 2
    print(A, B)


import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    works = []
    for _ in range(N):
        t, d = map(int, input().split())
        works.append((t, d))
    works.sort(key=lambda x: x[1], reverse=True)
    cur = 10**18
    for t, d in works:
        cur = min(cur, d)
        cur -= t
    print(cur)


import sys
from bisect import bisect_left
input = sys.stdin.readline
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 2)
    def add(self, idx, val):
        n = self.n
        bit = self.bit
        while idx <= n:
            bit[idx] += val
            idx += idx & -idx
    def sum(self, idx):
        s = 0
        bit = self.bit
        while idx:
            s += bit[idx]
            idx -= idx & -idx
        return s
TC = int(input())
for _ in range(TC):
    n, m = map(int, input().split())
    liquids = []
    prices = []
    for _ in range(n):
        d, p, l = map(int, input().split())
        liquids.append((d, p, l))
        prices.append(p)
    queries = []
    for i in range(m):
        g, L = map(int, input().split())
        queries.append((g, L))
    prices = sorted(set(prices))
    P = len(prices)
    liquids.sort(reverse=True)
    tastes = sorted({d for d, _, _ in liquids})
    # parallel binary search
    lo = [-1] * m
    hi = [len(tastes)] * m
    while True:
        bucket = [[] for _ in range(len(tastes))]
        active = False
        for i in range(m):
            if lo[i] + 1 < hi[i]:
                active = True
                mid = (lo[i] + hi[i]) // 2
                bucket[mid].append(i)
        if not active:
            break
        bitAmt = Fenwick(P)
        bitCost = Fenwick(P)
        ptr = 0
        for idx in range(len(tastes) - 1, -1, -1):
            needTaste = tastes[idx]
            while ptr < n and liquids[ptr][0] >= needTaste:
                d, p, l = liquids[ptr]
                k = bisect_left(prices, p) + 1
                bitAmt.add(k, l)
                bitCost.add(k, l * p)
                ptr += 1
            totalAmt = bitAmt.sum(P)
            for qi in bucket[idx]:
                g, L = queries[qi]
                if totalAmt < L:
                    lo[qi] = idx
                    continue
                left = 1
                right = P
                while left < right:
                    mid = (left + right) // 2
                    if bitAmt.sum(mid) >= L:
                        right = mid
                    else:
                        left = mid + 1
                pos = left
                amtBefore = bitAmt.sum(pos - 1)
                costBefore = bitCost.sum(pos - 1)
                remain = L - amtBefore
                price = prices[pos - 1]
                cost = costBefore + remain * price
                if cost <= g:
                    hi[qi] = idx
                else:
                    lo[qi] = idx
    ans = []
    for i in range(m):
        if hi[i] == len(tastes):
            ans.append("-1")
        else:
            ans.append(str(tastes[hi[i]]))
    print(" ".join(ans))


from itertools import combinations
INF = 10**18
T = int(input())
for _ in range(T):
    n, m, d = map(int, input().split())
    keys = []
    for _ in range(m):
        tmp = list(map(int, input().split()))
        c = tmp[0]
        s = tmp[1] - 1
        k = tmp[2]
        mask = 0
        for x in tmp[3:]:
            mask |= 1 << (x - 1)
        keys.append((c, s, mask))
    b = [int(input()) for _ in range(d)]
    ALL = (1 << n) - 1
    ans = INF
    for r in range(1, m + 1):
        for comb in combinations(range(m), r):
            cover = 0
            cost = 0
            cnt = [0] * d
            ok = True
            for idx in comb:
                c, s, mask = keys[idx]
                cost += c
                cover |= mask
                cnt[s] += 1
                if cnt[s] > b[s]:
                    ok = False
                    break
            if not ok:
                continue
            if cover == ALL:
                ans = min(ans, cost)
    if ans == INF:
        print(-1)
    else:
        print(ans)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    ans = 0
    for i in range(N):
        x1, y1 = points[i]
        max_dx = 0
        max_dy = 0
        for j in range(N):
            if i == j:
                continue
            x2, y2 = points[j]
            if x1 == x2:
                max_dy = max(max_dy, abs(y1 - y2))
            if y1 == y2:
                max_dx = max(max_dx, abs(x1 - x2))
        ans = max(ans, max_dx * max_dy)
    print(ans)


T = int(input())
for _ in range(T):
    N = int(input())
    M = N * (N - 1) // 2
    w = list(map(int, input().split()))
    w.sort()
    mn = sum(w[:N - 1])
    mx = 0
    idx = 0
    comp = N
    while comp > 1:
        mx += w[idx]
        idx += comp - 1
        comp -= 1
    print(mn, mx)


MOD = 998244353
def swap_row(A, i, j):
    A[i], A[j] = A[j], A[i]
def swap_col(A, i, j):
    for r in range(len(A)):
        A[r][i], A[r][j] = A[r][j], A[r][i]
def hessenberg(A):
    n = len(A)
    for c in range(n-2):
        p = -1
        for i in range(c+1, n):
            if A[i][c]:
                p = i
                break
        if p == -1:
            continue
        if p != c+1:
            swap_row(A, p, c+1)
            swap_col(A, p, c+1)
        inv = pow(A[c+1][c], MOD-2, MOD)
        for i in range(c+2, n):
            if A[i][c] == 0:
                continue
            k = A[i][c] * inv % MOD
            for j in range(c, n):
                A[i][j] = (A[i][j] - k*A[c+1][j]) % MOD
            for j in range(n):
                A[j][c+1] = (A[j][c+1] + k*A[j][i]) % MOD
    return A
def mul(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] = (c[i+j] + x*y) % MOD
    return c
def characteristic_polynomial(A):
    n = len(A)
    poly = [1]
    for i in range(n):
        poly = mul(poly, [(-A[i][i])%MOD, 1])
    return poly
def convert(poly):
    n = len(poly)-1
    res = [0]*(n+1)
    for i,c in enumerate(poly):
        res[n-i] = c
    return res
def horner(poly, x):
    ans = 0
    for c in poly:
        ans = (ans*x+c)%MOD
    return ans
H = hessenberg(A)
poly = characteristic_polynomial(H)
poly = convert(poly)


import sys
input = sys.stdin.readline
TC = int(input())
for _ in range(TC):
    n = int(input())
    p = list(map(int, input().split()))
    ans = [0] * (n + 1)
    for i, station in enumerate(p):
        ans[station] = i % 24 + 1
    print(*ans[1:])
    
