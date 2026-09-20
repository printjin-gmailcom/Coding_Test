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


