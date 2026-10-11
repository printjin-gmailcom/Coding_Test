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

