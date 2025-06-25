def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False]*m for _ in range(n)]
    from collections import deque
    def bfs(i, j):
        q = deque()
        q.append((i,j))
        visited[i][j] = True
        oil = [(i,j)]
        while q:
            x, y = q.popleft()
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and land[nx][ny]==1:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    oil.append((nx,ny))
        return oil
    oil_infos = []
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j]==1:
                cells = bfs(i,j)
                oil_infos.append((set(y for x,y in cells), len(cells)))  # (통과하는 열들, 크기)
    result = 0
    for col in range(m):
        total = 0
        for cols, size in oil_infos:
            if col in cols:
                total += size
        result = max(result, total)
    return result


from collections import deque
def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    oil_id_map = [[-1] * m for _ in range(n)]
    oil_sizes = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def bfs(x, y, oil_id):
        q = deque()
        q.append((x, y))
        visited[x][y] = True
        oil_id_map[x][y] = oil_id
        size = 1
        cols = set([y])
        while q:
            cx, cy = q.popleft()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and land[nx][ny] == 1:
                        visited[nx][ny] = True
                        oil_id_map[nx][ny] = oil_id
                        q.append((nx, ny))
                        size += 1
                        cols.add(ny)
        return size, cols
    oil_col_map = [set() for _ in range(m)]
    oil_id = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j] == 1:
                size, cols = bfs(i, j, oil_id)
                oil_sizes.append(size)
                for col in cols:
                    oil_col_map[col].add(oil_id)
                oil_id += 1
    max_oil = 0
    for col in range(m):
        total = sum(oil_sizes[oid] for oid in oil_col_map[col])
        max_oil = max(max_oil, total)
    return max_oil


def solution(diffs, times, limit):
    n = len(diffs)
    def is_possible(level):
        total_time = times[0]
        for i in range(1, n):
            if diffs[i] <= level:
                total_time += times[i]
            else:
                cnt = diffs[i] - level
                total_time += cnt * (times[i] + times[i-1]) + times[i]
                if total_time > limit:
                    return False
        return total_time <= limit
    left, right = 1, max(diffs)
    answer = right
    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer
