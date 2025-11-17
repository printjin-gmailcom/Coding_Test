import math
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    d = y - x
    n = int(math.sqrt(d))
    if n * n == d:
        print(2 * n - 1)
    elif n * n < d <= n * n + n:
        print(2 * n)
    else:
        print(2 * n + 1)
