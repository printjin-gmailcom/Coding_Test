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
