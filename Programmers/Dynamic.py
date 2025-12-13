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


def solution(money):
    n = len(money)
        if n == 3:
        return max(money)
        dp1 = [0] * n
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    for i in range(2, n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
    dp2 = [0] * n
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    return max(dp1[-2], dp2[-1])


def solution(arr):
    n = (len(arr) + 1) // 2
    nums = [int(arr[i * 2]) for i in range(n)]
    ops = [arr[i * 2 + 1] for i in range(n - 1)]
    dp_max = [[-10**18] * n for _ in range(n)]
    dp_min = [[10**18] * n for _ in range(n)]
    for i in range(n):
        dp_max[i][i] = nums[i]
        dp_min[i][i] = nums[i]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                if ops[k] == '+':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k + 1][j])
                else:
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k + 1][j])
    return dp_max[0][n - 1]
