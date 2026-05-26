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
