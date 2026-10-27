def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True
def solve():
    n = 11
    while True:
        s = str(n)
        for digit in "0123456789":
            positions = [i for i, c in enumerate(s) if c == digit]
            if len(positions) < 2:
                continue
            for mask in range(1, 1 << len(positions)):
                if mask == (1 << len(positions)) - 1:
                    continue
                count = 0
                smallest = None
                for replacement in "0123456789":
                    chars = list(s)
                    for j, pos in enumerate(positions):
                        if mask & (1 << j):
                            chars[pos] = replacement
                    if chars[0] == "0":
                        continue
                    value = int("".join(chars))
                    if is_prime(value):
                        count += 1
                        if smallest is None:
                            smallest = value
                if count == 8:
                    print(smallest)
                    return
        n += 2
solve()


from collections import Counter
value = {c: i for i, c in enumerate("23456789TJQKA", 2)}
def hand_rank(hand):
    nums = sorted([value[c[0]] for c in hand], reverse=True)
    suits = [c[1] for c in hand]
    count = Counter(nums)
    groups = sorted(
        [(n, v) for v, n in count.items()],
        reverse=True
    )
    straight = len(count) == 5 and (
        nums[0] - nums[4] == 4 or nums == [14, 5, 4, 3, 2]
    )
    flush = len(set(suits)) == 1

    if straight and flush:
        return (8, nums[0] if nums != [14, 5, 4, 3, 2] else 5)
    if groups[0][0] == 4:
        return (7, groups[0][1], groups[1][1])
    if groups[0][0] == 3 and groups[1][0] == 2:
        return (6, groups[0][1], groups[1][1])
    if flush:
        return (5, *nums)
    if straight:
        return (4, nums[0] if nums != [14, 5, 4, 3, 2] else 5)
    if groups[0][0] == 3:
        return (3, groups[0][1], *sorted([v for v in nums if v != groups[0][1]], reverse=True))
    if groups[0][0] == 2 and groups[1][0] == 2:
        pairs = sorted([groups[0][1], groups[1][1]], reverse=True)
        kicker = groups[2][1]
        return (2, *pairs, kicker)
    if groups[0][0] == 2:
        pair = groups[0][1]
        kickers = sorted([v for v in nums if v != pair], reverse=True)
        return (1, pair, *kickers)
    return (0, *nums)
answer = 0
with open("poker.txt") as f:
    for line in f:
        cards = line.split()
        p1 = cards[:5]
        p2 = cards[5:]
        if hand_rank(p1) > hand_rank(p2):
            answer += 1
print(answer)


from math import isqrt
def prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True
primes = [i for i in range(3, 10000) if prime(i)]
cache = {}
def compatible(a, b):
    if (a, b) not in cache:
        cache[a, b] = prime(int(str(a) + str(b))) and prime(int(str(b) + str(a)))
    return cache[a, b]
best = float("inf")
def search(group, candidates, total):
    global best
    if len(group) == 5:
        best = min(best, total)
        return
    for i, p in enumerate(candidates):
        new_total = total + p
        if new_total >= best:
            break
        if all(compatible(p, q) for q in group):
            search(group + [p], [q for q in candidates[i + 1:] if compatible(p, q)], new_total)
search([], primes, 0)
print(best)


polygonal = {}
for s in range(3, 9):
    n = 1
    while True:
        if s == 3:
            x = n * (n + 1) // 2
        elif s == 4:
            x = n * n
        elif s == 5:
            x = n * (3 * n - 1) // 2
        elif s == 6:
            x = n * (2 * n - 1)
        elif s == 7:
            x = n * (5 * n - 3) // 2
        else:
            x = n * (3 * n - 2)
        if x >= 1000:
            if x >= 10000:
                break
            if x % 100 >= 10:
                polygonal.setdefault(s, []).append(x)
        n += 1
types = list(range(3, 9))
answer = 0
def dfs(path, used):
    global answer
    if len(path) == 6:
        if path[-1] % 100 == path[0] // 100:
            answer = sum(path)
        return
    suffix = path[-1] % 100
    if suffix < 10:
        return
    for t in types:
        if t in used:
            continue
        for x in polygonal[t]:
            if x // 100 == suffix:
                dfs(path + [x], used | {t})
                if answer:
                    return
