from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque([(0, 0)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == m - 1:
            return maps[x][y]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    return -1


from collections import deque
def solution(n, computers):
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            for neighbor in range(n):
                if computers[node][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
    visited = [False] * n
    network_count = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            network_count += 1
    return network_count


from collections import defaultdict
def solution(tickets):
    graph = defaultdict(list)
    for start, end in sorted(tickets):
        graph[start].append(end)
    route = []
    def dfs(airport):
        while graph[airport]:
            next_airport = graph[airport].pop(0)
            dfs(next_airport)
        route.append(airport)
    dfs("ICN")
    return route[::-1]


def solution(numbers, target):
    def dfs(index, current_sum):
        if index == len(numbers):  
            if current_sum == target:
                return 1
            else:
                return 0
        return dfs(index + 1, current_sum + numbers[index]) + dfs(index + 1, current_sum - numbers[index])
    return dfs(0, 0)


def solution(n, wires):
    def dfs(node, visited, graph):
        visited[node] = True
        count = 1 
        for nxt in graph[node]:
            if not visited[nxt]:
                count += dfs(nxt, visited, graph)
        return count
    answer = n
    for cut in wires:
        graph = [[] for _ in range(n+1)]
        for v1, v2 in wires:
            if [v1, v2] == cut or [v2, v1] == cut:
                continue
            graph[v1].append(v2)
            graph[v2].append(v1)
        visited = [False] * (n+1)
        cnt = dfs(cut[0], visited, graph)
        diff = abs((n - cnt) - cnt)
        answer = min(answer, diff)
    return answer


from collections import deque
def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n+1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    dist = [-1] * (n+1)
    q = deque([destination])
    dist[destination] = 0
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if dist[nxt] == -1:  
                dist[nxt] = dist[now] + 1
                q.append(nxt)
    return [dist[s] for s in sources]


from itertools import permutations
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def solution(numbers):
    candidates = set()
    for i in range(1, len(numbers)+1):
        for perm in permutations(numbers, i):
            num = int(''.join(perm)) 
            candidates.add(num)
    answer = sum(1 for num in candidates if is_prime(num))
    return answer
