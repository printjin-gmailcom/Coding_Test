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