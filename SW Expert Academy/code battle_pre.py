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
    
