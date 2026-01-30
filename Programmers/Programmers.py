def count_paid_employees(n, timelogs, startday, time):
    paid_count = 0
    for i in range(n):
        paid = True
        for day in range(7):
            current_day = (startday + day) % 7
            if current_day in [5, 6]:
                continue
            if timelogs[i][day] > time[i] + 10:
                paid = False
                break
        if paid:
            paid_count += 1
    return paid_count
n = 2
timelogs = [[510, 500, 510, 500, 510, 500, 600], [700, 620, 510, 500, 700, 705, 659]]
startday = 5
time = [500, 700]
result = count_paid_employees(n, timelogs, startday, time)
print(result)


from itertools import combinations
def find_real_answer(n, tries, ans):
    possible_answers = set(combinations(range(1, n+1), len(ans)))
    for attempt, count in zip(tries, ans):
        new_possible_answers = set()
        for candidate in possible_answers:
            if len(set(candidate) & set(attempt)) == count:
                new_possible_answers.add(candidate)
        possible_answers = new_possible_answers
    return possible_answers, len(possible_answers)
n = 8
tries = [[1, 2, 3, 4, 5], [2, 5, 6, 7, 8]]
ans = [2, 1]
result, count = find_real_answer(n, tries, ans)
print(result, count)


def count_remaining_items(warehouse, requests):
    n, m = len(warehouse), len(warehouse[0])
    def is_edge(x, y):
        return x == 0 or x == n-1 or y == 0 or y == m-1
    def find_and_remove(item, use_crane):
        for i in range(n):
            for j in range(m):
                if warehouse[i][j] == item and (use_crane or is_edge(i, j)):
                    warehouse[i][j] = None
                    return True
        return False
    for req in requests:
        use_crane = len(req) > 1
        find_and_remove(req, use_crane)
    return sum(row.count(None) for row in warehouse)
warehouse = [['a', 'b', 'a'], ['a', 'd', 'e'], ['a', 'b', 'c']]
requests = ['a', 'bb', 'a']
result = count_remaining_items(warehouse, requests)
print(result)


