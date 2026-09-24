def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1
happy = [False] * 10000
for i in range(1, 10000):
    happy[i] = is_happy(i)
count = 0
total = 0
for i in range(1, 10000):
    if happy[i]:
        count += 1
        total += i
print(count * total)



def read_num(n):
    nums = ["", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    units = ["", "십", "백", "천"]
    result = ""
    for i, digit in enumerate(map(int, f"{n:04d}")):
        if digit:
            if digit != 1 or i == 3:
                result += nums[digit]
            result += units[3 - i]
    return result
def read_money(n):
    units = ["", "만", "억", "조"]
    groups = []
    while n:
        groups.append(n % 10000)
        n //= 10000
    result = []
    for i in range(len(groups) - 1, -1, -1):
        if groups[i]:
            part = read_num(groups[i])
            if i == 0 and groups[i] == 1:
                part = "일"
            result.append(part + units[i] + "원" if i == 0 else part + units[i])
    return " ".join(result)
inputs = [
    "1원",
    "80,270원",
    "111,111원",
    "1,234,567,890원",
    "100,000,000,000,000원"
]
for money in inputs:
    n = int(money.replace(",", "").replace("원", ""))
    print(read_money(n))


W, H = 1920, 1080
covered = bytearray(W * H)
with open("boxes.txt", "r") as f:
    for line in f:
        x1, y1, x2, y2 = map(int, line.split())
        for y in range(y1, y2):
            start = y * W + x1
            covered[start:start + (x2 - x1)] = b'\x01' * (x2 - x1)
print(sum(covered))


def column_name(n):
    result = []
    while n > 0:
        n -= 1
        result.append(chr(ord('A') + n % 26))
        n //= 26
    return ''.join(reversed(result))
print(column_name(100_000_000))


import sys
for line in sys.stdin:
    nums = list(map(int, line.replace(',', ' ').split()))
    if sum(x != 0 for x in nums) < 2:
        print(-1)
        continue
    nums.sort()
    a = [next(x for x in nums if x != 0)]
    nums.remove(a[0])
    b = [next(x for x in nums if x != 0)]
    nums.remove(b[0])
    for i, x in enumerate(nums):
        if i % 2 == 0:
            a.append(x)
        else:
            b.append(x)
    a = int(''.join(map(str, a)))
    b = int(''.join(map(str, b)))
    print(a + b)


a, b = 12345678999, 99987654321
x, y = 1, 2
total = 0
while x <= b:
    if x >= a:
        total += x
    x, y = y, x + y
print(total)


