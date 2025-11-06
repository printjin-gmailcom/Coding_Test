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


import sys
from collections import deque
def solution(grid):
    n = len(grid)
    m = len(grid[0])
    visited = [[[-1, -1] for _ in range(m)] for __ in range(n)]
    vis_count = 0
    def get_nexts(i, j, k):
        nexts = []
        flag = grid[i][j]
        if flag == 1:
            if k == 0:
                if j != 0:
                    nexts.append((i, j-1, 1))
                if i != 0:
                    a = grid[i-1][j]
                    if a == 1:
                        nexts.append((i-1, j, 1))
                    else:
                        nexts.append((i-1, j, 0))
            else:
                if j != m-1:
                    nexts.append((i, j+1, 0))
                if i != n-1:
                    a = grid[i+1][j]
                    if a == 1:
                        nexts.append((i+1, j, 0))
                    else:
                        nexts.append((i+1, j, 1))
        else:
            if k == 0:
                if j != 0:
                    nexts.append((i, j-1, 1))
                if i != n-1:
                    a = grid[i+1][j]
                    if a == 1:
                        nexts.append((i+1, j, 0))
                    else:
                        nexts.append((i+1, j, 1))
            else:
                if j != m-1:
                    nexts.append((i, j+1, 0))
                if i != 0:
                    a = grid[i-1][j]
                    if a == 1:
                        nexts.append((i-1, j, 1))
                    else:
                        nexts.append((i-1, j, 0))
        return nexts
    def go(start_i, start_j, start_k):
        nonlocal vis_count
        acc = []
        stack = deque()
        stack.append((start_i, start_j, start_k))
        visited[start_i][start_j][start_k] = vis_count
        while stack:
            x, y, z = stack.popleft()
            acc.append(x * m + y)
            for nx, ny, nz in get_nexts(x, y, z):
                if visited[nx][ny][nz] != vis_count:
                    visited[nx][ny][nz] = vis_count
                    stack.append((nx, ny, nz))
        return acc
    def calculate(merged, is_cycle):
        if not merged:
            return 0
        limit = len(merged)
        seen = set()
        dup = False
        for el in merged:
            if el in seen:
                dup = True
                break
            seen.add(el)
        if dup:
            limit -= 1
        if is_cycle:
            merged = merged + merged
        left = 0
        memo = {}
        dup_counts = 0
        ret = 0
        def add(el):
            nonlocal dup_counts
            v = memo.get(el, 0) + 1
            memo[el] = v
            if v == 2:
                dup_counts += 1
        def remove(el):
            nonlocal dup_counts
            v = memo.get(el, 0)
            if v == 1:
                del memo[el]
            else:
                memo[el] = v-1
                if v-1 == 1:
                    dup_counts -= 1
        for right in range(len(merged)):
            add(merged[right])
            while dup_counts >= 1:
                remove(merged[left])
                left += 1
            ret = max(ret, right - left + 1)
        return min(limit, ret)
    def check(i, j, k):
        nonlocal vis_count
        nexts = get_nexts(i, j, k)
        vis_count += 1
        visited[i][j][k] = vis_count
        if not nexts:
            return 1
        results = []
        for ni, nj, nk in nexts:
            results.append(go(ni, nj, nk))
        is_cycle = (len(results) == 2 and len(results[1]) == 0)
        merged = results[0][::-1]
        merged.append(i * m + j)
        if len(results) == 2:
            merged.extend(results[1])
        return calculate(merged, is_cycle)
    res = 0
    for i in range(n):
        for j in range(m):
            for k in range(2):
                if visited[i][j][k] == -1:
                    res = max(res, check(i, j, k))
    return res

