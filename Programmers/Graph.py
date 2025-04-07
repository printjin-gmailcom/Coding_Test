def solution(n, results):
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for win, lose in results:
        graph[win][lose] = 1
        graph[lose][win] = -1
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[j][i] = -1
                if graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
                    graph[j][i] = 1
    answer = 0
    for i in range(1, n + 1):
        if graph[i].count(0) == 2: 
            answer += 1
    return answer


from collections import deque, defaultdict
def solution(n, vertex):
    graph = defaultdict(list)
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    queue = deque([1])
    visited = [-1] * (n + 1)
    visited[1] = 0  
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if visited[neighbor] == -1: 
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)
    max_distance = max(visited)
    return visited.count(max_distance)