from itertools import permutations
from collections import defaultdict
def classify_trees(nodes, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    def count_children(node, parent, tree):
        children = [child for child in tree[node] if child != parent]
        return len(children), children
    def is_valid_tree(root, tree):
        stack = [root]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                return False
            visited.add(node)
            stack.extend(tree[node])
        return len(visited) == len(tree)
    total_hol_jjak = 0
    total_y_hol_y_jjak = 0
    for perm in permutations(nodes):
        tree = defaultdict(list)
        for u, v in edges:
            if perm.index(u) < perm.index(v):
                tree[u].append(v)
            else:
                tree[v].append(u)
        root = perm[0]
        if not is_valid_tree(root, tree):
            continue
        child_count, _ = count_children(root, None, tree)
        root_is_odd = root % 2 == 1
        child_is_odd = child_count % 2 == 1
        is_hol_jjak = root_is_odd and child_is_odd
        is_jjak_jjak = not root_is_odd and not child_is_odd
        is_y_hol = not root_is_odd and child_is_odd
        is_y_jjak = root_is_odd and not child_is_odd
        if (is_hol_jjak or is_jjak_jjak) and not (is_hol_jjak and is_y_jjak):
            total_hol_jjak += 1
        elif (is_y_hol or is_y_jjak) and not (is_jjak_jjak and is_y_hol):
            total_y_hol_y_jjak += 1
    return total_hol_jjak, total_y_hol_y_jjak
nodes = [9, 11, 4, 5, 16]
edges = [[9, 11], [4, 5], [5, 16]]
result = classify_trees(nodes, edges)
print(result[0], result[1])


def find_boxes(m, n, k):
    row_idx = (k - 1) // n  
    col_idx = (k - 1) % n  
    first_box_in_row = m - row_idx * n
    if row_idx % 2 == 0:
        return col_idx + 1
    else:
        return n - col_idx
result = find_boxes(7, 2, 4)
print(result)


def minimize_a_traces(traces, m, n):
    traces.sort(reverse=True, key=lambda x: x[0])  
    a_traces = 0
    b_traces = 0    
    for a, b in traces:
        if b_traces + b < n:
            b_traces += b
        elif a_traces + a < m:
            a_traces += a
        else:
            return -1
    return a_traces if a_traces < m else -1
traces = [[1, 2], [1, 1]]
m = 3
n = 3
result = minimize_a_traces(traces, m, n)
print(result)


def server_addition(visitors, k, m):
    servers_added = 0  
    active_servers = [] 
    for i in range(len(visitors)):
        active_servers = [end_time for end_time in active_servers if end_time > i]
        if visitors[i] >= k:
            if not active_servers or active_servers[0] <= i:
                servers_added += 1
                active_servers.append(i + m - 1)        
    return servers_added
visitors = [0, 0, 0, 0, 0, 0, 0, 4, 5, 0, 0, 0, 0, 0, 0, 4, 1, 0, 0, 1, 1, 1]
k = 3
m = 5
result = server_addition(visitors, k, m)
print(result)


def server_addition(visitors, k, m):
    servers_added = 0 
    last_added_time = -1 
    for i in range(len(visitors)):
        if visitors[i] >= k and i > last_added_time:
            servers_added += 1
            last_added_time = i + m - 1 
    return servers_added
visitors = [0, 0, 0, 0, 0, 0, 0, 4, 5, 0, 0, 0, 0, 0, 0, 4, 1, 0, 0, 1, 1, 1]
k = 3
m = 5
result = server_addition(visitors, k, m)
print(result)


def find_position(m, ban):
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    available_chars = [char for char in alphabet if char not in ban]
    m_length = len(m)
    num_combinations = len(available_chars) ** m_length
    position = 0 
    for i in range(m_length):
        char = m[i]
        char_index = available_chars.index(char)
        num_combinations //= len(available_chars) 
        position += char_index * num_combinations
    return position + 1
ban = ['a', 'b', 'd', 'w', 'z', 'aa', 'bb']
m = 'ah'
result = find_position(m, ban)
print(result)


def solution(n, w, num):
    layers = (n + w - 1) // w
    grid = [[-1] * w for _ in range(layers)]
    count = 1
    for i in range(layers):
        if i % 2 == 0:
            for j in range(w):
                if count <= n:
                    grid[i][j] = count
                    count += 1
        else:
            for j in range(w - 1, -1, -1):
                if count <= n:
                    grid[i][j] = count
                    count += 1
    for r in range(layers):
        for c in range(w):
            if grid[r][c] == num:
                target_r, target_c = r, c
                break
    result = 1
    for r in range(target_r + 1, layers):
        if grid[r][target_c] != -1:
            result += 1
    return result


def solution(info, n, m):
    INF = 10**9
    dp = [INF] * m
    dp[0] = 0
    for a, b in info:
        new_dp = [INF] * m
        for b_trace in range(m):
            if dp[b_trace] == INF:
                continue
            if dp[b_trace] + a < n:
                new_dp[b_trace] = min(new_dp[b_trace], dp[b_trace] + a)
            if b_trace + b < m:
                new_dp[b_trace + b] = min(new_dp[b_trace + b], dp[b_trace])
        dp = new_dp
    ans = min(dp)
    return ans if ans < INF else -1
    
    def solution(n, bans):
    pow26 = [1]
    for _ in range(12):
        pow26.append(pow26[-1] * 26)
    def rank(s):
        l = len(s)
        r = sum(pow26[i] for i in range(1, l))
        cur = 0
        for c in s:
            cur = cur * 26 + (ord(c) - 97)
        return r + cur + 1
    banned = sorted(rank(b) for b in bans)
    def count_banned(x):
        lo, hi = 0, len(banned)
        while lo < hi:
            mid = (lo + hi) // 2
            if banned[mid] <= x:
                lo = mid + 1
            else:
                hi = mid
        return lo
    lo, hi = n, n + len(banned)
    while lo < hi:
        mid = (lo + hi) // 2
        if mid - count_banned(mid) >= n:
            hi = mid
        else:
            lo = mid + 1
    x = lo
    length = 1
    while x > pow26[length]:
        x -= pow26[length]
        length += 1
    x -= 1
    res = []
    for _ in range(length):
        res.append(chr(97 + x % 26))
        x //= 26
    return ''.join(reversed(res))


from collections import deque
def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    grid = [list(row) for row in storage]
    def outside_air():
        air = [[False]*m for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n-1 or j == 0 or j == m-1:
                    if grid[i][j] == '.' and not air[i][j]:
                        air[i][j] = True
                        q.append((i, j))
        while q:
            x, y = q.popleft()
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] == '.' and not air[nx][ny]:
                        air[nx][ny] = True
                        q.append((nx, ny))
        return air
    for req in requests:
        c = req[0]
        if len(req) == 2:
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == c:
                        grid[i][j] = '.'
        else:
            air = outside_air()
            remove = []
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == c:
                        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                            ni, nj = i+dx, j+dy
                            if not (0 <= ni < n and 0 <= nj < m) or air[ni][nj]:
                                remove.append((i, j))
                                break
            for i, j in remove:
                grid[i][j] = '.'
    return sum(grid[i][j] != '.' for i in range(n) for j in range(m))
