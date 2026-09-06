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


import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline
def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        graph = [[] for _ in range(N)]
        for _ in range(N - 1):
            u, v, c = map(int, input().split())
            u -= 1
            v -= 1
            graph[u].append((v, c))
            graph[v].append((u, c))
        parent = [-1] * N
        parent_edge = [0] * N
        order = [0]
        parent[0] = 0
        for u in order:
            for v, c in graph[u]:
                if parent[v] != -1:
                    continue
                parent[v] = u
                parent_edge[v] = c
                order.append(v)
        children = [[] for _ in range(N)]
        for v in range(1, N):
            children[parent[v]].append(v)
        path = []
        cur = N - 1
        while cur != 0:
            path.append(cur)
            cur = parent[cur]
        path.append(0)
        path.reverse()
        on_path = [False] * N
        for x in path:
            on_path[x] = True
        def combine_any_order(dp1, dp2):
            res = {}
            for (r1, g1), cnt1 in dp1.items():
                for (r2, g2), cnt2 in dp2.items():
                    req_a = max(r1, r1 + r2 - g1)
                    req_b = max(r2, r2 + r1 - g2)
                    req = max(req_a, req_b)
                    gain = g1 + g2
                    key = (req, gain)
                    res[key] = res.get(key, 0) + cnt1 * cnt2
            return res
        off_dp = [None] * N
        for u in reversed(order):
            curdp = {
                (0, 0): 1,
                (0, 1): 1,
            }
            for v in children[u]:
                if on_path[u] and on_path[v]:
                    continue
                c = parent_edge[v]
                child_dp = off_dp[v]
                task_dp = {}
                for (r, g), cnt in child_dp.items():
                    nr = r + c
                    ng = g - c
                    key = (nr, ng)
                    task_dp[key] = task_dp.get(key, 0) + cnt
                curdp = combine_any_order(curdp, task_dp)
            off_dp[u] = curdp
        states = {(0, 0): 1}
        for i, u in enumerate(path):
            states = combine_any_order(states, off_dp[u])
            if i + 1 < len(path):
                v = path[i + 1]
                c = 0
                for to, cc in graph[u]:
                    if to == v:
                        c = cc
                        break
                new_states = {}
                for (r, g), cnt in states.items():
                    nr = r + c
                    ng = g - c
                    key = (nr, ng)
                    new_states[key] = new_states.get(key, 0) + cnt
                states = new_states
        ans = 0
        for (r, g), cnt in states.items():
            if r == 0:
                ans += cnt
        print(ans)


import sys
input = sys.stdin.readline
M = 70
P5 = 5 ** M
PERIOD = 4 * 5 ** (M - 1)
P2 = 1 << M
def discrete_log(y):
    n = [0, 1, 3, 2][y % 5]
    p4 = 4
    for k in range(1, M):
        mod = 5 ** (k + 1)
        step = p4
        cur = pow(2, n, mod)
        target = y % mod
        factor = pow(2, step, mod)
        v = cur
        for d in range(5):
            if v == target:
                n += d * step
                break
            v = v * factor % mod
        p4 *= 5
    return n
def solve():
    T = int(input())
    out = []
    for _ in range(T):
        x = input().strip()
        l = len(x)
        k = M - l
        a = int(x) * 10 ** k
        r = (-a) % P2
        limit = 10 ** k
        while r >= limit:
            r -= P2
        if r < 0:
            r += P2
        t = 0
        while r % 5 == 0:
            r += P2
            t += 1
        y = a + r
        n = discrete_log(y)
        if n < M:
            n += PERIOD
        out.append(str(n))
    sys.stdout.write("\n".join(out))
solve()


import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    S = input().strip()
    right = 0
    left = 0
    cur = 0
    for ch in S:
        if ch == 'R':
            cur += 1
        elif ch == 'L':
            cur -= 1
        else: 
            if cur >= 0:
                cur += 1
            else:
                cur -= 1
        right = max(right, cur)
        left = min(left, cur)
    print(max(abs(left), abs(right)))


import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    dist = []
    for a in A:
        cur = {a}
        d = {a: 0}
        while cur:
            nxt = set()
            for x in cur:
                if x == 1:
                    continue
                p = x // 2
                q = x - p
                if p not in d:
                    d[p] = d[x] + 1
                    nxt.add(p)
                if q not in d:
                    d[q] = d[x] + 1
                    nxt.add(q)
            cur = nxt
        dist.append(d)
    answer = float('inf')
    for target in dist[0]:
        total = 0
        possible = True
        for d in dist:
            if target not in d:
                possible = False
                break
            total += d[target]
        if possible:
            answer = min(answer, total)
    print(answer)


