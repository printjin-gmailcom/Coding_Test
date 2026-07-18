T = int(input())
for test_case in range(1, T + 1):
    n = input()
    if "9" in n:
        print(f"#{test_case} Yes")
    else:
        print(f"#{test_case} No")


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    total = 0
    for _ in range(N):
        L, R = map(int, input().split())
        total += R - L + 1
    print(f"#{test_case} {total}")
  

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    s = set()
    for _ in range(n):
        x = int(input())
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    print(f"#{tc} {len(s)}")


from itertools import permutations

INF = 10 ** 18

T = int(input())
for tc in range(1, T + 1):
    N, M, R = map(int, input().split())
    towns = list(map(int, input().split()))
    dist = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        dist[i][i] = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        if c < dist[a][b]:
            dist[a][b] = c
            dist[b][a] = c
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    ans = INF
    for order in permutations(towns):
        total = 0
        for i in range(R - 1):
            total += dist[order[i]][order[i + 1]]
        ans = min(ans, total)
    print(f"#{tc} {ans}")