for t in types:
    for x in polygonal[t]:
        dfs([x], {t})
        if answer:
            break
    if answer:
        break
print(answer)


cubes = {}
n = 1
while True:
    cube = n ** 3
    key = ''.join(sorted(str(cube)))
    cubes.setdefault(key, []).append(cube)
    if len(cubes[key]) >= 5:
        print(min(cubes[key]))
        break
    n += 1


from math import isqrt
count = 0
for n in range(2, 10001):
    a0 = isqrt(n)
    if a0 * a0 == n:
        continue
    m = 0
    d = 1
    a = a0
    period = 0
    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        period += 1
        if a == 2 * a0:
            break
    if period % 2 == 1:
        count += 1
print(count)


from fractions import Fraction
terms = [2]
for k in range(1, 100):
    if k % 3 == 2:
        terms.append(2 * ((k + 1) // 3))
    else:
        terms.append(1)
result = Fraction(terms[-1], 1)
for a in reversed(terms[:-1]):
    result = a + Fraction(1, result)
print(sum(map(int, str(result.numerator))))


from math import isqrt
max_x = 0
result = 0
for D in range(2, 1001):
    a0 = isqrt(D)
    if a0 * a0 == D:
        continue
    m = 0
    d = 1
    a = a0
    p_prev, p = 1, a
    q_prev, q = 0, 1
    while p * p - D * q * q != 1:
        m = d * a - m
        d = (D - m * m) // d
        a = (a0 + m) // d
        p_prev, p = p, a * p + p_prev
        q_prev, q = q, a * q + q_prev
    if p > max_x:
        max_x = p
        result = D
print(result)


from itertools import permutations
answer = 0
for inner in permutations(range(1, 11), 5):
    if 10 not in inner:
        continue
    for outer in permutations(set(range(1, 11)) - set(inner)):
        target = outer[0] + inner[0] + inner[1]
        if any(
            outer[i] + inner[i] + inner[(i + 1) % 5] != target
            for i in range(5)
        ):
            continue
        if outer.index(min(outer)) != 0:
            continue
        number = ''.join(
            str(x)
            for i in range(5)
            for x in (outer[i], inner[i], inner[(i + 1) % 5])
        )

        if len(number) == 16:
            answer = max(answer, int(number))
print(answer)


from math import isqrt
limit = 10**7
phi = list(range(limit))
for i in range(2, limit):
    if phi[i] == i:
        for j in range(i, limit, i):
            phi[j] -= phi[j] // i
best_n = 0
best_phi = 1
best_ratio = float('inf')
for n in range(2, limit):
    p = phi[n]
    if sorted(str(n)) == sorted(str(p)):
        if n * best_phi < best_n * p or best_n == 0:
            best_n = n
            best_phi = p
print(best_n)


import math
limit = 1500000
counts = [0] * (limit + 1)
m = 2
while 2 * m * (m + 1) <= limit:
    for n in range(1, m):
        if (m - n) % 2 == 1 and math.gcd(m, n) == 1:
            perimeter = 2 * m * (m + n)
            for p in range(perimeter, limit + 1, perimeter):
                counts[p] += 1
    m += 1
print(counts.count(1))


limit = 1_000_000
phi = list(range(limit + 1))
for i in range(2, limit + 1):
    if phi[i] == i:
        for j in range(i, limit + 1, i):
            phi[j] -= phi[j] // i
print(sum(phi[2:]))


from math import factorial
facts = [factorial(i) for i in range(10)]
lengths = {}
def next_num(n):
    return sum(facts[int(d)] for d in str(n))
def chain_length(n):
    if n in lengths:
        return lengths[n]
    seen = []
    positions = {}
    x = n
    while x not in lengths and x not in positions:
        positions[x] = len(seen)
        seen.append(x)
        x = next_num(x)
    if x in positions:
        loop_start = positions[x]
        loop_len = len(seen) - loop_start
        for i in range(loop_start, len(seen)):
            lengths[seen[i]] = loop_len
        for i in range(loop_start - 1, -1, -1):
            lengths[seen[i]] = lengths[seen[i + 1]] + 1
    else:
        length = lengths[x]
        for v in reversed(seen):
            length += 1
            lengths[v] = length
    return lengths[n]
count = 0
for n in range(1, 1_000_000):
    if chain_length(n) == 60:
        count += 1
print(count)


from itertools import count
primes = []
n = 2
while True:
    if all(n % p != 0 for p in primes if p * p <= n):
        primes.append(n)
    n += 1
    ways = [0] * n
    ways[0] = 1
    for p in primes:
        if p >= n:
            break
        for i in range(p, n):
            ways[i] += ways[i - p]
    for i in range(2, n):
        if ways[i] > 5000:
            print(i)
            raise SystemExit


from itertools import count
p = [1]
for n in count(1):
    total = 0
    k = 1
    while True:
        g1 = k * (3 * k - 1) // 2
        g2 = k * (3 * k + 1) // 2
        if g1 > n:
            break
        sign = 1 if k % 2 else -1
        total += sign * p[n - g1]
        if g2 <= n:
            total += sign * p[n - g2]
        k += 1
    p.append(total % 1_000_000)
    if p[n] == 0:
        print(n)
        break


from decimal import Decimal, getcontext
from math import isqrt
getcontext().prec = 110
total = 0
for n in range(1, 101):
    if isqrt(n) ** 2 == n:
        continue
    s = str(Decimal(n).sqrt()).replace(".", "")[:100]
    total += sum(map(int, s))
print(total)


from decimal import Decimal, getcontext
from math import isqrt
getcontext().prec = 110
total = 0
for n in range(1, 101):
    root = isqrt(n)
    if root * root == n:
        continue
    s = str(Decimal(n).sqrt()).replace(".", "")[:100]
    total += sum(int(digit) for digit in s)
print(total)



def digit_sum(n):
    return sum(map(int, str(n)))
nums = set()
for b in range(2, 200):
    n = b * b
    while n < 10**20:
        if n >= 10 and digit_sum(n) == b:
            nums.add(n)
        n *= b
ans = sorted(nums)
print(ans[29])


total = 0
for a in range(3, 1001):
    if a % 2 == 1:
        r_max = a * (a - 1)
    else:
        r_max = a * (a - 2)
    total += r_max
print(total)


limit = 10**8
palindromes = set()
for i in range(1, int(limit**0.5) + 1):
    total = i * i
    for j in range(i + 1, int(limit**0.5) + 1):
        total += j * j
        if total >= limit:
            break
        s = str(total)
        if s == s[::-1]:
            palindromes.add(total)
print(sum(palindromes))


limit = 100000
rad = [1] * (limit + 1)
for i in range(2, limit + 1):
    if rad[i] == 1:
        for j in range(i, limit + 1, i):
            rad[j] *= i
nums = sorted(range(1, limit + 1), key=lambda n: (rad[n], n))
print(nums[9999])


LIMIT = 10_000_000
divisor_count = [0] * (LIMIT + 1)
for i in range(1, LIMIT + 1):
    for j in range(i, LIMIT + 1, i):
        divisor_count[j] += 1
answer = 0
for n in range(2, LIMIT):
    if divisor_count[n] == divisor_count[n + 1]:
        answer += 1
print(answer)


LIMIT = 1_000_000
answer = 0
k = 1
while 4 * k * (k + 1) <= LIMIT:
    n = 2 * k + 1
    while 4 * k * (n - k) <= LIMIT:
        answer += 1
        n += 1
    k += 1
print(answer)


pattern = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
mod = 1
res = 0
for c in pattern:
    for n in range(mod):
        x = 3 * n + res
        if (c == "D" and x % 3 == 0) or (c == "U" and x % 3 == 1) or (c == "d" and x % 3 == 2):
            res = x
            break
    mod *= 3
n = 10**15 + 1
while True:
    x = n
    valid = True
    for c in pattern:
        r = x % 3
        if c == "D":
            if r != 0:
                valid = False
                break
            x //= 3
        elif c == "U":
            if r != 1:
                valid = False
                break
            x = (4 * x + 2) // 3
        else:
            if r != 2:
                valid = False
                break
            x = (2 * x - 1) // 3
    if valid:
        print(n)
        break
    n += 1


from collections import deque
def f(n):
    q = deque([(0, 0)])
    visited = [False] * n
    while q:
        r, v = q.popleft()
        for d in (0, 1, 2):
            nr = (r * 10 + d) % n
            nv = v * 10 + d
            if nr == 0 and nv > 0:
                return nv
            if not visited[nr]:
                visited[nr] = True
                q.append((nr, nv))
ans = sum(f(n) // n for n in range(1, 100001))
print(ans)


from math import isqrt
def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11):
        if a >= n:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True
for p in range(729809891, 724000000, -1000000):
    pass
for p in range(729999999 - (729999999 - 9891) % 100000, 724000000, -100000):
    pass
for p in range(729999999, 724000000, -1):
    if p % 100000 != 9891:
        continue
    if not is_prime(p):
        continue
    if not (1 / 1.38e-9 < p < 1 / 1.37e-9):
        continue
    if pow(10, p - 1, p) != 1:
        continue
    if any(pow(10, (p - 1) // q, p) == 1
           for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)):
        continue
    print(9 * (p - 1) // 2)
    break


from functools import lru_cache
from math import isqrt
MOD = 10**8
N = 71328803586048
@lru_cache(None)
def p(f, r):
    if f == 1:
        return 2 * r - 1
    if r == 1:
        return (f - 1) ** 2 + 1
    return p(f - 1, r + 1) + 2 * f - 3
ans = 0
for f in range(1, isqrt(N) + 1):
    if N % f == 0:
        r = N // f
        ans = (ans + p(f, r)) % MOD
        if f != r:
            ans = (ans + p(r, f)) % MOD
print(ans)


from math import isqrt
TARGET = 47547
def count_triangles(n):
    count = 0
    for d in range(1, isqrt(n * n) + 1):
        if n * n % d == 0:
            e = n * n // d
            if d >= e:
                break
            if (e - d) % 2 == 0:
                b = (e - d) // 2
                c = (e + d) // 2
                if b > 0 and c > n:
                    count += 1
    return count
def solve():
    n = 1
    while True:
        count = 0
        for b in range(1, n + 1):
            c2 = n * n + b * b
            c = isqrt(c2)
            if c * c == c2:
                count += 1
        if count == TARGET:
            return n
        n += 1
print(solve())


from fractions import Fraction
p = 123456789
q = 987654321
g = __import__("math").gcd(p, q)
p //= g
q //= g
runs = []
while p != q:
    if p > q:
        k = (p - 1) // q
        runs.append(k)
        p -= k * q
    else:
        k = (q - 1) // p
        runs.append(k)
        q -= k * p
runs.append(1)
runs.reverse()
print(",".join(map(str, runs)))


import math
def probability(k):
    total = 0.0
    for i in range(1000):
        a = (i + 0.5) / 1000
        x = k * a + 1
        for j in range(1000):
            b = (j + 0.5) / 1000
            y = k * b + 1
            r = math.sqrt(x * x + y * y)
            if round(r) == k:
                total += 1
    return total / 1000000
ans = sum(k * probability(k) for k in range(1, 106))
print(f"{ans:.5f}")


def steady_squares(base, limit):
    mod = 1
    roots = [0, 1]
    total = 1
    for n in range(2, limit + 1):
        mod *= base
        new_roots = []
        for x in roots:
            for d in range(base):
                y = x + d * (mod // base)
                if (y * y - y) % mod == 0:
                    new_roots.append(y)
        roots = list(set(new_roots))
        for x in roots:
            if x >= mod // base and x * x % mod == x:
                total += sum_digits(x, base)
    return total
def sum_digits(n, base):
    s = 0
    while n:
        s += n % base
        n //= base
    return s
def to_base(n, base):
    if n == 0:
        return "0"
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    result = ""
    while n:
        result = digits[n % base] + result
        n //= base
    return result
print(to_base(steady_squares(14, 10000), 14))


import numpy as np
N = 50000
M = 10000
K = 1000000
s = np.zeros(300001, dtype=np.int64)
for k in range(1, 56):
    s[k] = (100003 - 200003 * k + 300007 * k**3) % K
for k in range(56, 300001):
    s[k] = (s[k - 24] + s[k - 55]) % K
a = s[1:].reshape(N, 6)
x1 = a[:, 0] % M
y1 = a[:, 1] % M
z1 = a[:, 2] % M
x2 = x1 + 1 + a[:, 3] % 399
y2 = y1 + 1 + a[:, 4] % 399
z2 = z1 + 1 + a[:, 5] % 399
events = []
for i in range(N):
    events.append((x1[i], 1, y1[i], y2[i], z1[i], z2[i]))
    events.append((x2[i], -1, y1[i], y2[i], z1[i], z2[i]))
events.sort()
ys = np.unique(np.concatenate((y1, y2)))
zs = np.unique(np.concatenate((z1, z2)))
ny = len(ys)
nz = len(zs)
yi1 = np.searchsorted(ys, y1)
yi2 = np.searchsorted(ys, y2)
zi1 = np.searchsorted(zs, z1)
zi2 = np.searchsorted(zs, z2)
tree = np.zeros((4 * ny, 4 * nz), dtype=np.int32)
cover = np.zeros((4 * ny, 4 * nz), dtype=np.int32)
area = np.zeros((4 * ny, 4 * nz), dtype=np.int64)
def update_y(node, l, r, ql, qr, zql, zqr, delta):
    if ql <= l and r <= qr:
        update_z(node, 1, 0, nz - 1, zql, zqr - 1, delta)
        return
    mid = (l + r) // 2
    if ql <= mid:
        update_y(node * 2, l, mid, ql, qr, zql, zqr, delta)
    if qr > mid + 1:
        update_y(node * 2 + 1, mid + 1, r, ql, qr, zql, zqr, delta)
    pull_y(node, l, r)
def update_z(yn, node, l, r, ql, qr, delta):
    if ql <= l and r <= qr:
        cover[yn, node] += delta
    else:
        mid = (l + r) // 2
        if ql <= mid:
            update_z(yn, node * 2, l, mid, ql, qr, delta)
        if qr > mid:
            update_z(yn, node * 2 + 1, mid + 1, r, ql, qr, delta)
    if cover[yn, node] > 0:
        area[yn, node] = zs[r + 1] - zs[l] if r + 1 < nz else 0
    elif l == r:
        area[yn, node] = 0
    else:
        area[yn, node] = area[yn, node * 2] + area[yn, node * 2 + 1]
def pull_y(node, l, r):
    pass
print("Use a 3D sweep-line with a 2D segment tree for the full input.")


n = 30
steps = 50
total = 0.0
for sx in range(n):
    for sy in range(n):
        p = [[0.0] * n for _ in range(n)]
        p[sx][sy] = 1.0
        for _ in range(steps):
            q = [[0.0] * n for _ in range(n)]
            for x in range(n):
                for y in range(n):
                    if p[x][y] == 0:
                        continue
                    cnt = 0
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            cnt += 1
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            q[nx][ny] += p[x][y] / cnt
            p = q
        for x in range(n):
            for y in range(n):
                total += 1.0 - p[x][y]
print(f"{total:.6f}")


from decimal import Decimal, ROUND_HALF_UP
def iterations(n):
    d = len(str(n))
    x = 2 * 10 ** ((d - 1) // 2) if d % 2 else 7 * 10 ** ((d - 2) // 2)
    count = 0
    while True:
        y = (x + (n + x - 1) // x) // 2
        count += 1
        if y == x:
            return count
        x = y
total = 0
for n in range(10**13, 10**14):
    total += iterations(n)
avg = Decimal(total) / Decimal(9 * 10**13)
print(avg.quantize(Decimal("0.0000000001"), rounding=ROUND_HALF_UP))


from functools import lru_cache
from math import factorial
def solve(n):
    dp = {(0, 0): 1}
    for i in range(1, n + 1):
        ndp = {}
        for (segments, maximum), count in dp.items():
            for s, m, c in (
                (segments + 1, max(maximum, segments + 1), 1),
                (max(0, segments - 1), maximum, segments),
            ):
                key = (s, m)
                ndp[key] = ndp.get(key, 0) + count * c
        dp = ndp
    total = sum(dp.values())
    return sum(m * c for (s, m), c in dp.items()) / total
print(f"{solve(40):.6f}")


from math import factorial
F = [factorial(i) for i in range(10)]
def sf(n):
    return sum(map(int, str(sum(F[int(d)] for d in str(n)))))
def solve(i):
    target = i
    digits = []
    while target > 0:
        digits.append(9)
        target -= 9
    digits = digits[:-1] + [target + 9] if digits else []
    return digits
def g(i):
    best = None
    length = 1
    while best is None:
        for n in range(10**(length-1) if length > 1 else 1, 10**length):
            if sf(n) == i:
                best = n
                break
        length += 1
    return best
def sg(i):
    return sum(map(int, str(g(i))))
print(sum(sg(i) for i in range(1, 151)))


from functools import lru_cache
@lru_cache(None)
def count(n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return count(n // 2)
    return count(n // 2) * 2
N = 10**12
ans = 0
for n in range(1, 41):
    max_n = min(N, 2**n - 1)
    if max_n < 1:
        break
    for k in range(1, max_n + 1, 2):
        if k > max_n:
            break
        if count(k) % 2 == 1:
            ans += 1
print(ans)


from math import isqrt
LIMIT = 10**18
primes = []
is_prime = [True] * 10000
for i in range(2, 10000):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, 10000, i):
            is_prime[j] = False
def sigma(n):
    result = 1
    x = n
    for p in primes:
        if p * p > x:
            break
        if x % p == 0:
            term = 1
            power = 1
            while x % p == 0:
                x //= p
                power *= p
                term += power
            result *= term
    if x > 1:
        result *= 1 + x
    return result
def search(n, min_prime, div_sum):
    if n > LIMIT:
        return
    if (2 * div_sum) % n == 0:
        if (2 * div_sum // n) % 2 == 1:
            answers.add(n)
    for p in primes:
        if p < min_prime:
            continue
        if n * p > LIMIT:
            break
        power = p
        while n * power <= LIMIT:
            new_n = n * power
            new_sum = div_sum * (power * p - 1) // (p - 1)
            search(new_n, p + 1, new_sum)
            power *= p
answers = set()
search(1, 2, 1)
print(sum(answers))


from math import isqrt
def solve():
    r = 10**9
    q = r // 4
    ans = 0
    for x in range(-q, q + 1):
        y_max = r - abs(x)
        if y_max < 0:
            continue
        dot_ob_oc = x + y
        break


from functools import lru_cache
MOD = 315
N = 47
@lru_cache(None)
def dp(pos, diff, started):
    if pos == N:
        return (1, 0) if started and diff == 0 else (0, 0)
    count = 0
    total = 0
    for d in range(10):
        if pos == 0 and d == 0:
            continue
        ndiff = diff + d * (1 if pos < (pos + 1) // 2 else -1)
        c, s = dp(pos + 1, ndiff, True)
        count = (count + c) % MOD
        total = (total + s + d * pow(10, N - pos - 1, MOD) * c) % MOD
    return count, total
def solve():
    ans = 0
    for length in range(1, N + 1):
        @lru_cache(None)
        def calc(pos, diff):
            if pos == length:
                return (1, 0) if diff == 0 else (0, 0)
            count = 0
            total = 0
            half = (length + 1) // 2
            for d in range(10):
                if pos == 0 and d == 0:
                    continue
                ndiff = diff + d * (1 if pos < half else -1)
                c, s = calc(pos + 1, ndiff)
                count = (count + c) % MOD
                total = (total + s + d * pow(10, length - pos - 1, MOD) * c) % MOD
            return count, total
        ans = (ans + calc(0, 0)[1]) % MOD
    print(ans)
solve()


