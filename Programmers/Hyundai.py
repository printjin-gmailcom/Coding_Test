MOD = 1_000_000_007
def mat_mult(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        Ci = C[i]
        for k in range(n):
            aik = Ai[k]
            if aik:
                Bk = B[k]
                for j in range(n):
                    Ci[j] = (Ci[j] + aik * Bk[j]) % MOD
    return C
def mat_pow(A, exp):
    n = len(A)
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        res[i][i] = 1
    base = A
    while exp > 0:
        if exp & 1:
            res = mat_mult(res, base)
        base = mat_mult(base, base)
        exp >>= 1
    return res
def solution(grid, d, k):
    n_rows = len(grid)
    n_cols = len(grid[0])
    N = n_rows * n_cols
    L = len(d)
    def idx(r, c): return r * n_cols + c
    B_list = []
    for p in range(L):
        B_list.append([[0]*N for _ in range(N)])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for r in range(n_rows):
        for c in range(n_cols):
            u = idx(r,c)
            h_u = grid[r][c]
            for dr,dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n_rows and 0 <= nc < n_cols:
                    v = idx(nr,nc)
                    slope = grid[nr][nc] - h_u
                    for p in range(L):
                        if d[p] == slope:
                            B_list[p][u][v] = (B_list[p][u][v] + 1) % MOD
    if L == 0:
        return 0
    A = B_list[0]
    for p in range(1, L):
        A = mat_mult(A, B_list[p])
    A_k = mat_pow(A, k)
    total = 0
    Nrange = range(N)
    for i in Nrange:
        row = A_k[i]
        s = sum(row) % MOD
        total = (total + s) % MOD
    return total
