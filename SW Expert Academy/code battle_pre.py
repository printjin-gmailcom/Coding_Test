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
    

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    while True:
        s = input().strip()
        if s:
            break
    n = s.count('N')
    s_cnt = s.count('S')
    e = s.count('E')
    w = s.count('W')
    ok = True
    if (n == 0) != (s_cnt == 0):
        ok = False
    if (e == 0) != (w == 0):
        ok = False
    print("Yes" if ok else "No")


import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    while True:
        line = input().strip()
        if line:
            break
    n = int(line)
    deg = [0] * (n + 1)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        deg[u] += 1
        deg[v] += 1
    ans = 0
    for i in range(1, n + 1):
        if deg[i] > 2:
            ans += deg[i] - 2
    print(ans)


import sys
input = sys.stdin.readline
TC = int(input())
for _ in range(TC):
    N, x = map(int, input().split())
    A = list(map(int, input().split()))
    total = 0
    for i in range(N):
        total += A[i] << i
    ans = 0
    for v in range(total // x + 1):
        carry = 0
        ok = True
        for i in range(61):
            have = carry
            if i < N:
                have += A[i]
            need = x if ((v >> i) & 1) else 0
            if have < need:
                ok = False
                break
            have -= need
            carry = have // 2
        if ok:
            ans += 1
    print(ans)


MOD = 998244353
def solve_color(lengths):
    m = len(lengths)
    dp = [[0] * (m + 1) for _ in range(m + 1)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(i + 1):
            dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD
            if lengths[i] > j:
                dp[i + 1][j + 1] = (
                    dp[i + 1][j + 1]
                    + dp[i][j] * (lengths[i] - j)
                ) % MOD
    return dp[m]
TC = int(input())
for _ in range(TC):
    N = int(input())
    black = []
    white = []
    lens = [min(i + 1, 2 * N - 1 - i) for i in range(2 * N - 1)]
    for i, l in enumerate(lens):
        if i % 2 == 0:
            black.append(l)
        else:
            white.append(l)
    b = solve_color(black)
    w = solve_color(white)
    ans = []
    for k in range(1, 2 * N):
        cur = 0
        for i in range(max(0, k - len(w)), min(k, len(b)) + 1):
            cur = (cur + b[i] * w[k - i]) % MOD
        ans.append(cur)
    print(*ans)


import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    A = input().strip()
    n = A.count('N')
    s = A.count('S')
    e = A.count('E')
    w = A.count('W')
    if (n == 0) != (s == 0):
        print("No")
    elif (e == 0) != (w == 0):
        print("No")
    else:
        print("Yes")


import sys
input = sys.stdin.readline
TC = int(input())
for _ in range(TC):
    N = int(input())
    deg = [0] * (N + 1)
    for _ in range(N - 1):
        u, v = map(int, input().split())
        deg[u] += 1
        deg[v] += 1
    ans = 0
    for i in range(1, N + 1):
        if deg[i] > 2:
            ans += deg[i] - 2
    print(ans)


import sys
input = sys.stdin.readline
def solve():
    N, M, K = map(int, input().split())
    C = list(map(int, input().split()))
    likes = [[] for _ in range(K)]
    for worker in range(M):
        data = list(map(int, input().split()))
        for color in data[1:]:
            likes[color].append(worker)
    cnt = [0] * M
    full = 0
    for i in range(M):
        offset = (-i) % M
        for w in likes[C[i]]:
            r = (w + offset) % M
            if cnt[r] == M - 1:
                full += 1
            cnt[r] += 1
    valid = [False] * (N - M + 1)
    valid[0] = full > 0
    for y in range(1, N - M + 1):
        out_pos = y - 1
        in_pos = y + M - 1
        offset = (-out_pos) % M
        for w in likes[C[out_pos]]:
            r = (w + offset) % M
            if cnt[r] == M:
                full -= 1
            cnt[r] -= 1
        for w in likes[C[in_pos]]:
            r = (w + offset) % M
            if cnt[r] == M - 1:
                full += 1
            cnt[r] += 1
        valid[y] = full > 0
    answer = 0
    pos = 0
    last_valid = -1
    for y in range(len(valid)):
        if valid[y]:
            last_valid = y
        if y == pos:
            if last_valid < pos:
                return -1
            answer += 1
            pos = last_valid + M
            if pos >= N:
                return answer
    return -1
T = int(input())
for _ in range(T):
    print(solve())


import sys
input = sys.stdin.readline
def solve():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    edges.sort(key=lambda x: x[2])
    total = N + M
    parent = [-1] * total
    deg = [0] * N
    bad = [False] * total
    head = [-1] * total
    to = [0] * (2 * M)
    nxt = [0] * (2 * M)
    ecnt = 0
    def add_edge(u, v):
        nonlocal ecnt
        to[ecnt] = v
        nxt[ecnt] = head[u]
        head[u] = ecnt
        ecnt += 1
    def find(x):
        while parent[x] >= 0:
            if parent[parent[x]] >= 0:
                parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    cur = N
    for u, v, w in edges:
        deg[u] += 1
        deg[v] += 1
        fu = find(u)
        fv = find(v)
        node = cur
        cur += 1
        if deg[u] >= 3 or deg[v] >= 3:
            bad[node] = True
        if bad[fu] or bad[fv] or fu == fv:
            bad[node] = True
        parent[node] = parent[fu]
        if fu != fv:
            parent[node] += parent[fv]
        parent[fu] = node
        parent[fv] = node
        add_edge(node, fu)
        if fu != fv:
            add_edge(node, fv)
    LOG = (total).bit_length()
    up = [[0] * total for _ in range(LOG)]
    depth = [0] * total
    low_bad = [-1] * total
    roots = [i for i in range(total) if parent[i] < 0]
    stack = []
    for root in roots:
        up[0][root] = root
        stack.append((root, -1, -1))
        while stack:
            u, p, last = stack.pop()
            if bad[u]:
                last = u
            low_bad[u] = last
            if p != -1:
                up[0][u] = p
                depth[u] = depth[p] + 1
            e = head[u]
            while e != -1:
                v = to[e]
                if v != p:
                    stack.append((v, u, last))
                e = nxt[e]
    for k in range(1, LOG):
        prev = up[k - 1]
        cur_up = up[k]
        for i in range(total):
            cur_up[i] = prev[prev[i]]
    def lca(a, b):
        if depth[a] < depth[b]:
            a, b = b, a
        diff = depth[a] - depth[b]
        bit = 0
        while diff:
            if diff & 1:
                a = up[bit][a]
            diff >>= 1
            bit += 1
        if a == b:
            return a
        for k in range(LOG - 1, -1, -1):
            if up[k][a] != up[k][b]:
                a = up[k][a]
                b = up[k][b]
        return up[0][a]
    Q = int(input())
    ans = []
    for _ in range(Q):
        x, y = map(int, input().split())
        z = lca(x, y)
        b = low_bad[z]
        if b < N:
            ans.append("-1")
        else:
            ans.append(str(edges[b - N][2]))
    print(" ".join(ans))
T = int(input())
for _ in range(T):
    solve()


import math
T = int(input())
for _ in range(T):
    S, P = map(int, input().split())
    d = S * S - 4 * P
    if d >= 0 and math.isqrt(d) ** 2 == d:
        r = math.isqrt(d)
        print("Yes" if (S + r) % 2 == 0 else "No")
    else:
        print("No")


T = int(input())
for _ in range(T):
    N = int(input())
    S = input().strip()
    stack = []
    for c in S:
        stack.append(c)
        if len(stack) >= 3 and stack[-3:] == ['f', 'o', 'x']:
            del stack[-3:]
    print(len(stack))
    

import sys
input = sys.stdin.readline
def has_prime_1_mod_4(n):
    p = 3
    while p * p <= n:
        if n % p == 0:
            if p % 4 == 1:
                return True
            while n % p == 0:
                n //= p
        p += 2
    return n > 1 and n % 4 == 1
T = int(input())
for _ in range(T):
    X, Y, S = map(int, input().split())
    odd = S
    two = 1
    while odd % 2 == 0:
        odd //= 2
        two *= 2
    if has_prime_1_mod_4(odd):
        g = two
    else:
        g = S
    if X % g == 0 and Y % g == 0:
        print("yes")
    else:
        print("no")


import sys
input = sys.stdin.readline
def solve():
    T = int(input())
    for _ in range(T):
        H, W = map(int, input().split())
        board = [input().strip() for _ in range(H)]
        forbidden = set()
        for r1 in range(H):
            for c1 in range(W):
                for r2 in range(H):
                    for c2 in range(W):
                        if board[r1][c1] != board[r2][c2]:
                            forbidden.add((r2 - r1, c2 - c1))
        def valid(a, b, c):
            for dy, dx in forbidden:
                if dy % c != 0:
                    continue
                y = dy // c
                if (dx - y * b) % a == 0:
                    return False
            return True
        for area in range(1, H * W + 1):
            found = False
            for a in range(1, area + 1):
                if area % a != 0:
                    continue
                c = area // a
                for b in range(a):
                    if valid(a, b, c):
                        found = True
                        break
                if found:
                    break
            if found:
                print(area)
                break


import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    X, Y, Z = map(int, input().split())
    M = max(X, Y, Z)
    if (X == M) + (Y == M) + (Z == M) < 2:
        print(-1, -1, -1)
        continue
    if X <= Y and X <= Z:
        A = X
        B = X
        C = M
    elif Y <= X and Y <= Z:
        A = M
        B = Y
        C = Y
    else:
        A = Z
        B = M
        C = Z
    print(A, B, C)


import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    d = list(map(int, input().split()))
    X = abs(X)
    if X == 0:
        print(0)
        continue
    prefix = [0] * (N + 1)
    max_val = 0
    max_idx = -1
    answer = -1
    for i in range(N):
        prefix[i + 1] = prefix[i] + d[i]
        max_val = max(max_val, d[i])
        if d[i] == max_val and max_idx == -1:
            max_idx = i
        S = prefix[i + 1]
        M = max(d[:i + 1])
        if S >= X and S >= 2 * M - X:
            answer = i + 1
            break
    if answer != -1:
        print(answer)
        continue
    M = max(d)
    total = sum(d)
    need = max(X, 2 * M - X)
    q = max(0, (need - 1) // total)
    base_sum = q * total
    if base_sum >= need:
        print(q * N)
        continue
    current = base_sum
    for i in range(N):
        current += d[i]
        if current >= need:
            print(q * N + i + 1)
            break


import sys
from collections import deque
input = sys.stdin.readline
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
T = int(input())
for _ in range(T):
    C = int(input())
    dsu = DSU(26)
    edges = []
    for _ in range(C):
        a, _, b, _, s = input().split()
        u = ord(b) - ord('A')
        v = ord(a) - ord('A')
        s = s[1:-1]
        edges.append((u, v, s))
        if not s:
            dsu.union(u, v)
    possible = True
    compressed_edges = []
    for u, v, s in edges:
        u = dsu.find(u)
        v = dsu.find(v)
        if u == v:
            if s:
                possible = False
                break
            continue
        compressed_edges.append((u, v, s))
    if not possible:
        print(-1)
        continue
    group_id = {}
    for i in range(26):
        root = dsu.find(i)
        if root not in group_id:
            group_id[root] = len(group_id)
    N = len(group_id)
    graph = [[] for _ in range(N)]
    indegree = [0] * N
    for u, v, s in compressed_edges:
        u = group_id[u]
        v = group_id[v]
        graph[u].append((v, s))
        indegree[v] += 1
    q = deque()
    for i in range(N):
        if indegree[i] == 0:
            q.append(i)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v, s in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    if len(order) != N:
        print(-1)
        continue
    value = [None] * N
    for u in order:
        if value[u] is None:
            value[u] = ""
        for v, s in graph[u]:
            candidate = value[u] + s
            if value[v] is None:
                value[v] = candidate
            elif value[v] != candidate:
                possible = False
                break
        if not possible:
            break
    if not possible:
        print(-1)
        continue
    answer = 0
    for i in range(26):
        root = dsu.find(i)
        group = group_id[root]
        answer += len(value[group])
    print(answer)


import sys
input = sys.stdin.readline
def can_match(graph, start, used, n):
    match = [-1] * n
    for g in used:
        match[g] = -2
    def dfs(child, visited):
        for gift in graph[child]:
            if gift in used or visited[gift]:
                continue
            visited[gift] = True
            if match[gift] == -1 or dfs(match[gift], visited):
                match[gift] = child
                return True
        return False
    for child in range(start, n):
        visited = [False] * n
        if not dfs(child, visited):
            return False
    return True
T = int(input())
for _ in range(T):
    N = int(input())
    A = []
    for _ in range(N):
        A.append([x - 1 for x in map(int, input().split())])
    first = [A[i][0] for i in range(N)]
    is_first = [False] * N
    for gift in first:
        is_first[gift] = True
    second = [-1] * N
    for i in range(N):
        for gift in A[i]:
            if not is_first[gift]:
                second[i] = gift
                break
    graph = []
    for i in range(N):
        choices = [first[i]]
        if second[i] != -1:
            choices.append(second[i])
        choices.sort()
        graph.append(choices)
    answer = [-1] * N
    used = set()
    possible = True
    for i in range(N):
        chosen = -1
        for gift in graph[i]:
            if gift in used:
                continue
            used.add(gift)
            if can_match(graph, i + 1, used, N):
                chosen = gift
                break
            used.remove(gift)
        if chosen == -1:
            possible = False
            break
        answer[i] = chosen
    if possible:
        print(*(x + 1 for x in answer))
    else:
        print(-1)
