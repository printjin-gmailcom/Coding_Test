import heapq
def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    queue = [(0, 1)]
    while queue:
        current_time, current_village = heapq.heappop(queue)
        if current_time > dist[current_village]:
            continue
        for neighbor, travel_time in graph[current_village]:
            new_time = current_time + travel_time
            if new_time < dist[neighbor]:
                dist[neighbor] = new_time
                heapq.heappush(queue, (new_time, neighbor))
    return sum(1 for time in dist if time <= K)