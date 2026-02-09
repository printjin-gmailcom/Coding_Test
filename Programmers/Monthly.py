def solution(n, m, x, y, queries):
    min_row, max_row = x, x
    min_col, max_col = y, y
    for command, dx in reversed(queries):
        if command == 0: 
            max_col = min(m - 1, max_col + dx)
            if min_col != 0:
                min_col += dx
        elif command == 1:  
            min_col = max(0, min_col - dx)
            if max_col != m - 1:
                max_col -= dx
        elif command == 2:  
            max_row = min(n - 1, max_row + dx)
            if min_row != 0:
                min_row += dx
        elif command == 3:  
            min_row = max(0, min_row - dx)
            if max_row != n - 1:
                max_row -= dx
        if min_row >= n or max_row < 0 or min_col >= m or max_col < 0:
            return 0
    return (max_row - min_row + 1) * (max_col - min_col + 1)


def solution(n, left, right):
    result = []
    for idx in range(left, right + 1):
        row = idx // n
        col = idx % n
        result.append(max(row, col) + 1)
    return result


def solution(absolutes, signs):
    return sum(absolutes[i] if signs[i] else -absolutes[i] for i in range(len(absolutes)))


def solution(numbers):
    all_numbers = set(range(10))
    missing_numbers = all_numbers - set(numbers)
    return sum(missing_numbers)


def solution(n):
    answer = 0
    for i in range(1, n):
        if n % i == 1:
            answer = i
            break
    return answer


def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += int(a[i]*b[i])
    return answer


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        ans = 0
        for j in range(1, i + 1): 
            if i % j == 0: 
                ans += 1  
        if ans % 2 == 0: 
            answer += i 
        else:
            answer -= i
    return answer


def solution(s):
    count = 0 
    zero = 0 
    while s != "1": 
        zero += s.count('0') 
        s = s.replace('0', '') 
        s = bin(len(s))[2:] 
        count += 1  
    return [count, zero]  


def solution(n):
    ternary = ""
    while n > 0:
        n, r = divmod(n, 3) 
        ternary += str(r)    
    return int(ternary, 3) 


from itertools import combinations
def solution(numbers):
    answer = set()  
    for a, b in combinations(numbers, 2):
        answer.add(a + b)
    return sorted(answer)


def solution(numbers): 
    return [((num ^ (num+1)) >> 2) + num + 1 for num in numbers]


def solution(s):
    answer = []
    for x in s:
        stack = []
        cnt = 0
        for c in x:
            stack.append(c)
            if len(stack) >= 3 and ''.join(stack[-3:]) == '110':
                stack.pop()
                stack.pop()
                stack.pop()
                cnt += 1
        i = len(stack) - 1
        while i >= 0 and stack[i] == '1':
            i -= 1
        result = ''.join(stack[:i+1]) + '110'*cnt + ''.join(stack[i+1:])
        answer.append(result)
    return answer


def solution(a):
    n = len(a)
    if n <= 2:
        return n  
    left_min = [0] * n
    right_min = [0] * n
    left_min[0] = a[0]
    for i in range(1, n):
        left_min[i] = min(left_min[i-1], a[i])
    right_min[n-1] = a[n-1]
    for i in range(n-2, -1, -1):
        right_min[i] = min(right_min[i+1], a[i])
    answer = 0
    for i in range(n):
        if i == 0 or i == n-1:
            answer += 1
        elif a[i] <= left_min[i-1] or a[i] <= right_min[i+1]:
            answer += 1
    return answer


from collections import Counter
def solution(a):
    count = Counter(a)
    max_len = 0
    for v in count:
        if count[v] <= max_len // 2:
            continue
        pairs = 0
        i = 0
        n = len(a)
        while i < n - 1:
            if (a[i] == v and a[i+1] != v) or (a[i] != v and a[i+1] == v):
                pairs += 1
                i += 2 
            else:
                i += 1
        max_len = max(max_len, pairs * 2)
    return max_len


import sys
sys.setrecursionlimit(10**9)
def solution(a, edges):
    if sum(a) != 0:
        return -1
    n = len(a)
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    visited = [False]*n
    ans = 0
    def dfs(x):
        nonlocal ans
        visited[x] = True
        s = a[x]
        for nx in g[x]:
            if not visited[nx]:
                s_child = dfs(nx)
                ans += abs(s_child)
                s += s_child
        return s
    if dfs(0) != 0:
        return -1
    return ans


def solution(a):
    MOD = 10000019
    n = len(a)
    m = len(a[0])
    col_sums = [0] * m
    for row in a:
        for j, v in enumerate(row):
            col_sums[j] += v
    C = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        C[i][0] = C[i][i] = 1
        for j in range(1, i):
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD
    dp = [0] * (n + 1)
    dp[0] = 1
    for c in col_sums:
        new_dp = [0] * (n + 1)
        for k in range(n + 1):
            if dp[k] == 0:
                continue
            for x in range(max(0, c - (n - k)), min(c, k) + 1):
                nk = k + c - 2 * x
                ways = (C[k][x] * C[n - k][c - x]) % MOD
                new_dp[nk] = (new_dp[nk] + dp[k] * ways) % MOD
        dp = new_dp
    return dp[0]


from collections import defaultdict
import sys; sys.setrecursionlimit(1000000)
def dfs(u, A, d, visited):
    if all(v in visited for v in A[u]):
        return u, d, 1
    farthestnode, maxdepth, maxdepthcnt = None, -1, 0
    for v in A[u]:
        if v in visited:
            continue
        visited.add(v)
        node, depth, depthcnt = dfs(v, A, d+1, visited)
        if depth > maxdepth:
            farthestnode, maxdepth, maxdepthcnt = node, depth, depthcnt
        elif depth == maxdepth:
            maxdepthcnt += depthcnt
    return farthestnode, maxdepth, maxdepthcnt
def solution(n, edges):
    A = defaultdict(list)
    for u, v in edges:
        A[u].append(v)
        A[v].append(u)
    visited = set()
    visited.add(1)
    farthest, _, _ = dfs(1, A, 0, visited)
    visited = set()
    visited.add(farthest)
    farthest, diameter, cnt1 = dfs(farthest, A, 0, visited)
    visited = set()
    visited.add(farthest)
    farthest, diameter, cnt2 = dfs(farthest, A, 0, visited)
    if cnt1 == 1 and cnt2 == 1:
        return diameter - 1
    else:
        return diameter
