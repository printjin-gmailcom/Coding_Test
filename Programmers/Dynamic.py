def solution(N, number):
    if N == number:
        return 1
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
    for i in range(1, 9):
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i-j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)
        if number in dp[i]:
            return i
    return -1


def solution(triangle):
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]


def solution(m, n, puddles):
    MOD = 1000000007
    dp = [[0] * (m+1) for _ in range(n+1)]
    for x, y in puddles:
        dp[y][x] = -1
    dp[1][1] = 1  
    for y in range(1, n+1):
        for x in range(1, m+1):
            if dp[y][x] == -1:
                dp[y][x] = 0
                continue
            if x > 1:
                dp[y][x] += dp[y][x-1]
            if y > 1:
                dp[y][x] += dp[y-1][x]
            dp[y][x] %= MOD
    return dp[n][m]
