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


