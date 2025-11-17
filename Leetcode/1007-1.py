import sys
import math
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    pts = [tuple(map(int, input().split())) for _ in range(n)]
    sx = sum(x for x, _ in pts)
    sy = sum(y for _, y in pts)
    half = n // 2
    ans = [float('inf')]
    def dfs(i, cnt, xsum, ysum):
        if cnt > half:
            return
        if i == n:
            if cnt == half:
                vx = sx - 2 * xsum
                vy = sy - 2 * ysum
                dist = math.hypot(vx, vy)
                if dist < ans[0]:
                    ans[0] = dist
            return
        dfs(i + 1, cnt + 1, xsum + pts[i][0], ysum + pts[i][1])
        dfs(i + 1, cnt, xsum, ysum)
    dfs(0, 0, 0, 0)
    print(f"{ans[0]:.12f}")
