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

