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


def solution(points, routes):
    from collections import defaultdict
    robot_paths = []
    for route in routes:
        path = []
        for i in range(len(route) - 1):
            sr, sc = points[route[i] - 1]
            er, ec = points[route[i + 1] - 1]
            while sr != er:
                path.append((sr, sc))
                sr += 1 if sr < er else -1
            while sc != ec:
                path.append((sr, sc))
                sc += 1 if sc < ec else -1
        path.append((er, ec))
        robot_paths.append(path)
    t = 0
    danger_count = 0
    active = True
    while active:
        pos_count = defaultdict(int)
        active = False
        for path in robot_paths:
            if t < len(path):
                pos_count[path[t]] += 1
                active = True
        for v in pos_count.values():
            if v >= 2:
                danger_count += 1
        t += 1
    return danger_count


from collections import deque
def solution(maze):
    n, m = len(maze), len(maze[0])
    dirs = [(-1,0),(1,0),(0,-1),(0,1),(0,0)]
    rs = bs = re = be = None
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1: rs = (i,j)
            elif maze[i][j] == 2: bs = (i,j)
            elif maze[i][j] == 3: re = (i,j)
            elif maze[i][j] == 4: be = (i,j)
    def inside(x,y):
        return 0 <= x < n and 0 <= y < m and maze[x][y] != 5
    encode = lambda x,y: x*m+y
    start = (rs[0],rs[1],bs[0],bs[1], 1<<encode(rs[0],rs[1]), 1<<encode(bs[0],bs[1]))
    q = deque([(start,0)])
    visited = set([start])
    while q:
        (rx,ry,bx,by, rv, bv), d = q.popleft()
        if (rx,ry) == re and (bx,by) == be:
            return d
        for drx,dry in dirs:
            nrx,nry = rx+drx, ry+dry
            if (rx,ry)==re:
                nrx,nry = rx,ry
            else:
                if not inside(nrx,nry): continue
                if rv & (1<<encode(nrx,nry)): continue
            for dbx,dby in dirs:
                nbx,nby = bx+dbx, by+dby
                if (bx,by)==be:
                    nbx,nby = bx,by
                else:
                    if not inside(nbx,nby): continue
                    if bv & (1<<encode(nbx,nby)): continue
                if (nrx,nry)==(nbx,nby): continue
                if (nrx,nry)==(bx,by) and (nbx,nby)==(rx,ry): continue
                nrv = rv | (1<<encode(nrx,nry))
                nbv = bv | (1<<encode(nbx,nby))
                state = (nrx,nry,nbx,nby,nrv,nbv)
                if state not in visited:
                    visited.add(state)
                    q.append((state,d+1))
    return 0


def solution(expressions):
    def to10(s, base):
        v = 0
        for ch in s:
            d = int(ch)
            if d >= base:
                return None
            v = v * base + d
        return v
    parsed = []
    nums = set()
    for exp in expressions:
        a, op, b, _, c = exp.split()
        parsed.append((a, op, b, c))
        for x in [a, b, c]:
            if x != "X":
                for ch in x:
                    nums.add(int(ch))
    min_base = max(nums) + 1
    if min_base < 2:
        min_base = 2
    candidates = []
    for base in range(min_base, 10):
        ok = True
        for a, op, b, c in parsed:
            if c == "X":
                continue
            A = to10(a, base)
            B = to10(b, base)
            C = to10(c, base)
            if A is None or B is None or C is None:
                ok = False
                break
            if op == "+":
                if A + B != C:
                    ok = False
                    break
            else:
                if A - B != C:
                    ok = False
                    break
        if ok:
            candidates.append(base)
    res = []
    for a, op, b, c in parsed:
        if c != "X":
            continue
        vals = set()
        for base in candidates:
            A = to10(a, base)
            B = to10(b, base)
            if A is None or B is None:
                continue
            if op == "+":
                v = A + B
            else:
                v = A - B
            out = ""
            if v == 0:
                out = "0"
            else:
                tmp = []
                while v > 0:
                    tmp.append(str(v % base))
                    v //= base
                out = "".join(reversed(tmp))
            vals.add(out)
        if len(vals) == 1:
            res.append(f"{a} {op} {b} = {vals.pop()}")
        else:
            res.append(f"{a} {op} {b} = ?")
    return res


from fractions import Fraction
def solution(h1,m1,s1,h2,m2,s2):
    t1 = h1*3600 + m1*60 + s1
    t2 = h2*3600 + m2*60 + s2
    p_sm = Fraction(3600,59)
    p_sh = Fraction(43200,719)
    def ceil_frac(fr):
        n,d = fr.numerator, fr.denominator
        return (n + d - 1) // d
    def floor_frac(fr):
        n,d = fr.numerator, fr.denominator
        return n // d
    times = set()
    q1_min = ceil_frac(Fraction(t1,1) / p_sm)
    q1_max = floor_frac(Fraction(t2,1) / p_sm)
    for k in range(q1_min, q1_max+1):
        times.add(k * p_sm)
    q2_min = ceil_frac(Fraction(t1,1) / p_sh)
    q2_max = floor_frac(Fraction(t2,1) / p_sh)
    for k in range(q2_min, q2_max+1):
        times.add(k * p_sh)
    return sum(1 for tt in times if tt >= t1 and tt <= t2)
