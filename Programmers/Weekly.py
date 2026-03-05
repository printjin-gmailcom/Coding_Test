def solution(price, money, count):
    total = 0
    for i in range(1, count + 1): 
        total += price * i 
    if total > money:  
        answer = total - money 
    else:
        answer = 0  
    return answer


def solution(arr):
    def compress(x, y, size):
        start = arr[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != start:
                    size //= 2
                    a1 = compress(x, y, size)
                    a2 = compress(x, y + size, size)
                    a3 = compress(x + size, y, size)
                    a4 = compress(x + size, y + size, size)
                    return [a1[0] + a2[0] + a3[0] + a4[0], a1[1] + a2[1] + a3[1] + a4[1]]
        if start == 0:
            return [1, 0]
        else:
            return [0, 1]
    return compress(0, 0, len(arr))


def solution(s):
    def is_valid(brackets):
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for ch in brackets:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        return not stack
    n = len(s)
    count = 0
    for i in range(n):
        rotated = s[i:] + s[:i]
        if is_valid(rotated):
            count += 1
    return count


def solution(n):
    triangle = [[0] * (i + 1) for i in range(n)]
    num = 1
    x, y = -1, 0
    
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:  
                x += 1
            elif i % 3 == 1:  
                y += 1
            else: 
                x -= 1
                y -= 1
            triangle[x][y] = num
            num += 1
    answer = []
    for row in triangle:
        answer.extend(row)
    return answer


def solution(grid):
    n = len(grid)
    m = len(grid[0])
    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    change = {
        'S': [0, 1, 2, 3],
        'L': [3, 0, 1, 2],
        'R': [1, 2, 3, 0]}
    answer = []
    for i in range(n):
        for j in range(m):
            for d in range(4):
                if visited[i][j][d]:
                    continue 
                x, y, dir = i, j, d
                cnt = 0
                while not visited[x][y][dir]:
                    visited[x][y][dir] = True
                    cnt += 1
                    dir = change[grid[x][y]][dir]
                    x = (x + dx[dir]) % n
                    y = (y + dy[dir]) % m
                if cnt > 0:
                    answer.append(cnt)
    return sorted(answer)


def solution(a, b, g, s, w, t):
    left, right = 0, 10**16
    answer = right
    while left <= right:
        mid = (left + right) // 2
        total_gold = 0
        total_silver = 0
        total = 0
        for i in range(len(g)):
            time = t[i]
            weight = w[i]
            cnt = mid // (2 * time)
            if mid % (2 * time) >= time:
                cnt += 1
            max_move = cnt * weight
            gold = min(g[i], max_move)
            silver = min(s[i], max_move)
            total_gold += gold
            total_silver += silver
            total += min(g[i] + s[i], max_move)
        if total_gold >= a and total_silver >= b and total >= a + b:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


def solution(line):
    points = set()
    INF = 10**18
    min_x, min_y = INF, INF
    max_x, max_y = -INF, -INF
    n = len(line)
    for i in range(n):
        A, B, C = line[i]
        for j in range(i + 1, n):
            D, E, F = line[j]
            denom = A * E - B * D
            if denom == 0:
                continue
            x_num = B * F - C * E
            y_num = C * D - A * F
            if x_num % denom != 0 or y_num % denom != 0:
                continue
            x = x_num // denom
            y = y_num // denom
            points.add((x, y))
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    grid = [['.'] * width for _ in range(height)]
    for x, y in points:
        grid[max_y - y][x - min_x] = '*'
    return [''.join(row) for row in grid]
   

def Calc(s_len, e_len):
    if s_len > e_len:
        N, K = e_len, s_len
    else:
        N, K = s_len, e_len
    if N == 1:
        return N * K
    return ((N + K + 1) * (N + 1) * N // 2) - ((N + 1) * N * (2 * N + 1) // 3)
def MaxBeauty(size):
    if size == 1:
        return 0
    return (size * size * (size - 1) // 2) - ((size - 1) * size * (2 * size - 1) // 6)
def solution(s):
    n = len(s)
    if n == 0:
        return 0
    answer = MaxBeauty(n)
    nodes = []
    cur_char = s[0]
    length = 1
    for c in s[1:]:
        if c == cur_char:
            length += 1
        else:
            nodes.append((cur_char, length))
            cur_char = c
            length = 1
    nodes.append((cur_char, length))
    if len(nodes) == 1:
        return 0
    tables = [{} for _ in range(26)]
    for ch, seg_len in nodes:
        idx = ord(ch) - ord('a')
        answer -= MaxBeauty(seg_len)
        table = tables[idx]
        for prev_len, cnt in table.items():
            answer -= cnt * Calc(prev_len, seg_len)
        table[seg_len] = table.get(seg_len, 0) + 1
    return answer


import sys
sys.setrecursionlimit(400000)
from collections import defaultdict
def set_depth_subtree(node, prev):
    sub_trees = []
    depths = []
    for child in graph[node]:
        if child == prev:
            continue
        set_depth_subtree(child, node)
        sub_trees.append((sub_tree[child], child))
        depths.append((depth[child], child))
        depth[node] = max(depth[node], depth[child] + 1)
    sub_trees.sort(reverse=True)
    depths.sort(reverse=True)
    if len(sub_trees) >= 2:
        if sub_trees[0][1] != depths[0][1]:
            sub_tree[node] = sub_trees[0][0] + depths[0][0] + 1
        else:
            sub_tree[node] = max(
                sub_trees[0][0] + depths[1][0] + 1,
                sub_trees[1][0] + depths[0][0] + 1)
    elif len(sub_trees) == 1:
        sub_tree[node] = sub_trees[0][0] + 1
def DFS(node, prev, height):
    global answer
    sub_trees = []
    depths = []
    for child in graph[node]:
        if child == prev:
            continue
        sub_trees.append((sub_tree[child], child))
        depths.append((depth[child], child))
    sub_trees.sort(reverse=True)
    depths.sort(reverse=True)
    for child in graph[node]:
        if child == prev:
            continue
        next_height = height + 1
        if depths[0][1] != child:
            next_height = max(next_height, depths[0][0] + 2)
        elif len(depths) >= 2 and depths[0][1] == child:
            next_height = max(next_height, depths[1][0] + 2)
        DFS(child, node, next_height)
    if len(sub_trees) >= 3:
        answer = max(
            answer,
            sub_trees[0][0] + sub_trees[1][0] + height,
            sub_trees[0][0] + sub_trees[2][0] + depths[1][0] + 1,
            sub_trees[0][0] + sub_trees[1][0] + depths[2][0] + 1)
    elif len(sub_trees) == 2:
        answer = max(
            answer,
            sub_trees[0][0] + sub_trees[1][0] + height)
def solution(t):
    global answer, N, graph, sub_tree, depth
    N = len(t) + 1
    graph = defaultdict(list)
    sub_tree = [1] * N
    depth = [1] * N
    answer = 0
    for v1, v2 in t:
        graph[v1].append(v2)
        graph[v2].append(v1)
    set_depth_subtree(0, -1)
    DFS(0, -1, 1)
    return answer


import math
import bisect
MOD = int(1e9 + 7)
def binary_search(arr, x):
    idx = bisect.bisect_left(arr, x)
    if idx == 0 and arr[idx] != x:
        return -1
    elif idx == len(arr):
        return -1
    else:
        return idx
def solve(b):
    maxb, n = max(b), len(b)
    ps = [0, b[0]]
    for i in range(1, n):
        ps.append(ps[-1] + b[i])
    maxe = math.ceil(math.log2(ps[-1]))
    dp = [[0] * (maxe + 1) for _ in range(n)]
    dp[0][0] = 1
    for i in range(1, n):
        dp[i][0] = sum(dp[i-1])
        for e in range(1, maxe + 1):
            if dp[i][e-1] == 0:
                continue
            target = ps[i + 1] - b[i] * 2**(e-1)
            jhalf = binary_search(ps, target)
            if jhalf == -1:
                continue
            eprime = math.log2(b[i] / b[jhalf - 1]) + (e - 1)
            if not eprime.is_integer() or eprime < 0:
                continue
            if not dp[jhalf - 1][int(eprime)] > 0:
                continue.
            target = ps[i + 1] - b[i] * 2**e
            jfull = binary_search(ps, target)
            if jfull == -1:
                continue
            if jfull == 0:
                dp[i][e] = 1
            else:
            	dp[i][e] = sum(dp[jfull - 1]) % MOD
    return sum(dp[-1]) % MOD
def solution(a, s):
    answer = []
    start = 0
    for l in s:
        b = a[start:start+l]
        answer.append(solve(b))
        start += l
    return answer