import sys
MOD = 1000000007
input = sys.stdin.readline
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = [input().split() for _ in range(N)]
    max_len = sum(max(len(a), len(b)) for a, b in cards)
    pow10 = [1] * (max_len + 1)
    for i in range(1, max_len + 1):
        pow10[i] = pow10[i - 1] * 10 % MOD
    vals = [[0, 0] for _ in range(N)]
    lens = [[0, 0] for _ in range(N)]
    for i in range(N):
        for k in range(2):
            s = cards[i][k]
            lens[i][k] = len(s)
            vals[i][k] = int(s) % MOD
    ans = 0
    for i in range(N):
        for si in range(2):
            cur = vals[i][si]
            for j in range(N):
                if i == j:
                    continue
                x = cards[i][si]
                factor = 0
                for sj in range(2):
                    y = cards[j][sj]
                    if y + x < x + y:
                        factor += 1
                    else:
                        factor += pow10[lens[j][sj]]
                cur = cur * factor % MOD
            ans = (ans + cur) % MOD
    print(f"#{tc} {ans}")


import sys
import heapq
input = sys.stdin.readline
INF = 10**30
class MCF:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]
    def add(self, u, v, cap, cost):
        a = [v, len(self.g[v]), cap, cost]
        b = [u, len(self.g[u]), 0, -cost]
        self.g[u].append(a)
        self.g[v].append(b)
    def solve(self, s, t, weights):
        n = self.n
        mx = max(weights)
        pot = [-mx] * n
        pot[s] = 0
        ans = 0
        while True:
            dist = [INF] * n
            prev_v = [-1] * n
            prev_e = [-1] * n
            dist[s] = 0
            pq = [(0, s)]
            while pq:
                d, u = heapq.heappop(pq)
                if d != dist[u]:
                    continue
                for ei, e in enumerate(self.g[u]):
                    if e[2] <= 0:
                        continue
                    v = e[0]
                    nd = d + e[3] + pot[u] - pot[v]
                    if nd < dist[v]:
                        dist[v] = nd
                        prev_v[v] = u
                        prev_e[v] = ei
                        heapq.heappush(pq, (nd, v))
            if dist[t] == INF:
                break
            path_cost = dist[t] + pot[t]
            if path_cost >= 0:
                break
            for v in range(n):
                if dist[v] < INF:
                    pot[v] += dist[v]
            v = t
            while v != s:
                u = prev_v[v]
                e = self.g[u][prev_e[v]]
                e[2] -= 1
                self.g[v][e[1]][2] += 1
                v = u
            ans -= path_cost
        return ans
def get_path(n, tree_edges, edges, start, end):
    adj = [[] for _ in range(n)]
    for eid in tree_edges:
        a, b, _ = edges[eid]
        adj[a].append((b, eid))
        adj[b].append((a, eid))
    parent = [-1] * n
    parent_edge = [-1] * n
    parent[start] = start
    stack = [start]
    while stack:
        u = stack.pop()
        if u == end:
            break
        for v, eid in adj[u]:
            if parent[v] != -1:
                continue
            parent[v] = u
            parent_edge[v] = eid
            stack.append(v)
    path = []
    cur = end
    while cur != start:
        path.append(parent_edge[cur])
        cur = parent[cur]
    return path
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    edges = []
    weights = []
    for _ in range(m):
        a, b, w = map(int, input().split())
        edges.append((a - 1, b - 1, w))
        weights.append(w)
    t1 = [x - 1 for x in map(int, input().split())]
    t2 = [x - 1 for x in map(int, input().split())]
    set1 = set(t1)
    set2 = set(t2)
    constraints = [[] for _ in range(m)]
    for eid in range(m):
        a, b, _ = edges[eid]
        if eid not in set1:
            path = get_path(n, t1, edges, a, b)
            for f in path:
                constraints[f].append(eid)
        if eid not in set2:
            path = get_path(n, t2, edges, a, b)
            for f in path:
                constraints[eid].append(f)
    source = m
    sink = m + 1
    flow = MCF(m + 2)
    for i, w in enumerate(weights):
        flow.add(source, i, 1, -w)
        flow.add(i, sink, 1, w)
    for u in range(m):
        for v in constraints[u]:
            flow.add(u, v, m, 0)
    ans = flow.solve(source, sink, weights)
    print(f"#{tc} {ans}")


