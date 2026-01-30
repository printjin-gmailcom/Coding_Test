def solution(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char) 
    if stack:
        return 0
    else:
        return 1 


def solution(n, a, b):
    answer = 0
    while a != b:
        a = (a + 1) // 2 
        b = (b + 1) // 2 
        answer += 1  
    return answer


def solution(strs, t):
    n = len(t)
    INF = 10**9
    dp = [INF] * (n + 1)
    dp[0] = 0
    strs_set = set(strs)
    max_len = max(len(s) for s in strs)
    for i in range(n):
        if dp[i] == INF:
            continue
        for l in range(1, max_len + 1):
            if i + l <= n and t[i:i+l] in strs_set:
                dp[i + l] = min(dp[i + l], dp[i] + 1)
    return dp[n] if dp[n] != INF else -1
