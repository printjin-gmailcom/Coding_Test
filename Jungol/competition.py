A = int(input())
print(A // 5)


X = int(input())
cycle = X // 2
result = cycle
if X % 2 == 1:
    result += 3
print(result)


N = int(input())
S = input()
result = []
for c in S:
    if c == 'J':
        result.append('O')
    elif c == 'O':
        result.append('I')
    else:
        result.append('J')
print(''.join(result))


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = 0
for a in A:
    for b in B:
        result += (a + b) * max(a, b)
print(result)


T = int(input())
V = int(input())
print(T * V)


P, Q = map(int, input().split())
A, B = map(int, input().split())
if Q <= P:
    print(Q * A)
else:
    print(P * A + (Q - P) * B)


N = int(input())
S = input()
T = input()


j = 0
h = 0
for i in range(N):
    if S[i] == T[i]:
        continue
    if (S[i] == 'R' and T[i] == 'S') or (S[i] == 'S' and T[i] == 'P') or (S[i] == 'P' and T[i] == 'R'):
        j += 1
    else:
        h += 1
print(j, h)


N = int(input())
A = list(map(int, input().split()))
for _ in range(N - 1):
    B = []
    for i in range(len(A) - 1):
        B.append(A[i] + A[i + 1])
    print(*B)
    A = B


A = int(input())
B = int(input())
print(A * 1000 + B * 10000)


A = int(input())
B = int(input())
C = int(input())
if A + B + C <= 21:
    print(1)
else:
    print(0)


N = int(input())
A = int(input())
B = int(input())
cnt = 0
for i in range(1, N + 1):
    if (i % A == 0) ^ (i % B == 0):
        cnt += 1
print(cnt)


N = int(input())
S = input()
for d in range(1, N):
    if N % d == 0:
        if S == S[:d] * (N // d):
            print("Yes")
            break
else:
    print("No")


s = input()
result = ""
for i in range(len(s)):
    result += s[i]
    if i == 0 or i == 1 or i == 4 or i == len(s) - 1:
        result += "!"
print(result)


n, m, k = map(int, input().split())
priority = []
if m > 0:
    priority = list(map(int, input().split()))
count = m
for i in range(1, k):
    if i not in priority:
        count += 1
print(count + 1)


def pair(x):
    return x + 1 if x % 2 == 1 else x - 1
n = int(input())
a, b = map(int, input().split())
seats = []
for _ in range(a - 1):
    seats.append(int(input()))
occupied = set(seats)
if a < b:
    possible = False
    for s in range(1, 2 * n + 1):
        if s not in occupied and pair(s) in occupied:
            possible = True
            break
    print("Yena" if possible else "Chaewon")
else:
    chaewon_seat = seats[b - 1]
    blocked = pair(chaewon_seat)
    possible = False
    for s in range(1, 2 * n + 1):
        if s not in occupied and s != blocked:
            possible = True
            break
    print("Yena" if possible else "Chaewon")


n = int(input())
s = input()
INF = -10**18
dp = [[INF] * 3 for _ in range(n)]
if s[0] != 'X':
    dp[0][0] = 1
if s[0] != 'O':
    dp[0][1] = 0
for i in range(1, n):
    if s[i] != 'X':
        for j in range(1, 3):
            if dp[i - 1][j] != INF:
                dp[i][0] = max(dp[i][0], dp[i - 1][j] + 1)
    if s[i] != 'O':
        if dp[i - 1][0] != INF:
            dp[i][1] = max(dp[i][1], dp[i - 1][0])
        if dp[i - 1][1] != INF:
            dp[i][2] = max(dp[i][2], dp[i - 1][1])
ans = max(dp[n - 1])
print(ans if ans != INF else -1)


import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
w = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
parity = [-1] * (n + 1)
q = deque([1])
parity[1] = 0
while q:
    now = q.popleft()
    for nxt in graph[now]:
        if parity[nxt] == -1:
            parity[nxt] = parity[now] ^ 1
            q.append(nxt)
add = [0, 0]
Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, i, v = query
        add[parity[i]] += v
    else:
        _, i = query
        print(w[i] + add[parity[i]])


import sys
from functools import lru_cache
input = sys.stdin.readline
patterns = []
for a in range(4):
    for b in range(3):
        for c in range(2):
            if 3*a + 5*b + 7*c <= 10:
                patterns.append((a,b,c,a+b+c))
def dp(a,b,c,k):
    if k == 0:
        return 0
    best = 0
    for x,y,z,val in patterns:
        if a >= x and b >= y and c >= z:
            best = max(best, val + dp(a-x, b-y, c-z, k-1))
    return best
T = int(input())
for _ in range(T):
    A,B,C = map(int,input().split())
    print(dp(A,B,C,5))


import sys
from collections import deque
input = sys.stdin.readline
MOD = 10**9 + 7
N, M = map(int, input().split())
dir_graph = [[] for _ in range(N + 1)]
undir_graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(M):
    A, B, C = map(int, input().split())
    dir_graph[A].append(C)
    dir_graph[B].append(C)
    indegree[C] += 2
    undir_graph[A].append(B)
    undir_graph[B].append(A)
q = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
cnt = 0
while q:
    x = q.popleft()
    cnt += 1
    for nxt in dir_graph[x]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)
if cnt != N:
    print(0)
    sys.exit()
color = [-1] * (N + 1)
components = 0
for i in range(1, N + 1):
    if color[i] != -1:
        continue
    components += 1
    q = deque([i])
    color[i] = 0
    while q:
        x = q.popleft()
        for nxt in undir_graph[x]:
            if color[nxt] == -1:
                color[nxt] = color[x] ^ 1
                q.append(nxt)
            elif color[nxt] == color[x]:
                print(0)
                sys.exit()
print(pow(2, components, MOD))


n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    left = B[i] * A[ans]
    right = B[ans] * A[i]
    if left > right:
        ans = i
    elif left == right:
        ans = i
print(ans + 1)


import sys
input = sys.stdin.readline
n = int(input())
arr = map(int, input().split())
odd = 0
for x in arr:
    odd += x & 1
even = n - odd
if odd > even and ((odd - even) & 1):
    print("myongjin")
else:
    print("hambak")


import sys
input = sys.stdin.readline
cand = ["MUPC", "MJUPC", "MPC", "MJPC"]
cnt = {x: 0 for x in cand}
n = int(input())
for _ in range(n):
    s = input().strip()
    if s not in cnt:
        s = "MUPC"
    cnt[s] += 1
mx = max(cnt.values())
res = [k for k, v in cnt.items() if v == mx]
if len(res) > 1:
    print("REVOTE")
else:
    print(res[0])


import sys
input = sys.stdin.readline
N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
mx = max(A)
base = mx - 20
freq = [0] * 21
for a in A:
    freq[a - base] += 1
total = 0
for i in range(21):
    total += freq[i] * (1 << i)
need = P * total
sel = 0
cnt = 0
for i in range(20, -1, -1):
    v = 1 << i
    f = freq[i]
    if sel * Q >= need:
        print(cnt)
        break
    if (sel + f * v) * Q < need:
        sel += f * v
        cnt += f
    else:
        rem = need - sel * Q
        t = (rem + v * Q - 1) // (v * Q)
        print(cnt + t)
        break


from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
mx = 0
trigger = [False] * n
for i, x in enumerate(a):
    if x > mx:
        mx = x
        trigger[i] = True
d = deque()
rev = False
for i in range(n - 1, -1, -1):
    if d:
        if not rev:
            d.appendleft(d.pop())
        else:
            d.append(d.popleft())
    if trigger[i]:
        rev ^= True
    if not rev:
        d.appendleft(a[i])
    else:
        d.append(a[i])
if not rev:
    print(*d)
else:
    print(*reversed(d))


import sys
from heapq import heappush, heappop
input = sys.stdin.readline
N = int(input())
adj = [[] for _ in range(N + 1)]
deg = [0] * (N + 1)
for _ in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    deg[u] += 1
    deg[v] += 1
B = 450
heavy_nodes = []
heavy_id = [-1] * (N + 1)
for i in range(1, N + 1):
    if deg[i] >= B:
        heavy_id[i] = len(heavy_nodes)
        heavy_nodes.append(i)
H = len(heavy_nodes)
heavy_heap = [[] for _ in range(H)]
heavy_set = {}
stay = [0] * (N + 1)
heavy_adj = [[] for _ in range(N + 1)]
for hidx, h in enumerate(heavy_nodes):
    heavy_set[h] = set(adj[h])
    for v in adj[h]:
        heappush(heavy_heap[hidx], (0, v))
        heavy_adj[v].append(hidx)
cur = 1
Q = int(input())
for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        u = cur
        if deg[u] < B:
            best_v = -1
            best_w = None
            for v in adj[u]:
                w = stay[v]
                if best_w is None or w < best_w or (w == best_w and v < best_v):
                    best_w = w
                    best_v = v
            cur = best_v
        else:
            hidx = heavy_id[u]
            hp = heavy_heap[hidx]
            while hp and hp[0][0] != stay[hp[0][1]]:
                heappop(hp)
            cur = hp[0][1]
    elif q[0] == '2':
        x = int(q[1])
        u = cur
        ok = False
        if deg[u] < B:
            for v in adj[u]:
                if v == x:
                    ok = True
                    break
        else:
            ok = x in heavy_set[u]
        if ok:
            cur = x
    else:
        t = int(q[1])
        stay[cur] += t
        nw = stay[cur]
        for hidx in heavy_adj[cur]:
            heappush(heavy_heap[hidx], (nw, cur))
print(cur)


import sys
MOD = 1000000007
N, K, L, R = map(int, sys.stdin.readline().split())
f = [0] * (R + 1)
f[0] = 1
p = 1
for i in range(1, min(R, K - 1) + 1):
    p = p * N % MOD
    f[i] = p
if K <= R:
    p = p * N % MOD
    f[K] = (p - N) % MOD
    for i in range(K + 1, R + 1):
        f[i] = (N * f[i - 1] - (N - 1) * f[i - K]) % MOD
ans = 0
for i in range(L, R + 1):
    ans += f[i]
print(ans % MOD)


import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
S = sum(a)
mod = 2 * N
D0 = (S - N * a[0]) % mod
for x in a[1:]:
    if (S - N * x) % mod != D0:
        print(-1)
        sys.exit()
if D0 & 1:
    print(-1)
    sys.exit()
L = 0
for x in a:
    D = S - N * x
    if D > 0:
        L = max(L, (D + 1) // 2)
c = D0 // 2
if c >= L:
    print(c)
else:
    print(c + ((L - c + N - 1) // N) * N)


from collections import Counter
n = int(input())
s = input().strip()
m = int(input())
t = input().strip()
target = "ICPC"
i = 0
need = Counter()
for c in target:
    if i < len(s) and s[i] == c:
        i += 1
    else:
        need[c] += 1
have = Counter(t)
ok = True
for c, cnt in need.items():
    if have[c] < cnt:
        ok = False
        break
print("m4us happy" if ok else "m4us sad")


A, B, C = map(int, input().split())
H = int(input())
ans = A + B + C
for mask in range(8):
    hp = H
    t = 0
    arr = [A, B, C]
    for i in range(3):
        if mask & (1 << i):
            hp -= arr[i] // 2
            t += arr[i] // 2
        else:
            t += arr[i]
    if hp >= 1:
        ans = min(ans, t)
print(ans)


n = int(input())
t = input().strip()
cream = 0
jam = 0
cur = []
for ch in t:
    if ch == 'S':
        if cur:
            runs = []
            cnt = 1
            for i in range(1, len(cur)):
                if cur[i] == cur[i - 1]:
                    cnt += 1
                else:
                    runs.append(cur[i - 1])
                    cnt = 1
            runs.append(cur[-1])
            if len(runs) == 2:
                if runs[0] == 'C' and runs[1] == 'J':
                    cream += 1
                elif runs[0] == 'J' and runs[1] == 'C':
                    jam += 1
        cur = []
    else:
        cur.append(ch)
print(cream)
print(jam)


n = int(input())
t = input().strip()
runs = []
i = 0
while i < n:
    j = i
    while j < n and t[j] == t[i]:
        j += 1
    runs.append((t[i], j - i))
    i = j
m = len(runs)
take = [0] * m
first = None
second = None
for i in range(m - 1, -1, -1):
    c, length = runs[i]
    if first is None:
        take[i] = 1
        first = c
        second = None
    elif c != first:
        take[i] = 1 if first < c else length
        first, second = c, first
    else:
        take[i] = 1 if (second is None or second < c) else length
ans = []
for (c, _), x in zip(runs, take):
    ans.append(c * x)
print("".join(ans))


n = int(input())
s = input().strip()
def solve(start):
    prev = 0
    cnt = 0
    for i in range(n):
        target = (start + i) & 1
        cur = (ord(s[i]) - 48) ^ target
        if cur == 1 and prev == 0:
            cnt += 1
        prev = cur
    return cnt
print(min(solve(0), solve(1)))


import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
s = sum(a)
t = sum((n - 1 - i) * a[i] for i in range(n - 1))
def check():
    return s % n == 0 and 2 * t == (n - 1) * s
ans = ["Yes" if check() else "No"]
q = int(input())
for _ in range(q):
    idx, x = map(int, input().split())
    idx -= 1
    diff = x - a[idx]
    s += diff
    if idx < n - 1:
        t += (n - 1 - idx) * diff
    a[idx] = x
    ans.append("Yes" if check() else "No")
sys.stdout.write("\n".join(ans))


import sys
from collections import defaultdict
input = sys.stdin.readline
n, m, q = map(int, input().split())
edges = []
deg = [0] * n
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((u, v))
    deg[u] += 1
    deg[v] += 1
cnt = [defaultdict(int) for _ in range(n)]
for u, v in edges:
    cnt[u][deg[v]] += 1
    cnt[v][deg[u]] += 1
ans = defaultdict(int)
out = []
for _ in range(q):
    qry = list(map(int, input().split()))
    if qry[0] == 1:
        _, i, x = qry
        i -= 1
        for d, c in cnt[i].items():
            ans[d] += x * c
    else:
        _, d = qry
        out.append(str(ans[d]))
sys.stdout.write("\n".join(out))


import sys
MOD = 1000000007
input = sys.stdin.readline
n, m = map(int, input().split())
basis_v = [0] * 20
def insert_basis(basis, x):
    for b in range(19, -1, -1):
        if (x >> b) & 1:
            if basis[b]:
                x ^= basis[b]
            else:
                basis[b] = x
                return True
    return False
r = 0
for _ in range(n):
    s = input().strip()
    mask = int(s, 2)
    if insert_basis(basis_v, mask):
        r += 1
k = (m + 1) // 2
basis_union = basis_v[:]
rank_union = r
for i in range(k):
    j = m - 1 - i
    mask = 0
    mask |= 1 << i
    if j != i:
        mask |= 1 << j
    if insert_basis(basis_union, mask):
        rank_union += 1
d = r + k - rank_union
exp = n - r + d
print((pow(2, exp, MOD) - 1) % MOD)


n = int(input())
if n % 2 == 1:
    m = (n + 1) // 2
    ans = []
    for k in range(1, m):
        ans.extend([-k, k])
    ans.append(0)
else:
    m = n // 2
    ans = []
    for k in range(1, m):
        ans.extend([-k, k])
    ans.extend([0, -m])
print(*ans)