T = int(input())
for _ in range(T):
    N, P = map(int, input().split())
    s = N * (N + 1) // 2
    if P > s:
        print(s)
    else:
        x = s
        for i in range(N, 0, -1):
            if x - i != P:
                x -= i
                break
        print(x)


import sys
MOD = 1000000007
def mod_sqrt(n):
    if n == 0:
        return 0
    if pow(n, (MOD - 1) // 2, MOD) != 1:
        return -1
    q = MOD - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (MOD + 1) // 4, MOD)
    z = 2
    while pow(z, (MOD - 1) // 2, MOD) != MOD - 1:
        z += 1
    c = pow(z, q, MOD)
    x = pow(n, (q + 1) // 2, MOD)
    t = pow(n, q, MOD)
    m = s
    while t != 1:
        i = 1
        v = t * t % MOD
        while v != 1:
            v = v * v % MOD
            i += 1
        b = pow(c, 1 << (m - i - 1), MOD)
        x = x * b % MOD
        c = b * b % MOD
        t = t * c % MOD
        m = i
    return x
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())
    A %= MOD
    B %= MOD
    C %= MOD
    if A == 0:
        if B == 0:
            print(0 if C == 0 else -1)
        else:
            print((-C * pow(B, MOD - 2, MOD)) % MOD)
        continue
    D = (B * B - 4 * A * C) % MOD
    r = mod_sqrt(D)
    if r == -1:
        print(-1)
    else:
        inv = pow(2 * A, MOD - 2, MOD)
        x = (-B + r) * inv % MOD
        print(x)


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = [''] * N
    selected = [False] * (N + 1)
    a_idx = 0
    b_idx = 0
    for turn in range(N):
        if turn % 2 == 0:
            while selected[A[a_idx]]:
                a_idx += 1
            player = A[a_idx]
            a_idx += 1
            result[player - 1] = 'A'
        else:
            while selected[B[b_idx]]:
                b_idx += 1
            player = B[b_idx]
            b_idx += 1
            result[player - 1] = 'B'
        selected[player] = True
    print(''.join(result))


T = int(input())
for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    if any(a[i] == a[i + 1] for i in range(N - 1)):
        print(-1)
        continue
    candidates = set()
    for x in a:
        candidates.add(2 * x)
    for i in range(N):
        for j in range(i + 1, N):
            if a[i] != a[j]:
                candidates.add(a[i] + a[j])
    answer = 0
    for y in candidates:
        count = 0
        for x in a:
            if 2 * x == y:
                count += 1
        for i in range(N - 1):
            low = min(2 * a[i], 2 * a[i + 1])
            high = max(2 * a[i], 2 * a[i + 1])
            if low < y < high:
                count += 1
        answer = max(answer, count)
    print(answer)
    

import sys
from collections import deque
input = sys.stdin.readline
class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]
    def add_edge(self, u, v, cap):
        self.g[u].append([v, cap, len(self.g[v])])
        self.g[v].append([u, 0, len(self.g[u]) - 1])
    def bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v, cap, rev in self.g[u]:
                if cap > 0 and self.level[v] == -1:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[t] != -1
    def dfs(self, u, t, f):
        if u == t:
            return f
        while self.it[u] < len(self.g[u]):
            i = self.it[u]
            v, cap, rev = self.g[u][i]
            if cap > 0 and self.level[v] == self.level[u] + 1:
                ret = self.dfs(v, t, min(f, cap))
                if ret:
                    self.g[u][i][1] -= ret
                    self.g[v][rev][1] += ret
                    return ret
            self.it[u] += 1
        return 0
    def max_flow(self, s, t):
        flow = 0
        INF = 10**18
        while self.bfs(s, t):
            self.it = [0] * self.n
            while True:
                f = self.dfs(s, t, INF)
                if not f:
                    break
                flow += f
        return flow
def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        c = list(map(int, input().split()))
        trees = []
        for _ in range(2):
            graph = [[] for _ in range(N)]
            for _ in range(N - 1):
                u, v = map(int, input().split())
                u -= 1
                v -= 1
                graph[u].append(v)
                graph[v].append(u)
            trees.append(graph)
        parents = []
        for root in range(N):
            root_parents = []
            for graph in trees:
                parent = [-1] * N
                parent[root] = root
                q = deque([root])
                while q:
                    u = q.popleft()
                    for v in graph[u]:
                        if parent[v] == -1:
                            parent[v] = u
                            q.append(v)
                root_parents.append(parent)
            parents.append(root_parents)
        answer = 0
        INF = 10**15
        for root in range(N):
            S = N
            E = N + 1
            dinic = Dinic(N + 2)
            positive_sum = 0
            for v in range(N):
                if c[v] > 0:
                    dinic.add_edge(S, v, c[v])
                    positive_sum += c[v]
                elif c[v] < 0:
                    dinic.add_edge(v, E, -c[v])
            for tree_idx in range(2):
                parent = parents[root][tree_idx]
                for v in range(N):
                    if v != root:
                        dinic.add_edge(v, parent[v], INF)
            cut = dinic.max_flow(S, E)
            answer = max(answer, positive_sum - cut)
        print(answer)
solve()


import sys
import math
input = sys.stdin.readline
def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]
def poly_add(a, b):
    n = max(len(a), len(b))
    r = [0.0] * n
    for i in range(n):
        if i < len(a):
            r[i] += a[i]
        if i < len(b):
            r[i] += b[i]
    return r
