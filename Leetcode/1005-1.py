import sys
input = sys.stdin.readline
from collections import deque
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    indeg = [0] * (n+1)
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indeg[y] += 1
    w = int(input())
    q = deque()
    dp = [0] * (n+1)
    for i in range(1, n+1):
        if indeg[i] == 0:
            q.append(i)
            dp[i] = d[i]
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            dp[nxt] = max(dp[nxt], dp[cur] + d[nxt])
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    print(dp[w])