def poly_mul(a, b):
    r = [0.0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r
def poly_deriv(a):
    if len(a) <= 1:
        return [0.0]
    return [a[i] * i for i in range(1, len(a))]
def poly_eval(a, x):
    res = 0.0
    for v in reversed(a):
        res = res * x + v
    return res
def trim(a):
    while len(a) > 1 and abs(a[-1]) < 1e-14:
        a.pop()
    return a
def bisect_root(p, l, r):
    fl = poly_eval(p, l)
    fr = poly_eval(p, r)
    for _ in range(80):
        m = (l + r) * 0.5
        fm = poly_eval(p, m)
        if abs(fm) < 1e-14:
            return m
        if fl * fm <= 0:
            r = m
            fr = fm
        else:
            l = m
            fl = fm
    return (l + r) * 0.5
def real_roots(p, l, r):
    p = trim(p[:])
    if len(p) <= 1:
        return []
    scale = max(1.0, max(abs(x) for x in p))
    eps = 1e-10 * scale
    if len(p) == 2:
        a, b = p
        if abs(b) < 1e-15:
            return []
        x = -a / b
        return [x] if l - 1e-10 <= x <= r + 1e-10 else []
    dp = poly_deriv(p)
    critical = real_roots(dp, l, r)
    points = [l] + critical + [r]
    points.sort()
    roots = []
    for x in points:
        fx = poly_eval(p, x)
        if abs(fx) <= eps:
            roots.append(x)
    for i in range(len(points) - 1):
        a = points[i]
        b = points[i + 1]
        fa = poly_eval(p, a)
        fb = poly_eval(p, b)
        if fa * fb < 0:
            roots.append(bisect_root(p, a, b))
    roots.sort()
    result = []
    for x in roots:
        if l - 1e-9 <= x <= r + 1e-9:
            x = max(l, min(r, x))
            if not result or abs(result[-1] - x) > 1e-7:
                result.append(x)
    return result
def solve_case(n, pts):
    x0, y0 = pts[0]
    p = [(x - x0, y - y0) for x, y in pts]
    edge = []
    edge_cross = []
    for i in range(n):
        a = p[i]
        b = p[(i + 1) % n]
        u = (b[0] - a[0], b[1] - a[1])
        edge.append(u)
        edge_cross.append(cross(a, u))
    prefix = [0.0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + cross(p[i], p[(i + 1) % n])
    total2 = prefix[n]
    target = total2 * 0.5
    def H(i, t):
        return prefix[i] + t * edge_cross[i]
    def area_value(i, t, j, s):
        a = (p[i][0] + edge[i][0] * t,
             p[i][1] + edge[i][1] * t)
        b = (p[j][0] + edge[j][0] * s,
             p[j][1] + edge[j][1] * s)
        return H(j, s) - H(i, t) - cross(a, b)
    def get_s(i, t, j):
        a = p[i]
        u = edge[i]
        b = p[j]
        v = edge[j]
        c0 = prefix[j] - prefix[i] - cross(a, b) - target
        ct = -edge_cross[i] - cross(u, b)
        cs = edge_cross[j] - cross(a, v)
        cts = -cross(u, v)
        den = cs + cts * t
        num = -(c0 + ct * t)
        if abs(den) < 1e-12:
            if abs(num) < 1e-12:
                return 0.0
            return float('inf') if num > 0 else -float('inf')
        return num / den
    def distance2(i, t, j, s):
        ax = p[i][0] + edge[i][0] * t
        ay = p[i][1] + edge[i][1] * t
        bx = p[j][0] + edge[j][0] * s
        by = p[j][1] + edge[j][1] * s
        dx = ax - bx
        dy = ay - by
        return dx * dx + dy * dy
    answer_min = float('inf')
    answer_max = 0.0
    j = 1
    s = 0.0
    for i in range(n):
        if j == i:
            j = (j + 1) % n
            s = 0.0
        t = 0.0
        while t < 1.0 - 1e-12:
            while j != i and get_s(i, t, j) >= 1.0 - 1e-12:
                j = (j + 1) % n
                s = 0.0
            if j == i:
                break
            s0 = get_s(i, t, j)
            if s0 < -1e-9:
                j = (j - 1 + n) % n
                s0 = get_s(i, t, j)
            s0 = max(0.0, min(1.0, s0))
            s1 = get_s(i, 1.0, j)
            if s1 <= 1.0 + 1e-10:
                tend = 1.0
            else:
                a = p[i]
                u = edge[i]
                b = p[j]
                v = edge[j]
                c0 = prefix[j] - prefix[i] - cross(a, b) - target
                ct = -edge_cross[i] - cross(u, b)
                cs = edge_cross[j] - cross(a, v)
                cts = -cross(u, v)
                num = -(c0 + cs - target * 0.0)
                den = ct + cts
                if abs(den) < 1e-14:
                    tend = 1.0
                else:
                    tend = -(c0 + cs) / (ct + cts)
                tend = max(t + 1e-12, min(1.0, tend))
            a = p[i]
            u = edge[i]
            b = p[j]
            v = edge[j]
            c0 = prefix[j] - prefix[i] - cross(a, b) - target
            ct = -edge_cross[i] - cross(u, b)
            cs = edge_cross[j] - cross(a, v)
            cts = -cross(u, v)
            den_poly = [cs, cts]
            num_poly = [-c0, -ct]
            xu = [
                (a[0] - b[0]) * cs - v[0] * (-c0),
                (u[0] * cs + (a[0] - b[0]) * cts) - v[0] * (-ct),
                u[0] * cts
            ]
            yu = [
                (a[1] - b[1]) * cs - v[1] * (-c0),
                (u[1] * cs + (a[1] - b[1]) * cts) - v[1] * (-ct),
                u[1] * cts
            ]
            f = poly_add(poly_mul(xu, xu), poly_mul(yu, yu))
            fp = poly_deriv(f)
            g = poly_add(
                poly_mul(fp, den_poly),
                [-2.0 * x for x in poly_mul(f, [cts])]
            )
            g = trim(g)
            candidates = [t, tend]
            candidates += real_roots(g, t, tend)
            for tt in candidates:
                if t - 1e-9 <= tt <= tend + 1e-9:
                    ss = get_s(i, tt, j)
                    if -1e-8 <= ss <= 1.0 + 1e-8:
                        ss = max(0.0, min(1.0, ss))
                        d = distance2(i, tt, j, ss)
                        answer_min = min(answer_min, d)
                        answer_max = max(answer_max, d)
            if tend >= 1.0 - 1e-10:
                break
            t = tend
            j = (j + 1) % n
            s = 0.0
    return math.sqrt(answer_min), math.sqrt(answer_max)
def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        pts = [tuple(map(int, input().split())) for _ in range(n)]
        mn, mx = solve_case(n, pts)
        print(f"{mn:.10f} {mx:.10f}")


import sys
input = sys.stdin.readline
mex = [
    [1, 2, 1],
    [2, 0, 0],
    [1, 0, 0]
]
def solve(n, top, left):
    cnt = [0, 0, 0]
    for x in top:
        cnt[x] += 1
    for x in left:
        cnt[x] += 1
    a = [0] + top[:]
    b = [0] + [top[0]] + left[:]
    if n <= 5:
        for i in range(2, n + 1):
            a[i - 1] = b[i]
            for j in range(i, n + 1):
                a[j] = mex[a[j - 1]][a[j]]
                cnt[a[j]] += 1
            b[i] = a[i]
            for j in range(i + 1, n + 1):
                b[j] = mex[b[j - 1]][b[j]]
                cnt[b[j]] += 1
        return cnt
    for i in range(2, 6):
        a[i - 1] = b[i]
        for j in range(i, 6):
            a[j] = mex[a[j - 1]][a[j]]
            cnt[a[j]] += 1
        b[i] = a[i]
        for j in range(i + 1, 6):
            b[j] = mex[b[j - 1]][b[j]]
            cnt[b[j]] += 1
    for i in range(5, n):
        cnt[a[5]] += 1
    for i in range(6, n):
        cnt[b[5]] += 1
    return cnt
T = int(input())
for _ in range(T):
    n = int(input())
    top = list(map(int, input().split()))
    left = [int(input()) for _ in range(n - 1)]
    ans = solve(n, top, left)
    print(*ans)


import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    people = [tuple(map(int, input().split())) for _ in range(N)]
    total = sum(max(0, -c) for _, c in people)
    if total == 0:
        print(0)
        continue
    left = []
    right = []
    for x, c in people:
        if x < 0:
            left.append((x, c))
        else:
            right.append((x, c))
    def calc(arr, start):
        return sum(abs(arr[i][0] - arr[i - 1][0]) for i in range(1, len(arr))) + abs(arr[0][0] - start)
    ans = float('inf')
    for split in range(N + 1):
        pass
    pos = [x for x, c in people]
    c = [v for x, v in people]
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i + 1] = prefix[i] + c[i]
    for i in range(N + 1):
        if prefix[i] >= 0 and prefix[N] - prefix[i] <= 0:
            if i == 0:
                cost = abs(pos[N - 1])
            elif i == N:
                cost = abs(pos[0])
            else:
                cost = abs(pos[i - 1]) + abs(pos[N - 1] - pos[i - 1])
            ans = min(ans, cost)
    def greedy(start_idx, end_idx, direction):
        carry = 0
        dist = 0
        prev = 0
        indices = range(start_idx, end_idx, direction)
        for i in indices:
            x, amount = people[i]
            dist += abs(x - prev)
            prev = x
            if amount > 0:
                carry += amount
            else:
                carry += amount
        return dist
    left_need = 0
    right_need = 0
    for x, c in people:
        if x < 0:
            left_need += -c
        else:
            right_need += -c
    def solve_side(indices):
        carry = 0
        distance = 0
        prev = 0
        for i in indices:
            x, c = people[i]
            distance += abs(x - prev)
            prev = x
            carry += c
        return distance
    best = float('inf')
    for first_right in [True, False]:
        carry = 0
        distance = 0
        prev = 0
        visited = set()
        order = []
        if first_right:
            order.extend(range(N - 1, -1, -1))
        else:
            order.extend(range(N))
        for i in order:
            x, c = people[i]
            if c < 0 and carry + c < 0:
                continue
            distance += abs(x - prev)
            prev = x
            carry += c
            visited.add(i)
        if len(visited) == N:
            best = min(best, distance)
    print(best)


T = int(input())
for tc in range(1, T + 1):
    s = input().strip()
    n = len(s)
    h = n // 2
    a = s[:h]
    b = s[-h:]
    if s == s[::-1] and a == a[::-1] and b == b[::-1]:
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")


T = int(input())
MAX = 1500
prime = [True] * (MAX + 1)
prime[0] = prime[1] = False
for i in range(2, int(MAX ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, MAX + 1, i):
            prime[j] = False
for tc in range(1, T + 1):
    n = int(input())
    m = n
    while not prime[m]:
        m += 1
    x = 2 * (m - n)
    if x > n:
        print(f"#{tc} -1")
        continue
    edges = []
    for i in range(1, n + 1):
        edges.append((i, i % n + 1))
    if x == 2:
        edges.append((1, 3))
    else:
        k = x // 2
        for i in range(1, k + 1):
            edges.append((i, i + k))
    print(f"#{tc} {len(edges)}")
    for u, v in edges:
        print(u, v)


import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    parity = 0
    answer = 0
    for i in range(1, N):
        target = i + 1
        if A[i][0] == target:
            current = 0
        else:
            current = 1
        if current != parity:
            answer += 1
            parity = current
    print(answer)


import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    parity = 0
    answer = 0
    for i in range(1, N):
        target = i + 1
        if A[i][0] == target:
            current = 0
        else:
            current = 1
        if current != parity:
            answer += 1
            parity = current
    print(answer)


from math import gcd
T = int(input())
for tc in range(1, T + 1):
    N, PD, PG = map(int, input().split())
    if (PD == 0 and PG != 0) or (PD == 100 and PG != 100):
        print(f"#{tc} Broken")
        continue
    g = gcd(PD, 100)
    d = 100 // g
    if d <= N:
        print(f"#{tc} Possible")
    else:
        print(f"#{tc} Broken")


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [input() for _ in range(N)]
    for i in range(N - 1):
        for j in range(M - 1):
            if grid[i][j] == '#':
                if grid[i + 1][j] == '#' and grid[i][j + 1] == '#' and grid[i + 1][j + 1] == '#':
                    grid[i] = grid[i][:j] + '.' + grid[i][j + 1:]
                    grid[i + 1] = grid[i + 1][:j] + '.' + grid[i + 1][j + 1:]
                else:
                    break
        else:
            continue
        break
    else:
        print(f"#{tc} YES")
        continue
    print(f"#{tc} NO")


T = int(input())
for tc in range(1, T + 1):
    s = input().strip()
    n = len(s)
    half = (n - 1) // 2
    if s != s[::-1]:
        print(f"#{tc} NO")
        continue
    left = s[:half]
    right = s[n - half:]
    if left == left[::-1] and right == right[::-1]:
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")


def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


def havel_hakimi(degrees):
    n = len(degrees)
    arr = [[degrees[i], i] for i in range(n)]
    edges = []

    while True:
        arr.sort(reverse=True)

        if arr[0][0] == 0:
            return edges

        d, v = arr[0]
        arr = arr[1:]

        if d > len(arr):
            return None

        for i in range(d):
            if arr[i][0] <= 0:
                return None

            u = arr[i][1]
            arr[i][0] -= 1
            edges.append((v + 1, u + 1))


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    if n == 3:
        print(f"#{tc} 3")
        print("1 2")
        print("2 3")
        print("3 1")
        continue
    if n == 4:
        print(f"#{tc} 5")
        print("1 2")
        print("1 3")
        print("1 4")
        print("2 3")
        print("2 4")
        continue
    m = n
    while not is_prime(m):
        m += 1
    while True:
        x = m - n
        if x <= n:
            degrees = [4] * x + [2] * (n - x)
            edges = havel_hakimi(degrees)
            if edges is not None and len(edges) == m:
                print(f"#{tc} {m}")
                for u, v in edges:
                    print(u, v)
                break
        m += 1
        while not is_prime(m):
            m += 1


T = int(input())
for tc in range(1, T + 1):
    S = input().strip()
    answer = float('inf')
    for i in range(1, len(S)):
        a = int(S[:i])
        b = int(S[i:])
        answer = min(answer, a + b)
    print(f"#{tc} {answer}")


import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = list(map(int, input().split()))
    max_x = max(queries)
    if max_x <= n:
        result = [a[x - 1] for x in queries]
    else:
        seq = a[:]
        total = sum(seq)
        seen = {}
        i = n
        while i < max_x:
            state = tuple(seq[-n:])
            if state in seen:
                start, length = seen[state]
                cycle_start = start
                cycle_length = length
                break
            seen[state] = (i, 0)
            value = total // n
            seq.append(value)
            total += value - seq[i - n]
            i += 1
            seen[state] = (seen[state][0], i - seen[state][0])
        else:
            cycle_start = cycle_length = 0
        if cycle_length:
            result = []
            for x in queries:
                if x <= n:
                    result.append(a[x - 1])
                elif x < cycle_start + 1:
                    result.append(seq[x - 1])
                else:
                    idx = cycle_start + (x - cycle_start - 1) % cycle_length
                    result.append(seq[idx])
        else:
            result = [seq[x - 1] for x in queries]
    print(f"#{tc}", *result)


import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    if N <= 1:
        print(f"#{tc} {N if 0 <= K else -1}")
        continue
    xs = sorted(x for x, y in points)
    ys = sorted(y for x, y in points)
    def pair_sum(arr):
        n = len(arr)
        prefix = 0
        result = 0
        for i, x in enumerate(arr):
            result += x * i - prefix
            prefix += x
        return result
    total = pair_sum(xs) + pair_sum(ys)
    if total <= K:
        print(f"#{tc} {N}")
        continue
    best = -1
    sx = sum(xs)
    sy = sum(ys)
    for x, y in points:
        pass
    coords = [(x, y) for x, y in points]
    total_x = pair_sum(xs)
    total_y = pair_sum(ys)
    for x, y in coords:
        pass
    dist_sum = [[0] * N for _ in range(N)]
    for i in range(N):
        xi, yi = points[i]
        for j in range(i + 1, N):
            xj, yj = points[j]
            dist = abs(xi - xj) + abs(yi - yj)
            dist_sum[i][j] = dist
    for mask in range(1 << N):
        if N > 20:
            break
        selected = []
        unselected = []
        for i in range(N):
            if mask & (1 << i):
                selected.append(i)
            else:
                unselected.append(i)
        a = 0
        for i in range(len(selected)):
            for j in range(i + 1, len(selected)):
                a += dist_sum[selected[i]][selected[j]]
        b = 0
        for i in range(len(unselected)):
            for j in range(i + 1, len(unselected)):
                b += dist_sum[unselected[i]][unselected[j]]
        if a - b <= K:
            best = max(best, len(selected))
    print(f"#{tc} {best}")


import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    V = list(map(int, input().split()))
    ok = True
    for i in range(N):
        for j in range(N):
            if V[i] != V[V[i] - 1]:
                ok = False
                break
        if not ok:
            break
    if not ok:
        print(f"#{tc} no")
        continue
    A = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            A[i][j] = max(V[i], V[j])
    valid = True
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if A[A[i][j] - 1][k] != A[i][A[j][k] - 1]:
                    valid = False
                    break
            if not valid:
                break
        if not valid:
            break
    if not valid:
        print(f"#{tc} no")
    else:
        print(f"#{tc} yes")
        for row in A:
            print(*row)


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    S = input().strip()
    def booth(s):
        return s[0] in s[-N//2:]
    doubled = S + S
    pi = [0] * (2 * N)
    for i in range(1, 2 * N):
        j = pi[i - 1]
        while j > 0 and doubled[i] != doubled[j]:
            j = pi[j - 1]
        if doubled[i] == doubled[j]:
            j += 1
        pi[i] = j
    answer = 0
    for length in range(N // 2, 0, -1):
        a = S[:length]
        b = S[N - length:]
        if len(a) == len(b):
            if a in (b + b):
                answer = length
                break
    print(f"#{tc} {answer}")


MOD = 1000000007
def resultant(f, g):
    while len(f) > 1 and f[-1] == 0:
        f.pop()
    while len(g) > 1 and g[-1] == 0:
        g.pop()
    result = 1
    while len(f) > 1 or len(g) > 1:
        if len(f) < len(g):
            m = len(f) - 1
            n = len(g) - 1
            if (m * n) & 1:
                result = (-result) % MOD
            f, g = g, f
        m = len(f) - 1
        n = len(g) - 1
        if n == 0:
            return result * pow(g[0], m, MOD) % MOD
        lc = g[-1]
        inv_lc = pow(lc, MOD - 2, MOD)
        r = f[:]
        for i in range(m, n - 1, -1):
            c = r[i] * inv_lc % MOD
            if c:
                start = i - n
                for j in range(n + 1):
                    r[start + j] = (r[start + j] - c * g[j]) % MOD
        degree = len(r) - 1
        while degree > 0 and r[degree] == 0:
            degree -= 1
        r = r[:degree + 1]
        result = result * pow(lc, m - degree, MOD) % MOD
        f, g = r, g
    return result
def permutation_sign(p):
    n = len(p)
    visited = [False] * n
    cycles = 0
    for i in range(n):
        if not visited[i]:
            cycles += 1
            cur = i
            while not visited[cur]:
                visited[cur] = True
                cur = p[cur]
    return -1 if (n - cycles) & 1 else 1
TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    A = list(map(int, input().split()))
    P = [x - 1 for x in map(int, input().split())]
    visited = [False] * N
    order = []
    cycle_count = 0
    for i in range(N):
        if not visited[i]:
            cycle_count += 1
            cur = i
            while not visited[cur]:
                visited[cur] = True
                order.append(cur)
                cur = P[cur]
    if cycle_count > 1:
        print(f"#{tc} 0")
        continue
    F = [A[i] % MOD for i in order]
    G = [MOD - 1] + [0] * (N - 1) + [1]
    det = resultant(F, G)
    det = det * permutation_sign(order) % MOD
    print(f"#{tc} {det}")


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    print(f"#{tc} {'Alice' if N % 2 == 0 else 'Bob'}")


import sys
input = sys.stdin.readline
TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    if N <= 3:
        result = "TAK"
    else:
        p0 = points[0]
        p1 = points[1]
        idx = 2
        while idx < N:
            p2 = points[idx]
            ax = p1[0] - p0[0]
            ay = p1[1] - p0[1]
            az = p1[2] - p0[2]
            bx = p2[0] - p0[0]
            by = p2[1] - p0[1]
            bz = p2[2] - p0[2]
            nx = ay * bz - az * by
            ny = az * bx - ax * bz
            nz = ax * by - ay * bx
            if nx != 0 or ny != 0 or nz != 0:
                break
            idx += 1
        if idx == N:
            result = "TAK"
        else:
            result = "TAK"
            for i in range(N):
                x, y, z = points[i]
                if nx * (x - p0[0]) + ny * (y - p0[1]) + nz * (z - p0[2]) != 0:
                    result = "NIE"
                    break
    print(f"#{tc} {result}")


