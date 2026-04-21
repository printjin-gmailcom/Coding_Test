print("Hello World")


from datetime import datetime, timedelta
utc_now = datetime.utcnow()
kst_now = utc_now + timedelta(hours=9)
print(kst_now.strftime("%Y-%m-%d"))


print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")


print("|\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\__|")


print("         ,r'\"7")
print("r`-_   ,'  ,/")
print(" \. \". L_r'")
print("   `~\\/")
print("      |")
print("      |")


print("5\n")
print("printjin\n")


a, b = input().split()
print(int(a)+int(b))


a, b = input().split()
print(int(a)-int(b))


a, b = input().split()
print(int(a)*int(b))


a, b = input().split()
print(int(a)/int(b))


a, b = input().split()
c  = int(a)+int(b)
d = int(a)-int(b)
e = int(a)*int(b)
f = int(a)//int(b)
g = int(a)%int(b)
print(c,d,e,f,g)


s = input()
print(s+'??!')


a = input()
print(int(a) - 543)


a, b, c = map(int, input().split())
print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)


A = int(input())
B = int(input())
print(A * (B % 10))
print(A * ((B // 10) % 10))
print(A * (B // 100))
print(A * B)


a, b, c = map(int, input().split())
print(a+b+c)


a, b = map(int, input().split())
if a > b:
    print('>')
if a < b:
    print('<')
if a == b:
    print('==')


a = int(input())  
if a >= 90:
    print('A')
elif a >= 80:
    print('B')
elif a >= 70:
    print('C')
elif a >= 60:
    print('D')
else:
    print('F')


a = int(input()) 
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print(1)
else:
    print(0)


a = int(input()) 
b = int(input()) 
if a > 0 and b > 0:
    print(1)
elif a < 0 and b > 0:
    print(2)
elif a < 0 and b < 0:
    print(3)
elif a > 0 and b < 0:
    print(4)


H, M = map(int, input().split())
if M >= 45:
    M -= 45
else:
    M += 15
    if H == 0:
        H = 23
    else:
        H -= 1
print(H, M)


A, B = map(int, input().split())  
C = int(input())  
B += C
A += B // 60 
B = B % 60  
A = A % 24
print(A, B)


A, B = map(int, input().split())  
C = int(input())  
B += C
A += B // 60 
B = B % 60  
A = A % 24
print(A, B)


a, b, c = map(int, input().split())  
if a == b == c:
    print(10000 + a * 1000)
elif a == b or b == c or a == c:
    if a == b or a == c:
        print(1000 + a * 100)
    else:
        print(1000 + b * 100)
else:
    d = max(a, b, c)
    print(d * 100)


a = int(input()) 
for i in range(1, 10):
    print(f"{a} * {i} = {a*i}")


a = int(input()) 
for i in range(a):
    b, c = map(int, input().split())
    print(b + c)


a = int(input()) 
answer = 0
for i in range(a + 1): 
    answer += i
print(answer)


X = int(input())
N = int(input())
total = 0
for _ in range(N):
    a, b = map(int, input().split())
    total += a * b
if total == X:
    print("Yes")
else:
    print("No")


print(int(input())//4*'long ' + 'int')


import sys
m = int(input())
for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a + b)


a = int(input())
for i in range(a):
    b, c = map(int, input().split())
    print('Case #'+str(i+1)+':', b+c)


a = int(input())
for i in range(a):
    b, c = map(int, input().split())
    print('Case #'+str(i+1)+':', str(b) + ' + ' + str(c) + ' = ' + str(b+c))


a = int(input())
for i in range(1, a+1):
    print('*' *i)


a = int(input())
for i in range(1, a+1):
    print(' ' *(a-i) + '*' * i)


while True:
    b, c = map(int, input().split())
    if b == 0 and c == 0:
        break
    print(b + c)


while True:
    b, c = map(int, input().split())
    print(b + c)


while True:
    try:
        a, b = map(int, input().split())  
        print(a + b) 
    except EOFError:
        break


n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
print(numbers.count(m))


n, m = map(int, input().split()) 
numbers = list(map(int, input().split())) 
answer = 0
for num in numbers:
    if num < m:
        answer += 1
print(answer)


n, m= map(int, input().split())
a = list(map(int, input().split()))
result = [num for num in a if num < m]
print(*result)


a = int(input())
n = list(map(int, input().split()))
print(min(n), max(n))


numbers = [int(input()) for _ in range(9)]
max_value = max(numbers)
max_index = numbers.index(max_value) + 1
print(max_value, max_index)


import sys
import math

def find_positions(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) 
    if x1 == x2 and y1 == y2 and r1 == r2:
        return -1 
    if d > r1 + r2 or d < abs(r1 - r2):
        return 0  
    if d == r1 + r2 or d == abs(r1 - r2):
        return 1  
    return 2 
T = int(sys.stdin.readline()) 
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    print(find_positions(x1, y1, r1, x2, y2, r2))


import sys
N, M = map(int, sys.stdin.readline().split())
baskets = [0] * N 
for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for idx in range(i - 1, j):  
        baskets[idx] = k
print(*baskets)


N, M = map(int, input().split())  
baskets = [0] * N  
for _ in range(M):  
    i, j, k = map(int, input().split())  
    for idx in range(i - 1, j):  
        baskets[idx] = k  
print(*baskets) #* 리스트 또는 튜플의 개별 요소를 풀어서 출력


N, M = map(int, input().split())  
baskets = list(range(1, N + 1)) 
for _ in range(M):
    i, j = map(int, input().split())  
    baskets[i - 1], baskets[j - 1] = baskets[j - 1], baskets[i - 1] 
print(*baskets) #* 리스트 또는 튜플의 개별 요소를 풀어서 출력


submitted = {int(input()) for _ in range(28)}
missing = sorted(set(range(1, 31)) - submitted)
print(missing[0], missing[1])


remainders = {int(input()) % 42 for _ in range(10)}
print(len(remainders))


N = int(input())  
scores = list(map(int, input().split()))  
M = max(scores)  
new_scores = [(score / M) * 100 for score in scores]  
print(sum(new_scores) / N)  


N, M = map(int, input().split())  
baskets = list(range(1, N + 1))
for _ in range(M):
    i, j = map(int, input().split())  
    baskets[i-1:j] = reversed(baskets[i-1:j])
print(*baskets)


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    print(*[A[i][j] + B[i][j] for j in range(M)])


matrix = [list(map(int, input().split())) for _ in range(9)]
max_value = 0
max_position = (0, 0)
for i in range(9):
    for j in range(9):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_position = (i, j)
print(max_value)
print(max_position[0] + 1, max_position[1] + 1)


lines = [input() for _ in range(5)]
for i in range(15):  
    for line in lines: 
        if i < len(line):  
            print(line[i], end="") 


paper = [[0] * 100 for _ in range(100)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1
area = sum(sum(row) for row in paper)
print(area)


S = input()
a = int(input())
print(S[a-1])


S = input()
print(len(S))


a = int(input())
for _ in range(a):
    s = input()
    print(s[0] + s[-1])


char = input() 
print(ord(char))  


N = int(input()) 
numbers = input() 
total = sum(int(num) for num in numbers)
print(total)


s = input()
for char in 'abcdefghijklmnopqrstuvwxyz':
    print(s.find(char), end=' ')


a = int(input())
for _ in range(a):
    i, j = input().split()
    i = int(i)  
    result = ""
    for char in j:
        result += char * i
    print(result)


s = input().strip()
if not s:
    print(0)
else:
    print(len(s.split()))


i, j = input().split()
i = int(i[::-1]) 
j = int(j[::-1])
print(max(i, j))


while True:
    try:
        print(input())
    except:
        break


dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
s = input()
time = 0
for char in s:
    for i in range(len(dial)):
        if char in dial[i]:
            time += (i + 3)
            break
print(time)


while True:
    i, j = map(int, input().split())
    if i == 0 and j == 0:
        break
    if j % i == 0:
        print("factor")
    elif i % j == 0:
        print("multiple")
    else:
        print("neither")


i, j = map(int, input().split())
li = []
for a in range(1, i + 1):
    if i % a == 0:
        li.append(a)
if j <= len(li):
    print(li[j-1])
else:
    print(0)


while True:
    n = int(input())
    if n == -1:
        break
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    if sum(divisors) == n:
        print(f"{n} = {' + '.join(map(str, divisors))}")
    else:
        print(f"{n} is NOT perfect.")


a = int(input())
li = list(map(int, input().split()))
answer = 0
for l in li:
    if l == 1:
        continue
    is_prime = True
    for i in range(2, int(l ** 0.5) + 1):
        if l % i == 0:
            is_prime = False
            break
    if is_prime:
        answer += 1
print(answer)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
minv = int(input())
maxv = int(input())
minvv = None
sumv = 0
for i in range(minv, maxv + 1):
    if is_prime(i):
        sumv += i
        if minvv is None or minvv > i:
            minvv = i
if minvv is None:
    print(-1)
else:
    print(sumv)
    print(minvv)


a = int(input())
i = 2
while i * i <= a: 
    while a % i == 0: 
        print(i)
        a = a // i
    i += 1 
if a > 1:
    print(a)


N, B = input().split() 
B = int(B) 
result = int(N, B) 
print(result) 


n, b = map(int, input().split())
li = []
if n == 0:
    li.append(0)
else:
    while n > 0:
        remainder = n % b 
        if remainder < 10:
            li.append(str(remainder))
        else:
            li.append(chr(remainder - 10 + ord('A'))) 
        n = n // b  
print("".join(li[::-1]))


T = int(input())
for _ in range(T):
    C = int(input())
    quarters = C // 25  
    C %= 25  
    dimes = C // 10 
    C %= 10  
    nickels = C // 5 
    C %= 5 
    pennies = C  
    print(quarters, dimes, nickels, pennies)


N = int(input())
print((2**N+1)**2)


i, j, k = map(int, input().split()) 
day = 0
while k > 0:
    k = k - i  
    if k > 0: 
        k = k + j 
    day += 1
print(day)


A, B, V = map(int, input().split())
x = (V - B) / (A - B)
if x == int(x):
    print(int(x))
else:
    print(int(x) + 1)


a = int(input())
ans = 1
st = 1
while a > st:
    st += 6 * ans
    ans += 1
print(ans)


x = int(input())
line = 1
while x > line * (line + 1) // 2:
    line += 1
prev = (line - 1) * line // 2
idx = x - prev
if line % 2 == 1: 
    top = line - (idx - 1)
    bottom = 1 + (idx - 1)
else:
    top = 1 + (idx - 1)
    bottom = line - (idx - 1)
print(f'{top}/{bottom}')


x = int(input())
y = int(input())
print(x*y)


x, y, w, h = map(int, input().split())
print(min(h-y, w-x, x, y))


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4 = x1 ^ x2 ^ x3
y4 = y1 ^ y2 ^ y3
print(x4, y4)


a = int(input())
print(a*4)


a = int(input())
max_x = -float('inf') 
min_x = float('inf') 
max_y = -float('inf')
min_y = float('inf')
for _ in range(a):
    x, y = map(int, input().split()) 
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
    if x < min_x:
        min_x = x
    if y < min_y:
        min_y = y
print((max_x - min_x) * (max_y - min_y))


x = int(input())
y = int(input())
z = int(input())
if x == 60 and y == 60 and z == 60:
    print("Equilateral")
elif x + y + z == 180:
    if x == y or y == z or z == x:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")


while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if a + b <= c or a + c <= b or b + c <= a:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")


slide = sorted(list(map(int, input().split())))
if slide[0] + slide[1] > slide[2]:
    print(sum(slide))
else:
    print((slide[0] + slide[1]) * 2 - 1)


a = int(input()) 
li = []
for _ in range(a):
    i = int(input())  
    li.append(i) 
for num in sorted(li):
    print(num)


numbers = []
for _ in range(5):
    numbers.append(int(input()))
numbers.sort()
average = sum(numbers) // 5
median = numbers[2]
print(average)
print(median)


n, k = map(int, input().split())
scores = list(map(int, input().split()))
scores.sort(reverse=True)
print(scores[k-1])


N = int(input())  
numbers = [int(input()) for _ in range(N)] 
numbers.sort()
for num in numbers:
    print(num)


import sys
N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
numbers.sort()
sys.stdout.write("\n".join(map(str, numbers)) + "\n")


N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()
for num in numbers:
    print(num)


import sys
N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
numbers.sort()
sys.stdout.write("\n".join(map(str, numbers)) + "\n")


import sys
N = int(sys.stdin.readline())
numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))
numbers.sort()
sys.stdout.write("\n".join(map(str, numbers)) + "\n")


num = input()
li = [int(digit) for digit in num]
li.sort(reverse=True)
result = int(''.join(map(str, li)))
print(result)


a = int(input()) 
li = []
for _ in range(a):
    x, y = map(int, input().split()) 
    li.append((x, y)) 
li.sort()  
for l in li:
    print(l[0], l[1]) 


import sys
n = int(sys.stdin.readline())
count = [0] * 10001
for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1
output = []
for i in range(1, 10001):
    if count[i] != 0:
        output.extend([i] * count[i])
sys.stdout.write("\n".join(map(str, output)) + "\n")


import sys
def input():
    return sys.stdin.readline()
n = int(input())  
count = [0] * 10001 
for _ in range(n):
    num = int(input()) 
    count[num] += 1 
for i in range(1, 10001):
    if count[i] > 0:
        sys.stdout.write((str(i) + '\n') * count[i])  


a = int(input()) 
li = []
for _ in range(a):
    x, y = map(int, input().split()) 
    li.append((x, y)) 
li.sort(key=lambda coord: (coord[1], coord[0])) 
for l in li:
    print(l[0], l[1])


a = int(input())
words = set()
for _ in range(a):
    words.add(input().strip())
sorted_words = sorted(words, key=lambda x: (len(x), x))
for word in sorted_words:
    print(word)


a = int(input())
li = []
for _ in range(a):
    x, y = input().split()
    li.append((x, y)) 
li.sort(key=lambda x: (len(x[0]), x[0]))
for l in li:
    print(l[0], l[1])


n = int(input())
coordinates = list(map(int, input().split()))  
sorted_coordinates = sorted(set(coordinates))
coordinate_map = {v: i for i, v in enumerate(sorted_coordinates)}
result = [coordinate_map[x] for x in coordinates]
print(*result)


a1, a0 = map(int, input().split())  
c = int(input()) 
n0 = int(input())  
def check_O_n(a1, a0, c, n0):
    for n in range(n0, 101):
        if a1 * n + a0 > c * n:
            return 0  
    return 1 
print(check_O_n(a1, a0, c, n0))


import itertools
N, M = map(int, input().split()) 
cards = list(map(int, input().split())) 
combinations = itertools.combinations(cards, 3)
max_sum = 0
for comb in combinations:
    comb_sum = sum(comb)
    if comb_sum <= M and comb_sum > max_sum:
        max_sum = comb_sum
print(max_sum)


def find_smallest_creator(N):
    start = max(1, N - 9 * len(str(N)))
    for M in range(start, N):
        if M + sum(map(int, str(M))) == N:
            return M
    return 0
N = int(input())
print(find_smallest_creator(N))


a, b, c, d, e, f = map(int, input().split())
x = (c * f - b * d) / (a * f - b * e)
y = (d - e * x) / f
print(x, y)


N = int(input()) 
count = 0  
num = 666 
while True:
    if '666' in str(num):
        count += 1  
        if count == N: 
            print(num)  
            break 
    num += 1 


N = int(input())
answer = -1
for i in range(N // 5, -1, -1):
    remaining = N - (i * 5)
    if remaining % 3 == 0:
        answer = i + (remaining // 3)
        break
print(answer)


grade_point = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}
total_score = 0.0
total_nums = 0.0
for _ in range(20):
    subject, num, grade = input().split()
    credit = float(num)  
    if grade != "P": 
        total_score += credit * grade_point[grade]
        total_nums += credit 
gpa = total_score / total_nums
print(f"{gpa:.6f}")


croatian_alphabets = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
word = input().strip()
count = 0
i = 0
while i < len(word):
    if i + 1 < len(word) and word[i:i+2] in croatian_alphabets:
        count += 1
        i += 2
    elif i + 2 < len(word) and word[i:i+3] == 'dz=':
        count += 1
        i += 3
    else:
        count += 1
        i += 1
print(count)


from collections import Counter
a = input().strip()
a = a.lower()  
alphabet_count = Counter(a)
max_count = max(alphabet_count.values())
most_common = [char for char, count in alphabet_count.items() if count == max_count]
if len(most_common) > 1:
    print('?')
else:
    print(most_common[0].upper())


a = input().strip()
a = a.lower() 
if a == a[::-1]: 
    print(1)
else:
    print(0)


k, q, l, v, n, p = 1, 1, 2, 2, 2, 8 
a, b, c, d, e, f = map(int, input().split())
answer = [k - a, q - b, l - c, v - d, n - e, p - f]
print(*answer)


n = int(input())
count = 0
for _ in range(n):
    word = input()
    is_group = True
    for char in set(word):  
        if word.find(char) != word.rfind(char): 
            if word.find(char) + word.count(char) != word.rfind(char) + 1:  
                is_group = False
                break
    if is_group:
        count += 1
print(count)


n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))


a = int(input())
have = set(map(int, input().split()))
b = int(input())
card = list(map(int, input().split()))
answer = []
for i in card:
    if i in have:
        answer.append(1)
    else:
        answer.append(0)
print(*answer)


import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = set(input().strip() for _ in range(n))
cnt = sum(1 for _ in range(m) if input().strip() in s)
print(cnt)


n = int(input())
pers = set()
for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        pers.add(name)
    else:
        pers.remove(name)
print('\n'.join(sorted(pers, reverse=True)))


import sys
input = sys.stdin.readline
N, M = map(int, input().split())
pokemon_name = {}
pokemon_number = {}
for i in range(1, N+1):
    name = input().strip()
    pokemon_name[i] = name
    pokemon_number[name] = i
for _ in range(M):
    query = input().strip()
    if query.isdigit():
        print(pokemon_name[int(query)])
    else:
        print(pokemon_number[query])


N, M = map(int, input().split())
pokemon_name = {}
pokemon_number = {}
for i in range(1, N+1):
    name = input().strip()
    pokemon_name[i] = name
    pokemon_number[name] = i
for _ in range(M):
    query = input().strip()
    if query.isdigit():
        print(pokemon_name[int(query)])
    else:
        print(pokemon_number[query])


from collections import Counter
a = int(input())
numbers = list(map(int, input().split()))
count = Counter(numbers)
b = int(input())
number = list(map(int, input().split()))
answer = []
for numb in number:
    if numb in count:
        answer.append(count[numb])
    else:
        answer.append(0)
print(*answer)


n, m = map(int, input().split())
heard = set()
seen = set()
for _ in range(n):
    heard.add(input().strip())
for _ in range(m):
    seen.add(input().strip())
result = sorted(heard & seen)
print(len(result))
for name in result:
    print(name)


a, b = map(int, input().split())
alist = list(map(int, input().split()))
aset = set(alist)
blist = list(map(int, input().split()))
bset = set(blist)
x = len(aset - bset)
y = len(bset - aset)
print(x + y)


string = input().strip()
substrings = set()
for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        substrings.add(string[i:j])
print(len(substrings))


N = int(input()) 
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort()
for num in nums:
    print(num)


N = int(input()) 
count = [0] * 10001 
for _ in range(N):
    num = int(input())
    count[num] += 1
for i in range(1, 10001):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)


import sys
N = int(sys.stdin.readline())
nums = [0] * 10001 
for _ in range(N):
    num = int(sys.stdin.readline())
    nums[num] += 1 
output = []
for i in range(1, 10001):
    if nums[i] > 0:
        output.extend([str(i)] * nums[i]) 
sys.stdout.write("\n".join(output) + "\n")


import math
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)
a = int(input())
for _ in range(a):
    x, y = map(int, input().split())
    print(lcm(x, y))

import math
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)
x, y = map(int, input().split())  
print(lcm(x, y))  


import math
a, b = map(int, input().split())
c, d = map(int, input().split()) 
numerator = a * d + b * c  
denominator = b * d  
gcd_value = math.gcd(numerator, denominator) 
print(numerator // gcd_value, denominator // gcd_value)


a = int(input())  
li = []
for _ in range(a):
    i = int(input())
    li.append(i)
li.sort() 
answer = []
for i in range(1, len(li)):
    diff = li[i] - li[i-1] 
    if diff > 1:
        for j in range(1, diff):
            answer.append(li[i-1] + j)
answer = li + answer 
print(len(answer))


import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
a = int(input())
for _ in range(a):
    n = int(input())
    while not is_prime(n):
        n += 1
    print(n)


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0: 
        return False
    for i in range(3, int(n ** 0.5) + 1, 2): 
        if n % i == 0:
            return False
    return True
a, b = map(int, input().split())
for i in range(a, b + 1):
    if is_prime(i):
        print(i)


a, b = map(int, input().split())
sieve = [True] * (b + 1)
sieve[0] = sieve[1] = False
for i in range(2, int(b**0.5) + 1):
    if sieve[i]:
        for j in range(i * i, b + 1, i):
            sieve[j] = False
for i in range(a, b + 1):
    if sieve[i]:
        print(i)


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
while True:
    a = int(input())
    if a == 0:
        break
    answer = 0
    for i in range(a + 1, 2 * a + 1):
        if is_prime(i):
            answer += 1
    print(answer)


def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return sieve
limit = 2 * 123456 
prime_sieve = sieve_of_eratosthenes(limit)
while True:
    a = int(input())
    if a == 0:
        break
    answer = sum(1 for i in range(a + 1, 2 * a + 1) if prime_sieve[i])
    print(answer)


import math
def count_open_windows(n):
    return int(math.sqrt(n))
N = int(input())
print(count_open_windows(N))


import math
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime
def goldbach_partition_count(n, is_prime):
    count = 0
    for i in range(2, n // 2 + 1):
        if is_prime[i] and is_prime[n - i]:
            count += 1
    return count
T = int(input())
test_cases = [int(input()) for _ in range(T)]
max_n = max(test_cases)
is_prime = sieve_of_eratosthenes(max_n)
for n in test_cases:
    print(goldbach_partition_count(n, is_prime))


import sys
input = sys.stdin.read
data = input().strip().splitlines()
n = int(data[0])
commands = data[1:]
stack = []
output = []
for cmd in commands:
    parts = cmd.split()
    if parts[0] == '1':
        stack.append(int(parts[1]))
    elif parts[0] == '2':
        output.append(str(stack.pop()) if stack else '-1')
    elif parts[0] == '3':
        output.append(str(len(stack)))
    elif parts[0] == '4':
        output.append('1' if not stack else '0')
    elif parts[0] == '5':
        output.append(str(stack[-1]) if stack else '-1')
print("\n".join(output))


a = int(input())
answer = []
for _ in range(a):
    i = int(input())
    if i == 0 and answer:
        answer.pop()
    else:
        answer.append(i)
print(sum(answer))


a = int(input())
for _ in range(a):
    i = input()
    while '()' in i:
        i = i.replace('()', '')
    if i == '':
        print('YES')
    else:
        print('NO')


from collections import deque
queue = deque()
a = int(input())
for _ in range(a):
    i = input().split()
    if i[0] == 'push':
        queue.append(i[1])
    elif i[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif i[0] == 'size':
        print(len(queue))
    elif i[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif i[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif i[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)


import sys
from collections import deque
queue = deque()
a = int(input())
commands = sys.stdin.read().splitlines()
for command in commands:
    i = command.split()
    if i[0] == 'push':
        queue.append(i[1])
    elif i[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif i[0] == 'size':
        print(len(queue))
    elif i[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif i[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif i[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)


from collections import deque
n = int(input()) 
queue = deque(range(1, n + 1))
while len(queue) > 1:
    queue.popleft()  
    queue.append(queue.popleft())  
print(queue[0])


from collections import deque
queue = deque()
answer = []
a, b = map(int, input().split())
for i in range(1, a + 1):
    queue.append(i)
while len(queue) > 0:
    queue.rotate(-(b-1))
    popped_value = queue.popleft()
    answer.append(popped_value)
print("<", end="")
print(", ".join(map(str, answer)), end="")
print(">")


from collections import deque
queue = deque()
a = int(input())
for _ in range(a):
    cmd = input().split()
    if cmd[0] == "1":
        queue.appendleft(int(cmd[1]))
    elif cmd[0] == "2":
        queue.append(int(cmd[1]))
    elif cmd[0] == "3":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd[0] == "4":
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif cmd[0] == "5":
        print(len(queue))
    elif cmd[0] == "6":
        if queue:
            print(0)
        else:
            print(1)
    elif cmd[0] == "7":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd[0] == "8":
        if queue:
            print(queue[-1])
        else:
            print(-1)


from collections import deque
import sys
input = sys.stdin.read
queue = deque()
commands = input().splitlines()
N = int(commands[0])
output = []
for i in range(1, N + 1):
    cmd = commands[i].split()
    if cmd[0] == "1":
        queue.appendleft(int(cmd[1]))
    elif cmd[0] == "2":
        queue.append(int(cmd[1]))
    elif cmd[0] == "3":
        if queue:
            output.append(str(queue.popleft()))
        else:
            output.append("-1")
    elif cmd[0] == "4":
        if queue:
            output.append(str(queue.pop()))
        else:
            output.append("-1")
    elif cmd[0] == "5":
        output.append(str(len(queue)))
    elif cmd[0] == "6":
        if queue:
            output.append("0")
        else:
            output.append("1")
    elif cmd[0] == "7":
        if queue:
            output.append(str(queue[0]))
        else:
            output.append("-1")
    elif cmd[0] == "8":
        if queue:
            output.append(str(queue[-1]))
        else:
            output.append("-1")
sys.stdout.write("\n".join(output) + "\n")


n = int(input())  
queue = list(map(int, input().split())) 
stack = []
target = 1 
for student in queue:
    stack.append(student)
    while stack and stack[-1] == target:
        stack.pop() 
        target += 1  
if target == n + 1:
    print("Nice")
else:
    print("Sad")


A = input()
B = input()
C = input()
print(int(A) + int(B) - int(C))
print(int(A + B) - int(C))


scale = {
    'c': 1, 'd': 2, 'e': 3, 'f': 4, 'g': 5, 'a': 6, 'b': 7, 'C': 8
}
num = input().split()
if num == [str(i) for i in range(1, 9)]:
    print("ascending")
elif num == [str(i) for i in range(8, 0, -1)]:
    print("descending")
else:
    print("mixed")


a = int(input())
b = int(input())
c = int(input())
num = a * b * c
nu = str(num)
answer = []
for n in range(10):  
    answer.append(nu.count(str(n)))
print(*answer)


T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split()) 
    floor = (N - 1) % H + 1  
    room = (N - 1) // H + 1 
    print(f"{floor}{room:02d}") 


a = int(input())
for i in range(1,a+1):
    print(i)


a, b, c, d, e = map(int, input().split())
num = a**2 + b**2 + c**2 + d**2 + e**2
answer = num%10
print(answer)


t = int(input())
for _ in range(t):
    result = input().strip()
    score = 0
    current_streak = 0
    for char in result:
        if char == 'O':
            current_streak += 1
            score += current_streak
        else:
            current_streak = 0
    print(score)


while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print('right')
    else:
        print('wrong')


import math
N = int(input())
S, M, L, XL, XXL, XXXL = map(int, input().split())
T, P = map(int, input().split())
shirts = [S, M, L, XL, XXL, XXXL]
total_shirt_bundles = sum(math.ceil(size / T) for size in shirts)
pen_bundles = N // P
pen_remainder = N % P
print(total_shirt_bundles)
print(pen_bundles, pen_remainder)


L = int(input())
text = input()
result = sum((ord(char) - ord('a') + 1) * (31**i) for i, char in enumerate(text))
print(result)


while True:
    num = input().strip()
    if num == '0':
        break
    if num == num[::-1]:
        print('yes')
    else:
        print('no')


a, b = map(int, input().split())
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)
print(gcd(a, b)) 
print(lcm(a, b))


a = int(input())
for _ in range(a):
    k = int(input())
    n = int(input())
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(1, n + 1):
        dp[0][i] = i
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp[k][n])


n = int(input())
count = 0
i = 5
while n >= i:
    count += n // i 
    i *= 5  
print(count)


i = int(input())
stack = []
for _ in range(i):
    li = input().split()
    if li[0] == 'push':
        stack.append(int(li[1]))
    elif li[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif li[0] == 'size':
        print(len(stack))
    elif li[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif li[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)


import sys
input = sys.stdin.read
data = input().splitlines()
i = int(data[0])
stack = []
result = []
for j in range(1, i + 1):
    li = data[j].split()
    if li[0] == 'push':
        stack.append(int(li[1]))
    elif li[0] == 'pop':
        if stack:
            result.append(str(stack.pop()))
        else:
            result.append("-1")
    elif li[0] == 'size':
        result.append(str(len(stack)))
    elif li[0] == 'empty':
        if stack:
            result.append("0")
        else:
            result.append("1")
    elif li[0] == 'top':
        if stack:
            result.append(str(stack[-1]))
        else:
            result.append("-1")
sys.stdout.write("\n".join(result) + "\n")


n, k = map(int, input().split())
ans = 1
wer = 1
for i in range(n, n - k, -1):
    ans *= i
for j in range(1, k + 1):
    wer *= j
print(ans // wer)


str1 = input().strip()
str2 = input().strip()
str3 = input().strip()
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)
num = 1
while True:
    if fizzbuzz(num) == str1 and fizzbuzz(num + 1) == str2 and fizzbuzz(num + 2) == str3:
        print(fizzbuzz(num + 3))
        break
    num += 1


import sys
from collections import deque
input = sys.stdin.read
data = input().splitlines()  
i = int(data[0])
queue = deque()  
result = []
for j in range(1, i + 1):
    li = data[j].split()
    if li[0] == 'push':
        queue.append(int(li[1]))  
    elif li[0] == 'pop':
        if queue:
            result.append(str(queue.popleft()))
        else:
            result.append("-1")
    elif li[0] == 'size':
        result.append(str(len(queue)))
    elif li[0] == 'empty':
        if queue:
            result.append("0")  
        else:
            result.append("1")  
    elif li[0] == 'front':
        if queue:
            result.append(str(queue[0]))  
        else:
            result.append("-1")
    elif li[0] == 'back':
        if queue:
            result.append(str(queue[-1])) 
        else:
            result.append("-1")
sys.stdout.write("\n".join(result) + "\n")


n = int(input())  
sequence = [int(input()) for _ in range(n)]  
stack = []
result = []
current = 1  
for num in sequence:
    while current <= num:  
        stack.append(current)
        result.append('+')
        current += 1
    if stack[-1] == num: 
        stack.pop()
        result.append('-')
    else: 
        print("NO")
        exit()
for op in result:
    print(op)


K, N = map(int, input().split())  
cable_lengths = [int(input()) for _ in range(K)]
max_length = max(cable_lengths)  
min_length = min(cable_lengths)  
for length in range(max_length, min_length - 1, -1):
    count = sum(cable // length for cable in cable_lengths)  
    if count >= N:  
        print(length)
        break


K, N = map(int, input().split())  
cable_lengths = [int(input()) for _ in range(K)]
left, right = 1, max(cable_lengths)  
while left <= right:
    mid = (left + right) // 2  
    count = sum(cable // mid for cable in cable_lengths)  
    if count >= N:  
        left = mid + 1  
    else:  
        right = mid - 1  
print(right)


from collections import Counter
a = int(input())
lists = [int(input()) for _ in range(a)]
lists.sort()
mean = round(sum(lists) / len(lists))  
median = lists[len(lists) // 2]  
count = Counter(lists)
max_freq = max(count.values())
modes = [k for k, v in count.items() if v == max_freq]
modes.sort()
mode = modes[0] if len(modes) == 1 else modes[1]  
range_value = lists[-1] - lists[0]  
print(mean)
print(median)
print(mode)
print(range_value)


import sys
from collections import Counter
input = sys.stdin.read
data = input().split()
a = int(data[0])
lists = list(map(int, data[1:]))
lists.sort()
mean = round(sum(lists) / a)
median = lists[a // 2]
count = Counter(lists)
max_freq = max(count.values())
modes = [k for k, v in count.items() if v == max_freq]
modes.sort()
mode = modes[0] if len(modes) == 1 else modes[1]
range_value = lists[-1] - lists[0]
print(mean)
print(median)
print(mode)
print(range_value)


import sys
from collections import deque
input = sys.stdin.read
data = input().split()
idx = 0
t = int(data[idx])
idx += 1
results = []
for _ in range(t):
    N, M = map(int, [data[idx], data[idx+1]])
    idx += 2
    priorities = list(map(int, data[idx:idx+N]))
    idx += N
    queue = deque((priority, i) for i, priority in enumerate(priorities))
    order = 0  
    while queue:
        if queue[0][0] < max(queue, key=lambda x: x[0])[0]:
            queue.append(queue.popleft())  
        else:
            order += 1  
            if queue.popleft()[1] == M:
                results.append(str(order))
                break  
print("\n".join(results))


a = int(input())  
a_list = set(map(int, input().split()))   
b = int(input())  
b_list = map(int, input().split())  
for bl in b_list:
    print(1 if bl in a_list else 0) 


N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]
min_repaints = float('inf')
for i in range(N - 7):
    for j in range(M - 7):
        w_start, b_start = 0, 0
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0:
                    if board[i + x][j + y] != 'W':
                        w_start += 1  
                    if board[i + x][j + y] != 'B':
                        b_start += 1 
                else:
                    if board[i + x][j + y] != 'B':
                        w_start += 1
                    if board[i + x][j + y] != 'W':
                        b_start += 1
        min_repaints = min(min_repaints, w_start, b_start)
print(min_repaints)


import sys

N, M = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(N)]
patterns = ["WBWBWBWB", "BWBWBWBW"]
min_repaints = float('inf')
for i in range(N - 7):
    for j in range(M - 7):
        w_start, b_start = 0, 0
        for x in range(8):
            row = board[i + x][j:j + 8]
            correct_w = patterns[x % 2]
            correct_b = patterns[(x + 1) % 2]
            for y in range(8):
                if row[y] != correct_w[y]:
                    w_start += 1
                if row[y] != correct_b[y]:
                    b_start += 1
        min_repaints = min(min_repaints, w_start, b_start)
print(min_repaints)


import sys
import numpy as np
N, M = map(int, sys.stdin.readline().split())
board = np.array([list(sys.stdin.readline().strip()) for _ in range(N)])
pattern_w = np.array([list("WBWBWBWB"), list("BWBWBWBW")] * 4)
pattern_b = np.array([list("BWBWBWBW"), list("WBWBWBWB")] * 4)
min_repaints = float('inf')
for i in range(N - 7):
    for j in range(M - 7):
        sub_board = board[i:i+8, j:j+8]
        w_start = np.sum(sub_board != pattern_w)
        b_start = np.sum(sub_board != pattern_b)
        min_repaints = min(min_repaints, w_start, b_start)
print(min_repaints)


N = int(input())  
people = [list(map(int, input().split())) for _ in range(N)]  
for i in range(N):  
    rank = 1  
    for j in range(N):  
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:  
            rank += 1  
    print(rank, end=" ")


import sys
N = int(sys.stdin.readline())
people = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
ranks = []
for i in range(N):
    rank = 1
    for j in range(N):
        if i != j and people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    ranks.append(str(rank))
print(" ".join(ranks))


import sys
a = int(sys.stdin.readline())
answer = set()
for _ in range(a):
    command = sys.stdin.readline().split()
    if command[0] == 'add':
        answer.add(int(command[1]))
    elif command[0] == 'remove':
        answer.discard(int(command[1]))  
    elif command[0] == 'check':
        print(1 if int(command[1]) in answer else 0) 
    elif command[0] == 'toggle':
        num = int(command[1])
        if num in answer:
            answer.remove(num)
        else:
            answer.add(num)
    elif command[0] == 'all':
        answer = set(range(1, 21))
    elif command[0] == 'empty':
        answer.clear()


a = int(input())
answer = set()
for _ in range(a):
    command = input().split()
    if command[0] == 'add':
        answer.add(int(command[1]))
    elif command[0] == 'remove':
        answer.discard(int(command[1]))  
    elif command[0] == 'check':
        print(1 if int(command[1]) in answer else 0)  
    elif command[0] == 'toggle':
        num = int(command[1])
        if num in answer:
            answer.remove(num)
        else:
            answer.add(num)
    elif command[0] == 'all':
        answer = set(range(1, 21))
    elif command[0] == 'empty':
        answer.clear()


n, k = map(int, input().split())  
coins = sorted([int(input()) for _ in range(n)], reverse=True)  
ans = 0  
for coin in coins:  
    if coin <= k:  
        ans += k // coin  
        k %= coin  
print(ans)


N = int(input())  
P = list(map(int, input().split()))  
P.sort() 
total_time = 0  
waiting_time = 0  
for time in P:  
    waiting_time += time   
    total_time += waiting_time  
print(total_time)


import sys
zero = [0] * 41
one = [0] * 41
zero[0] = 1
one[0] = 0
zero[1] = 0
one[1] = 1
for i in range(2, 41):
    zero[i] = zero[i-1] + zero[i-2]
    one[i] = one[i-1] + one[i-2]
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(zero[N], one[N])


n = int(input())
dp = [0] * (n + 1)
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
print(dp[n])


a = int(input())
dp = [0] * 12 
dp[1], dp[2], dp[3] = 1, 2, 4 
for i in range(4, 12): 
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for _ in range(a):
    n = int(input())
    print(dp[n])


import sys
n, m = map(int, sys.stdin.readline().split())
dic = {}
for _ in range(n):
    web, password = sys.stdin.readline().split()
    dic[web] = password
for _ in range(m):
    site = sys.stdin.readline().strip()
    print(dic[site])


import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    dic = {}
    for _ in range(n):
        name, types = sys.stdin.readline().split()
        if types not in dic:
            dic[types] = []
        dic[types].append(name)
    result = 1
    for types in dic:
        result *= (len(dic[types]) + 1)
    print(result - 1)


a, b = map(int, input().split())  
nums = list(map(int, input().split()))  
prefix = [0] * (a + 1)  
for i in range(a):  
    prefix[i + 1] = prefix[i] + nums[i]  
for _ in range(b):  
    m, n = map(int, input().split())  
    print(prefix[n] - prefix[m - 1])


import sys
a, b = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
prefix = [0] * (a + 1)
for i in range(a):
    prefix[i + 1] = prefix[i] + nums[i]
output = []
for _ in range(b):
    m, n = map(int, sys.stdin.readline().split())
    output.append(str(prefix[n] - prefix[m - 1]))
sys.stdout.write("\n".join(output) + "\n")


n = int(input())
dp = [0] * (n + 1)
dp[1] = 1
if n > 1:
    dp[2] = 2
for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
print(dp[n])


n = int(input())
dp = [0] * (n + 1)
dp[1] = 1
if n > 1:
    dp[2] = 3 
for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007
print(dp[n])


import math
def min_square_count(n):
    count = 0
    while n > 0:
        max_square = int(math.sqrt(n))
        n -= max_square * max_square
        count += 1
    return count
n = int(input())
print(min_square_count(n))


from collections import deque
def bfs(n, m, grid, start_x, start_y):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    distance = [[-1] * m for _ in range(n)]    
    queue = deque([(start_x, start_y)])
    distance[start_x][start_y] = 0    
    while queue:
        x, y = queue.popleft()        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy            
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                distance[i][j] = 0
            elif distance[i][j] == -1:
                distance[i][j] = -1
    return distance
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            start_x, start_y = i, j
            break
result = bfs(n, m, grid, start_x, start_y)
for row in result:
    print(" ".join(map(str, row)))


N = int(input())  
M = int(input())  
graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1  
stack = [1]
visited[1] = True
count = 0  
while stack:
    node = stack.pop()    
    for i in range(1, N + 1):
        if graph[node][i] == 1 and not visited[i]:  
            visited[i] = True  
            stack.append(i)
            count += 1  
print(count)


import sys
from collections import deque
input = sys.stdin.read
data = input().split("\n")
T = int(data[0])  
index = 1  
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y, field, visited, M, N):
    queue = deque([(x, y)])
    visited[y][x] = True  
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if field[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((nx, ny))
results = []
for _ in range(T):
    M, N, K = map(int, data[index].split())
    index += 1
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, data[index].split())
        field[y][x] = 1
        index += 1
    worm_count = 0
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1 and not visited[y][x]:
                bfs(x, y, field, visited, M, N)
                worm_count += 1  
    results.append(str(worm_count))
print("\n".join(results))


from collections import deque
N = int(input())
grid = [list(map(int, input().strip())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * N for _ in range(N)]
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if grid[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1
    return count
complexes = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and not visited[i][j]:
            complexes.append(bfs(i, j))
print(len(complexes))
for num in sorted(complexes):
    print(num)


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
for row in graph:
    print(' '.join(map(str, row)))


import heapq
import sys
input = sys.stdin.read
def solve():
    data = input().splitlines()
    heap = []
    N = int(data[0])
    result = []    
    for i in range(1, N+1):
        x = int(data[i])       
        if x != 0:
            heapq.heappush(heap, (abs(x), x))
        else:
            if heap:
                _, value = heapq.heappop(heap)
                result.append(str(value))
            else:
                result.append("0")    
    sys.stdout.write("\n".join(result) + "\n")
solve()


def find_pn(N, S):
    PN = "IO" * N + "I"
    PN_len = len(PN)
    count = 0   
    for i in range(len(S) - PN_len + 1):
        if S[i:i+PN_len] == PN:
            count += 1            
    return count
N = int(input())
M = int(input())
S = input()
print(find_pn(N, S))


from collections import deque
def bfs(N, K):
    visited = [False] * 100001
    queue = deque([(N, 0)])
    visited[N] = True
    while queue:
        current, steps = queue.popleft()
        if current == K:
            return steps
        for next_position in [current - 1, current + 1, current * 2]:
            if 0 <= next_position <= 100000 and not visited[next_position]:
                visited[next_position] = True
                queue.append((next_position, steps + 1))
    return -1
N, K = map(int, input().split())
print(bfs(N, K))


def find_min_steps(N, K):
    steps = 0
    while N != K:
        if K // 2 > N:
            K *= 2
        else:
            if K > N:
                K -= 1
            else:
                K += 1
        steps += 1
    return steps
N, K = map(int, input().split())
print(find_min_steps(N, K))


from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(maze, N, M):
    queue = deque([(0, 0)])
    maze[0][0] = 1    
    while queue:
        x, y = queue.popleft()        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1
    return maze[N-1][M-1]
N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
print(bfs(maze, N, M))


from collections import deque
def bfs(start, n, graph):
    dist = [-1] * (n + 1)
    dist[start] = 0
    queue = deque([start])
    while queue:
        node = queue.popleft()        
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)    
    return sum(dist[1:])
def find_kevin_bacon(n, m, relationships):
    graph = [[] for _ in range(n + 1)]    
    for a, b in relationships:
        graph[a].append(b)
        graph[b].append(a)    
    min_bacon = float('inf')
    person = -1    
    for i in range(1, n + 1):
        bacon_number = bfs(i, n, graph)        
        if bacon_number < min_bacon:
            min_bacon = bacon_number
            person = i    
    return person
n, m = map(int, input().split())
relationships = [tuple(map(int, input().split())) for _ in range(m)]
print(find_kevin_bacon(n, m, relationships))


from collections import defaultdict
def max_fruit_tanghuru(N, fruits):
    left = 0
    max_len = 0
    fruit_count = defaultdict(int)
    for right in range(N):
        fruit_count[fruits[right]] += 1
        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1       
        max_len = max(max_len, right - left + 1)
    return max_len
N = int(input())
fruits = list(map(int, input().split()))
result = max_fruit_tanghuru(N, fruits)
print(result)


from collections import deque
def bfs(N, M, campus):
    start_x, start_y = -1, -1
    for i in range(N):
        for j in range(M):
            if campus[i][j] == 'I':
                start_x, start_y = i, j
                break
        if start_x != -1:
            break
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start_x, start_y)])
    visited = [[False] * M for _ in range(N)]
    visited[start_x][start_y] = True   
    people_count = 0
    while queue:
        x, y = queue.popleft()
        if campus[x][y] == 'P':
            people_count += 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if campus[nx][ny] != 'X':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    if people_count == 0:
        return "TT"
    else:
        return str(people_count)
N, M = map(int, input().split())
campus = [list(input()) for _ in range(N)]
print(bfs(N, M, campus))


n = int(input())  
score = [int(input()) for _ in range(n)]  
if n == 1:
    print(score[0])
elif n == 2:
    print(score[0] + score[1])
else:
    dp = [0] * n  
    dp[0] = score[0]  
    dp[1] = score[0] + score[1]  
    for i in range(2, n):
        dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])
    print(dp[n-1])


import sys
sys.setrecursionlimit(10**6)
def dfs(graph, visited, node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)
def count_connected_components(N, M, edges):
    graph = {i: [] for i in range(1, N + 1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)    
    visited = [False] * (N + 1)
    count = 0
    for node in range(1, N + 1):
        if not visited[node]:
            dfs(graph, visited, node)
            count += 1            
    return count
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
result = count_connected_components(N, M, edges)
print(result)


from collections import deque
def bfs(graph, visited, node):
    queue = deque([node])
    visited[node] = True
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
def count_connected_components(N, M, edges):
    graph = {i: [] for i in range(1, N + 1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)    
    visited = [False] * (N + 1
    count = 0    
    for node in range(1, N + 1):
        if not visited[node]:
            bfs(graph, visited, node)
            count += 1            
    return count
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
result = count_connected_components(N, M, edges)
print(result)


import sys
sys.setrecursionlimit(10**6)
def dfs(graph, visited, node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)
def count_connected_components(N, M, edges):
    graph = {i: [] for i in range(1, N + 1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * (N + 1)
    count = 0
    for node in range(1, N + 1):
        if not visited[node]:
            dfs(graph, visited, node)
            count += 1     
    return count
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
result = count_connected_components(N, M, edges)
print(result)


import heapq
import sys
input = sys.stdin.read
data = input().splitlines()
N = int(data[0])
heap = []
for i in range(1, N + 1):
    x = int(data[i])
    if x == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -x)


def get_cut_length(trees, height):
    length = 0
    for tree in trees:
        if tree > height:
            length += tree - height
    return length
N, M = map(int, input().split())
trees = list(map(int, input().split()))
max_height = max(trees)
result = 0
for height in range(max_height + 1):
    cut_length = get_cut_length(trees, height)
    if cut_length >= M:
        result = height
print(result)


def count_paper(x, y, size):
    color = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                half_size = size // 2
                count_paper(x, y, half_size)
                count_paper(x + half_size, y, half_size)
                count_paper(x, y + half_size, half_size)
                count_paper(x + half_size, y + half_size, half_size)
                return
    if color == 0:
        white[0] += 1
    else:
        blue[0] += 1
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white = [0]
blue = [0]
count_paper(0, 0, N)
print(white[0])
print(blue[0])


import sys
import heapq
input = sys.stdin.read
data = input().splitlines()
N = int(data[0]) 
heap = []
result = []
for i in range(1, N + 1):
    x = int(data[i])
    if x == 0:
        if heap:
            result.append(str(heapq.heappop(heap))) 
        else:
            result.append("0")  
    else:
        heapq.heappush(heap, x)  
sys.stdout.write("\n".join(result) + "\n") 


expression = input().strip()
groups = expression.split('-')
result = sum(map(int, groups[0].split('+')))
for group in groups[1:]:
    result -= sum(map(int, group.split('+')))
print(result)


def get_cut_length(trees, height):
    length = 0
    for tree in trees:
        if tree > height:
            length += tree - height
    return length
def binary_search(trees, M):
    low = 0
    high = max(trees)
    answer = 0    
    while low <= high:
        mid = (low + high) // 2
        cut_length = get_cut_length(trees, mid)        
        if cut_length >= M:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1    
    return answer
N, M = map(int, input().split())
trees = list(map(int, input().split()))
result = binary_search(trees, M)
print(result)


from collections import deque
import sys
input = sys.stdin.read
data = input().splitlines()
N, M, V = map(int, data[0].split())
graph = {i: set() for i in range(1, N + 1)}
for i in range(1, M + 1):
    a, b = map(int, data[i].split())
    graph[a].add(b)
    graph[b].add(a)
def dfs(v, visited):
    stack = [v]
    result = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack.extend(sorted(graph[node], reverse=True)) 
    print(*result)
def bfs(v):
    queue = deque([v])
    visited = {v}
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for next_node in sorted(graph[node]): 
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)
    print(*result)
dfs(V, set()) 
bfs(V) 


import sys
import heapq
def D(n): return (n * 2) % 10000
def S(n): return 9999 if n == 0 else n - 1
def L(n): return (n % 1000) * 10 + n // 1000
def R(n): return (n % 10) * 1000 + n // 10
def dijkstra(A, B):
    heap = [(0, A, "")]
    visited = [False] * 10000
    while heap:
        cost, num, path = heapq.heappop(heap)
        if num == B:
            return path
        if visited[num]:
            continue
        visited[num] = True
        for op, func in zip("DSLR", [D, S, L, R]):
            new_num = func(num)
            if not visited[new_num]:
                heapq.heappush(heap, (cost + 1, new_num, path + op))
T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(dijkstra(A, B))


import sys
from collections import deque
def D(n): return (n * 2) % 10000
def S(n): return 9999 if n == 0 else n - 1
def L(n): return (n % 1000) * 10 + n // 1000
def R(n): return (n % 10) * 1000 + n // 10
def bfs(A, B):
    queue = deque([(A, "")])  
    visited = [False] * 10000
    visited[A] = True
    while queue:
        num, path = queue.popleft()        
        if num == B:
            return path        
        for op, func in zip("DSLR", [D, S, L, R]):
            new_num = func(num)
            if not visited[new_num]:  
                visited[new_num] = True
                queue.append((new_num, path + op))
T = int(sys.stdin.readline().strip())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(bfs(A, B))


import sys
from collections import deque
def D(n): return (n * 2) % 10000
def S(n): return 9999 if n == 0 else n - 1
def L(n): return (n % 1000) * 10 + n // 1000
def R(n): return (n % 10) * 1000 + n // 10
def bfs(A, B):
    queue = deque([(A, "")])
    visited = [False] * 10000
    visited[A] = True
    while queue:
        num, path = queue.popleft()
        if num == B:
            return path        
        for op, func in zip("DSLR", [D, S, L, R]):
            new_num = func(num)
            if not visited[new_num]:
                visited[new_num] = True
                queue.append((new_num, path + op))
T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(bfs(A, B))


import sys
import heapq
def solution():
    T = int(input())
    for _ in range(T):
        k = int(input())
        max_heap = []
        min_heap = []
        valid = [True] * k        
        for i in range(k):
            operation = input().split()
            cmd = operation[0]
            num = int(operation[1])            
            if cmd == 'I':
                heapq.heappush(min_heap, num)
                heapq.heappush(max_heap, -num)
            elif cmd == 'D':
                if num == 1:
                    while max_heap and not valid[max_heap[0]]:
                        heapq.heappop(max_heap)
                    if max_heap:
                        valid[max_heap[0]] = False
                        heapq.heappop(max_heap)
                elif num == -1:
                    while min_heap and not valid[min_heap[0]]:
                        heapq.heappop(min_heap)
                    if min_heap:
                        valid[min_heap[0]] = False
                        heapq.heappop(min_heap)        
        while min_heap and not valid[min_heap[0]]:
            heapq.heappop(min_heap)
        while max_heap and not valid[max_heap[0]]:
            heapq.heappop(max_heap)        
        if not min_heap or not max_heap:
            print("EMPTY")
        else:
            print(-max_heap[0], min_heap[0])
solution()


from collections import deque
def snakes_and_ladders(snakes, ladders):
    board_size = 100
    board = [i for i in range(board_size + 1)]
    for start, end in ladders:
        board[start] = end
    for start, end in snakes:
        board[start] = end
    visited = [False] * (board_size + 1)
    queue = deque([(1, 0)])
    visited[1] = True
    while queue:
        current, moves = queue.popleft()
        for dice_roll in range(1, 7):
            next_position = current + dice_roll
            if next_position <= board_size:
                next_position = board[next_position]
                if not visited[next_position]:
                    visited[next_position] = True
                    if next_position == board_size:
                        return moves + 1
                    queue.append((next_position, moves + 1))
    return -1
ladder_count, snake_count = map(int, input().split())
ladders = []
snakes = []
for _ in range(ladder_count):
    start, end = map(int, input().split())
    ladders.append((start, end))
for _ in range(snake_count):
    start, end = map(int, input().split())
    snakes.append((start, end))
result = snakes_and_ladders(snakes, ladders)
print(result)


from collections import deque
def bfs(grid, visited, x, y, N, color_map):
    queue = deque([(x, y)])
    visited[x][y] = True
    color = grid[x][y]    
    while queue:
        cx, cy = queue.popleft()        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if color_map[grid[nx][ny]] == color_map[color]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
def count_regions(grid, N, color_map):
    visited = [[False] * N for _ in range(N)]
    region_count = 0        
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(grid, visited, i, j, N, color_map)
                region_count += 1    
    return region_count
N = int(input())
grid = [input().strip() for _ in range(N)]
color_map_normal = {'R': 'R', 'G': 'G', 'B': 'B'}
color_map_colorblind = {'R': 'R', 'G': 'R', 'B': 'B'}
print(count_regions(grid, N, color_map_normal), count_regions(grid, N, color_map_colorblind))


import sys
N = int(sys.stdin.readline().strip())
meetings = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))
count = 0
end_time = 0
for start, end in meetings:
    if start >= end_time:  
        count += 1
        end_time = end
print(count)


import sys
from collections import deque
def process(p, n, arr):
    dq = deque(arr)  
    reverse = False  
    for cmd in p:
        if cmd == 'R':  
            reverse = not reverse  
        elif cmd == 'D':
            if not dq:  
                return "error"
            if reverse:
                dq.pop()  
            else:
                dq.popleft()  
    if reverse:
        dq.reverse() 
    return "[" + ",".join(map(str, dq)) + "]"
T = int(sys.stdin.readline().strip())  
for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())   
    arr_input = sys.stdin.readline().strip()
    if n == 0:
        arr = []
    else:
        arr = list(map(int, arr_input[1:-1].split(",")))  
    print(process(p, n, arr))


import sys
from collections import deque
M, N, H = map(int, sys.stdin.readline().split())
tomatoes = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
queue = deque()
for h in range(H):
    for r in range(N):
        for c in range(M):
            if tomatoes[h][r][c] == 1:
                queue.append((h, r, c, 0))
days = 0
while queue:
    z, x, y, days = queue.popleft()    
    for i in range(6):
        nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
        if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and tomatoes[nz][nx][ny] == 0:
            tomatoes[nz][nx][ny] = 1 
            queue.append((nz, nx, ny, days + 1))
for h in range(H):
    for r in range(N):
        for c in range(M):
            if tomatoes[h][r][c] == 0:
                print(-1)
                sys.exit(0)
print(days)


import sys
from collections import deque
M, N = map(int, sys.stdin.readline().split())
tomatoes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            queue.append((i, j, 0)) 
days = 0
while queue:
    x, y, days = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and tomatoes[nx][ny] == 0:
            tomatoes[nx][ny] = 1  
            queue.append((nx, ny, days + 1))
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 0:
            print(-1)
            sys.exit(0)
print(days)


import sys
from collections import deque
M, N, H = map(int, sys.stdin.readline().split())
tomatoes = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
queue = deque()
for h in range(H):
    for r in range(N):
        for c in range(M):
            if tomatoes[h][r][c] == 1:
                queue.append((h, r, c, 0))
days = 0
while queue:
    z, x, y, days = queue.popleft()    
    for i in range(6):
        nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
        if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and tomatoes[nz][nx][ny] == 0:
            tomatoes[nz][nx][ny] = 1 
            queue.append((nz, nx, ny, days + 1))
for h in range(H):
    for r in range(N):
        for c in range(M):
            if tomatoes[h][r][c] == 0:
                print(-1)
                sys.exit(0)
print(days)


def backtrack(start, path):
    if len(path) == M:
        print(" ".join(map(str, path)))
        return
    for i in range(start, N + 1):
        backtrack(i + 1, path + [i])
N, M = map(int, input().split())
backtrack(1, [])


from itertools import combinations
N, M = map(int, input().split()) 
for seq in combinations(range(1, N + 1), M):  
    print(" ".join(map(str, seq)))


def backtrack(N, M, start, path):
    if len(path) == M:  
        print(" ".join(map(str, path)))
        return
    for i in range(start, N + 1):  
        backtrack(N, M, i, path + [i])  
N, M = map(int, input().split()) 
backtrack(N, M, 1, []) 


from itertools import combinations_with_replacement
N, M = map(int, input().split())  
for seq in combinations_with_replacement(range(1, N + 1), M): 
    print(" ".join(map(str, seq))) 


def backtrack(nums, M, path):
    if len(path) == M:  
        print(" ".join(map(str, path)))
        return
    for i in range(len(nums)):  
        backtrack(nums[:i] + nums[i+1:], M, path + [nums[i]])  
N, M = map(int, input().split())  
nums = sorted(map(int, input().split())) 
backtrack(nums, M, []) 


from itertools import permutations
N, M = map(int, input().split()) 
nums = sorted(map(int, input().split())) 
for seq in permutations(nums, M): 
    print(" ".join(map(str, seq)))  

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix_sum[i][j] = (matrix[i - 1][j - 1] 
                            + prefix_sum[i - 1][j] 
                            + prefix_sum[i][j - 1] 
                            - prefix_sum[i - 1][j - 1])
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = (prefix_sum[x2][y2] 
              - prefix_sum[x1 - 1][y2] 
              - prefix_sum[x2][y1 - 1] 
              + prefix_sum[x1 - 1][y1 - 1])
    print(result)


N = int(input())
A = list(map(int, input().split()))
dp = [1] * N  
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:  
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))  


from collections import deque
N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
parent = [0] * (N+1)
queue = deque([1])
parent[1] = -1
while queue:
    node = queue.popleft()
    for neighbor in tree[node]:
        if parent[neighbor] == 0:
            parent[neighbor] = node
            queue.append(neighbor)
for i in range(2, N+1):
    print(parent[i])


import itertools
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(set(nums))
result = itertools.combinations_with_replacement(nums, M)
for seq in result:
    print(' '.join(map(str, seq)))


def min_operations(A, B):
    operations = 0
    while B >= A:
        if B == A:
            return operations + 1
        if B % 2 == 0:
            B //= 2
        elif B % 10 == 1:
            B //= 10
        else:
            break
        operations += 1
    return -1
A, B = map(int, input().split())
result = min_operations(A, B)
print(result)


N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]
dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0] 
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1] 
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2] 
print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))


A, B, C = map(int, input().split())
result = 1
for _ in range(B):
    result = (result * A) % C  
print(result)


def mod_exp(A, B, C):
    result = 1
    A = A % C 
    while B > 0:
        if B % 2 == 1:
            result = (result * A) % C
        A = (A * A) % C  
        B //= 2  
    return result
A, B, C = map(int, input().split())
print(mod_exp(A, B, C))


n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
dp = [row[:] for row in triangle]
for i in range(n-2, -1, -1):
    for j in range(i+1):
        dp[i][j] += max(dp[i+1][j], dp[i+1][j+1])
print(dp[0][0])


def build_tree(n):
    tree = {}
    for _ in range(n):
        data = input().split()
        parent = data[0]
        left_child = data[1]
        right_child = data[2]
        tree[parent] = (left_child, right_child)
    return tree
def preorder(tree, node):
    if node != '.':
        print(node, end='')
        left, right = tree[node]
        preorder(tree, left)
        preorder(tree, right)
def inorder(tree, node):
    if node != '.':
        left, right = tree[node]
        inorder(tree, left)
        print(node, end='')
        inorder(tree, right)
def postorder(tree, node):
    if node != '.':
        left, right = tree[node]
        postorder(tree, left)
        postorder(tree, right)
        print(node, end='')
n = int(input())
tree = build_tree(n)
preorder(tree, 'A')
print()
inorder(tree, 'A')
print()
postorder(tree, 'A')
print()


def max_sticker_score(T, test_cases):
    results = []
    for t in range(T):
        n = test_cases[t][0]
        stickers = test_cases[t][1:]
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = stickers[0][0]
        dp[1][0] = stickers[1][0]
        for i in range(1, n):
            dp[0][i] = max(dp[1][i-1] + stickers[0][i], dp[0][i-1])
            dp[1][i] = max(dp[0][i-1] + stickers[1][i], dp[1][i-1])
        results.append(max(dp[0][n-1], dp[1][n-1]))
    return results
T = int(input())
test_cases = []
for _ in range(T):
    n = int(input())
    stickers = []
    for i in range(2):
        stickers.append(list(map(int, input().split())))
    test_cases.append([n] + stickers)
results = max_sticker_score(T, test_cases)
for res in results:
    print(res)


import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
start, end = map(int, input().split())
def bfs(start):
    min_cost = 1e7
    q = deque()
    q.append([start, 0])
    while q:
        cur_v, cur_cost = q.popleft()
        if cur_v == end and cur_cost < min_cost:
            min_cost = cur_cost
        for v, c in graph[cur_v]:
            if [v, cur_cost+c] in q:
                continue
            q.append([v, cur_cost+c])          
    return min_cost
print(bfs(start))


import sys
import heapq 
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
start, end = map(int, input().split())
costs = [1e9 for _ in range(n+1)]
heap = []
costs[start] = 0
heapq.heappush(heap, [0, start])   
while heap:
    cur_cost, cur_v = heapq.heappop(heap)
    if costs[cur_v] < cur_cost:
        continue
    for next_v, next_cost in graph[cur_v]:
        sum_cost = cur_cost + next_cost
        if sum_cost >= costs[next_v]:
            continue      
        costs[next_v] = sum_cost
        heapq.heappush(heap, [sum_cost, next_v])  
print(costs[end])


import sys
def game():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]  
    max_dp = [0] * 3
    min_dp = [0] * 3   
    for i in range(3):
        max_dp[i] = board[0][i]
        min_dp[i] = board[0][i]   
    for i in range(1, N):
        new_max = [0] * 3
        new_min = [0] * 3      
        for j in range(3):
            if j == 0:
                new_max[j] = max(max_dp[j], max_dp[j+1]) + board[i][j]
            elif j == 2:
                new_max[j] = max(max_dp[j-1], max_dp[j]) + board[i][j]
            else:
                new_max[j] = max(max_dp[j-1], max_dp[j], max_dp[j+1]) + board[i][j]           
            if j == 0:
                new_min[j] = min(min_dp[j], min_dp[j+1]) + board[i][j]
            elif j == 2:
                new_min[j] = min(min_dp[j-1], min_dp[j]) + board[i][j]
            else:
                new_min[j] = min(min_dp[j-1], min_dp[j], min_dp[j+1]) + board[i][j]        
        max_dp = new_max
        min_dp = new_min    
    print(max(max_dp), min(min_dp))
game()


def game():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]   
    max_dp = board[0]
    min_dp = board[0]   
    for i in range(1, N):
        new_max = [0] * 3
        new_min = [0] * 3       
        for j in range(3):
            if j == 0:
                new_max[j] = max(max_dp[j], max_dp[j+1]) + board[i][j]
                new_min[j] = min(min_dp[j], min_dp[j+1]) + board[i][j]
            elif j == 2:
                new_max[j] = max(max_dp[j-1], max_dp[j]) + board[i][j]
                new_min[j] = min(min_dp[j-1], min_dp[j]) + board[i][j]
            else:
                new_max[j] = max(max_dp[j-1], max_dp[j], max_dp[j+1]) + board[i][j]
                new_min[j] = min(min_dp[j-1], min_dp[j], min_dp[j+1]) + board[i][j]       
        max_dp = new_max
        min_dp = new_min   
    print(max(max_dp), min(min_dp))
game()


def game():
    N = int(input())
    max_dp = list(map(int, input().split()))
    min_dp = max_dp[:]
    for _ in range(1, N):
        board = list(map(int, input().split()))
        new_max = [0] * 3
        new_min = [0] * 3       
        for j in range(3):
            if j == 0:
                new_max[j] = max(max_dp[j], max_dp[j+1]) + board[j]
                new_min[j] = min(min_dp[j], min_dp[j+1]) + board[j]
            elif j == 2:
                new_max[j] = max(max_dp[j-1], max_dp[j]) + board[j]
                new_min[j] = min(min_dp[j-1], min_dp[j]) + board[j]
            else:
                new_max[j] = max(max_dp[j-1], max_dp[j], max_dp[j+1]) + board[j]
                new_min[j] = min(min_dp[j-1], min_dp[j], min_dp[j+1]) + board[j]       
        max_dp = new_max
        min_dp = new_min   
    print(max(max_dp), min(min_dp))
game()


def lcs(str1, str2): 
    len1, len2 = len(str1), len(str2) 
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[len1][len2]
str1 = input().strip() 
str2 = input().strip() 
print(lcs(str1, str2))


n, k = map(int, input().split())
items = [(0, 0)] 
dp = [[0] * (k + 1) for _ in range(n + 1)]
for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))
for i in range(1, n + 1):
    w, v = items[i]
    for j in range(k + 1):
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
print(dp[n][k])


from itertools import combinations
def get_city_chicken_distance(houses, chicken_shops):
    total_distance = 0
    for hx, hy in houses:
        min_distance = float('inf')
        for cx, cy in chicken_shops:
            min_distance = min(min_distance, abs(hx - cx) + abs(hy - cy))
        total_distance += min_distance
    return total_distance
def solve_chicken_distance(N, M, city):
    houses = []
    chicken_shops = []    
    for r in range(N):
        for c in range(N):
            if city[r][c] == 1:
                houses.append((r, c))
            elif city[r][c] == 2:
                chicken_shops.append((r, c))    
    min_city_distance = float('inf')
    for selected_chickens in combinations(chicken_shops, M):
        min_city_distance = min(min_city_distance, get_city_chicken_distance(houses, selected_chickens))
    return min_city_distance
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
print(solve_chicken_distance(N, M, city))


from collections import deque
def solve_easy(N, M, truth_info, parties):
    if truth_info[0] == 0:  
        return M  
    truth_knowers = set(truth_info[1:])
    party_list = [set(party[1:]) for party in parties] 
    queue = deque(truth_knowers) 
    while queue:
        person = queue.popleft()
        for party in party_list:
            if person in party:  
                for p in party:
                    if p not in truth_knowers:
                        truth_knowers.add(p)
                        queue.append(p)  
    count = sum(1 for party in party_list if not (party & truth_knowers))
    return count
N, M = map(int, input().split())
truth_info = list(map(int, input().split()))
parties = [list(map(int, input().split())) for _ in range(M)]
print(solve_easy(N, M, truth_info, parties))


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
def union(parent, rank, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA != rootB:
        if rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
        elif rank[rootA] < rank[rootB]:
            parent[rootA] = rootB
        else:
            parent[rootB] = rootA
            rank[rootA] += 1
def solve(N, M, truth_info, parties):
    parent = [i for i in range(N + 1)]
    rank = [0] * (N + 1)
    if truth_info[0] > 0:
        truth_knowers = set(truth_info[1:])
    else:
        truth_knowers = set()
    party_list = []    
    for party in parties:
        party_size = party[0]
        party_people = party[1:]
        party_list.append(party_people)        
        for i in range(party_size - 1):
            union(parent, rank, party_people[i], party_people[i + 1])    
    real_truth_set = set(find(parent, person) for person in truth_knowers)   
    count = 0
    for party_people in party_list:
        if all(find(parent, person) not in real_truth_set for person in party_people):
            count += 1    
    return count
N, M = map(int, input().split())
truth_info = list(map(int, input().split()))
parties = [list(map(int, input().split())) for _ in range(M)]
print(solve(N, M, truth_info, parties))


N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1
for r in range(N):
    for c in range(1, N):
        if house[r][c] == 1:
            continue
        if c > 0 and dp[r][c - 1][0] > 0:
            dp[r][c][0] += dp[r][c - 1][0]
        if c > 0 and dp[r][c - 1][2] > 0:
            dp[r][c][0] += dp[r][c - 1][2]
        if r > 0 and dp[r - 1][c][1] > 0:
            dp[r][c][1] += dp[r - 1][c][1]
        if r > 0 and dp[r - 1][c][2] > 0:
            dp[r][c][1] += dp[r - 1][c][2]
        if r > 0 and c > 0 and house[r - 1][c] == 0 and house[r][c - 1] == 0:
            if dp[r - 1][c - 1][0] > 0:
                dp[r][c][2] += dp[r - 1][c - 1][0]
            if dp[r - 1][c - 1][1] > 0:
                dp[r][c][2] += dp[r - 1][c - 1][1]
            if dp[r - 1][c - 1][2] > 0:
                dp[r][c][2] += dp[r - 1][c - 1][2]
print(dp[N - 1][N - 1][0] + dp[N - 1][N - 1][1] + dp[N - 1][N - 1][2])


import sys
import heapq
def dijkstra(V, E, K, edges):
    INF = float('inf')
    graph = [[] for _ in range(V + 1)]
    distance = [INF] * (V + 1)    
    for u, v, w in edges:
        graph[u].append((w, v))    
    pq = []
    heapq.heappush(pq, (0, K))
    distance[K] = 0    
    while pq:
        dist, now = heapq.heappop(pq)        
        if distance[now] < dist:
            continue        
        for weight, next_node in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(pq, (cost, next_node))    
    return distance
input = sys.stdin.read
data = input().split('\n')
V, E = map(int, data[0].split())
K = int(data[1])
edges = [tuple(map(int, line.split())) for line in data[2:E+2]]
result = dijkstra(V, E, K, edges)
for i in range(1, V + 1):
    print(result[i] if result[i] != float('inf') else 'INF')


import sys
from collections import deque
def bfs(start, graph, n):
    visited = [-1] * (n + 1)
    queue = deque([(start, 0)]) 
    visited[start] = 0
    farthest_node = start
    max_distance = 0
    while queue:
        node, dist = queue.popleft()
        for next_node, weight in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = dist + weight
                queue.append((next_node, dist + weight))
                if visited[next_node] > max_distance:
                    max_distance = visited[next_node]
                    farthest_node = next_node
    return farthest_node, max_distance
input = sys.stdin.read
data = input().split('\n')
n = int(data[0])
graph = [[] for _ in range(n + 1)]
for i in range(1, n):
    u, v, w = map(int, data[i].split())
    graph[u].append((v, w))
    graph[v].append((u, w))
farthest_node, _ = bfs(1, graph, n)
_, tree_diameter = bfs(farthest_node, graph, n)
print(tree_diameter)


import sys
sys.setrecursionlimit(100000)
def dfs(node, dist, graph, visited):
    visited[node] = dist
    farthest_node = node
    max_distance = dist
    for next_node, weight in graph[node]:
        if visited[next_node] == -1:
            new_node, new_dist = dfs(next_node, dist + weight, graph, visited)
            if new_dist > max_distance:
                farthest_node, max_distance = new_node, new_dist
    return farthest_node, max_distance
input = sys.stdin.read
data = input().split('\n')
n = int(data[0])
graph = [[] for _ in range(n + 1)]
for i in range(1, n):
    u, v, w = map(int, data[i].split())
    graph[u].append((v, w))
    graph[v].append((u, w))
visited = [-1] * (n + 1)
farthest_node, _ = dfs(1, 0, graph, visited)
visited = [-1] * (n + 1)
_, tree_diameter = dfs(farthest_node, 0, graph, visited)
print(tree_diameter)


import sys
input = sys.stdin.read
data = input().split()
R, C = map(int, data[:2])
board = data[2:]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, visited):
    global max_count
    max_count = max(max_count, len(visited))
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in visited:
            dfs(nx, ny, visited | {board[nx][ny]})
max_count = 1
dfs(0, 0, {board[0][0]})
print(max_count)


import sys
sys.setrecursionlimit(10000)
input = sys.stdin.read
data = input().split()
R, C = map(int, data[:2])
board = data[2:]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, visited, count):
    global max_count
    max_count = max(max_count, count)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            char_bit = 1 << (ord(board[nx][ny]) - ord('A'))
            if not (visited & char_bit):
                dfs(nx, ny, visited | char_bit, count + 1)
max_count = 1
start_char_bit = 1 << (ord(board[0][0]) - ord('A'))
dfs(0, 0, start_char_bit, 1)
print(max_count)


import sys
sys.setrecursionlimit(10000)
input = sys.stdin.read
data = input().split()
R, C = map(int, data[:2])
board = data[2:]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [0] * 26
max_count = 0
def dfs(x, y, count):
    global max_count
    max_count = max(max_count, count)
    if max_count == R * C:
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            idx = ord(board[nx][ny]) - ord('A')
            if not visited[idx]:
                visited[idx] = 1
                dfs(nx, ny, count + 1)
                visited[idx] = 0 
visited[ord(board[0][0]) - ord('A')] = 1
dfs(0, 0, 1)
print(max_count)


import sys
sys.setrecursionlimit(10**6)
preorder = list(map(int, sys.stdin.read().split()))
def postorder(start, end):
    if start > end:
        return  
    split_idx = start + 1
    while split_idx <= end and preorder[split_idx] < preorder[start]:
        split_idx += 1
    postorder(start + 1, split_idx - 1)
    postorder(split_idx, end)
    print(preorder[start])
postorder(0, len(preorder) - 1)


def draw_triangle(n):
    if n == 3:
        return ["  *  ", " * * ", "*****"]
    small_triangle = draw_triangle(n // 2)
    top = [" " * (n // 2) + line + " " * (n // 2) for line in small_triangle]
    bottom = [line + " " + line for line in small_triangle]
    return top + bottom
N = int(input().strip())
print("\n".join(draw_triangle(N)))


from itertools import permutations
def is_valid(queen_pos):
    N = len(queen_pos)
    for i in range(N):
        for j in range(i+1, N):
            if abs(i - j) == abs(queen_pos[i] - queen_pos[j]):
                return False
    return True
def n_queen(N):
    count = 0
    for perm in permutations(range(N)):
        if is_valid(perm):
            count += 1
    return count
N = int(input())
print(n_queen(N))


ori = input()
bomb = input()
while bomb in ori:
    ori = ori.replace(bomb, "")
print(ori if ori else "FRULA")


ori = input()
bomb = input()
stack = []
bomb_len = len(bomb)
for char in ori:
    stack.append(char)
    if ''.join(stack[-bomb_len:]) == bomb:
        del stack[-bomb_len:]
result = ''.join(stack)
print(result if result else "FRULA")


import numpy as np
N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
np_A = np.array(A, dtype=np.int64)
result = np.linalg.matrix_power(np_A, B) % 1000
for row in result:
    print(' '.join(map(str, row)))


def multiply(A, B):
    N = len(A)
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(N)) % 1000
    return result
def power(matrix, b):
    if b == 1:
        return [[x % 1000 for x in row] for row in matrix]
    half = power(matrix, b // 2)
    result = multiply(half, half)
    if b % 2 == 1:
        result = multiply(result, matrix)
    return result
N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
for row in power(A, B):
    print(*row)


N = int(input())
A = list(map(int, input().split()))
inc = [1] * N
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            inc[i] = max(inc[i], inc[j] + 1)
dec = [1] * N
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if A[j] < A[i]:
            dec[i] = max(dec[i], dec[j] + 1)
max_len = 0
for i in range(N):
    max_len = max(max_len, inc[i] + dec[i] - 1)
print(max_len)


n = int(input())
m = int(input())
INF = int(1e9)
dist = [[INF] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = min(dist[a-1][b-1], c)
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()


from collections import deque
def bfs(n, k):
    MAX = 100001
    visited = [0] * MAX 
    count = [0] * MAX    
    queue = deque()
    queue.append(n)
    visited[n] = 1      
    count[n] = 1
    while queue:
        now = queue.popleft()
        for next_pos in [now - 1, now + 1, now * 2]:
            if 0 <= next_pos < MAX:
                if visited[next_pos] == 0:
                    visited[next_pos] = visited[now] + 1
                    count[next_pos] = count[now]
                    queue.append(next_pos)
                elif visited[next_pos] == visited[now] + 1:
                    count[next_pos] += count[now]
    return visited[k] - 1, count[k]
N, K = map(int, input().split())
time, ways = bfs(N, K)
print(time)
print(ways)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
n = int(input())
print(fib(n))


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
n = int(input())
print(fib(n)) 


def fib_list(n):
    fibs = [0, 1]
    for i in range(2, n):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs
n = int(input())
print(fib_list(n))


expr = input()
stack = []
result = ''
for token in expr:
    if token.isalpha():
        result += token
    elif token == '(':
        stack.append(token)
    elif token == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()
    elif token in '+-':
        while stack and stack[-1] not in '([':
            result += stack.pop()
        stack.append(token)
    elif token in '*/':
        while stack and stack[-1] in '*/':
            result += stack.pop()
        stack.append(token)
while stack:
    result += stack.pop()
print(result)


import sys
from collections import deque
input = sys.stdin.readline
V = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(V):
    data = list(map(int, input().split()))
    node = data[0]
    i = 1
    while data[i] != -1:
        graph[node].append((data[i], data[i + 1]))
        i += 2
def bfs(start):
    visited = [-1] * (V + 1)
    queue = deque()
    queue.append(start)
    visited[start] = 0
    while queue:
        current = queue.popleft()
        for neighbor, dist in graph[current]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[current] + dist
                queue.append(neighbor)
    max_dist = max(visited)
    farthest_node = visited.index(max_dist)
    return farthest_node, max_dist
node, _ = bfs(1)
_, diameter = bfs(node)
print(diameter)


from collections import deque
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_x, shark_y = i, j
            graph[i][j] = 0 
shark_size = 2
eat_count = 0
time = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y, size):
    visited = [[-1]*n for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    fishes = []
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if graph[nx][ny] <= size:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    if 0 < graph[nx][ny] < size:
                        fishes.append((visited[nx][ny], nx, ny))
    if not fishes:
        return None
    fishes.sort()
    return fishes[0]
while True:
    result = bfs(shark_x, shark_y, shark_size)
    if result is None:
        break
    dist, nx, ny = result
    time += dist
    shark_x, shark_y = nx, ny
    graph[nx][ny] = 0
    eat_count += 1
    if eat_count == shark_size:
        shark_size += 1
        eat_count = 0
print(time)


import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
start, end = map(int, input().split())
distance = [INF] * (n + 1)
prev = [0] * (n + 1)
heap = []
distance[start] = 0
heapq.heappush(heap, (0, start))
while heap:
    dist, now = heapq.heappop(heap)
    if distance[now] < dist:
        continue
    for next_node, cost in graph[now]:
        if distance[next_node] > dist + cost:
            distance[next_node] = dist + cost
            prev[next_node] = now
            heapq.heappush(heap, (distance[next_node], next_node))
path = []
temp = end
while temp:
    path.append(temp)
    temp = prev[temp]
path.reverse()
print(distance[end])
print(len(path))
print(' '.join(map(str, path)))


import heapq
import sys
input = sys.stdin.readline
def dijkstra(start, graph, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cost, now = heapq.heappop(heap)
        if cost > dist[now]:
            continue
        for to, time in graph[now]:
            if dist[to] > cost + time:
                dist[to] = cost + time
                heapq.heappush(heap, (dist[to], to))
    return dist
n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))        
    reverse_graph[b].append((a, t))  
to_party = dijkstra(x, reverse_graph, n)
from_party = dijkstra(x, graph, n)      
max_time = 0
for i in range(1, n + 1):
    total_time = to_party[i] + from_party[i]
    max_time = max(max_time, total_time)
print(max_time)


from itertools import combinations
def is_subsequence(sub, seq):
    i = 0
    for num in seq:
        if i < len(sub) and sub[i] == num:
            i += 1
    return i == len(sub)
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
common = [a for a in A if a in B]
candidates = []
for l in range(1, len(common) + 1):
    for comb in combinations(common, l):
        if is_subsequence(comb, B):
            candidates.append(comb)
if candidates:
    answer = max(candidates)
    print(len(answer))
    print(*answer)
else:
    print(0)


from itertools import combinations
from collections import deque
import copy
n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
empty = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 0]
virus = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 2]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(temp):
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    q.append((nx, ny))
max_safe = 0
for walls in combinations(empty, 3):
    temp_lab = copy.deepcopy(lab)
    for x, y in walls:
        temp_lab[x][y] = 1
    bfs(temp_lab)
    safe = sum(row.count(0) for row in temp_lab)
    max_safe = max(max_safe, safe)
print(max_safe)


n = int(input())
lis = []
for _ in range(n):
    i = int(input())
    lis.append(i)
lis.sort() 
for li in lis:
    print(li)


import sys
n = int(sys.stdin.readline())
lis = [int(sys.stdin.readline()) for _ in range(n)]
for num in sorted(lis):
    print(num)


import sys
input = sys.stdin.readline
count = [0] * 10001
n = int(input())
for _ in range(n):
    num = int(input())
    count[num] += 1
for i in range(10001):
    if count[i]:
        for _ in range(count[i]):
            print(i)


import sys
import math
input = sys.stdin.readline
n = int(input())
positions = [int(input()) for _ in range(n)]
distances = [positions[i+1] - positions[i] for i in range(n-1)]
gcd = distances[0]
for d in distances[1:]:
    gcd = math.gcd(gcd, d)
trees_to_plant = 0
for d in distances:
    trees_to_plant += (d // gcd) - 1
print(trees_to_plant)


def check_brackets(sen):
    stack = []
    for ch in sen:
        if ch in '([':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack[-1] != '(':
                return "no"
            stack.pop()
        elif ch == ']':
            if not stack or stack[-1] != '[':
                return "no"
            stack.pop()
    return "yes" if not stack else "no"
while True:
    line = input()
    if line == '.':
        break
    print(check_brackets(line))


from collections import deque
n = int(input())
nums = list(map(int, input().split()))
balloons = deque((i + 1, num) for i, num in enumerate(nums))
result = []
while balloons:
    idx, move = balloons.popleft()
    result.append(idx)
    if not balloons:
        break
    if move > 0:
        balloons.rotate(-(move - 1))
    else:
        balloons.rotate(-move)
print(*result)


from collections import deque
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
structures = []
for i in range(N):
    if A[i] == 0:
        structures.append(deque([B[i]]))
    else:
        structures.append([B[i]])
result = []
for c in C:
    for i in range(N):
        if A[i] == 0:
            structures[i].append(c)
            popped_value = structures[i].popleft()
        else:
            structures[i].append(c)
            popped_value = structures[i].pop()
        
        result.append(popped_value)
print(*result)


from collections import deque
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
structures = []
for i in range(N):
    if A[i] == 0:
        structures.append(deque([B[i]]))
    else:
        structures.append([B[i]])
result = []
for c in C:
    for i in range(N):
        if A[i] == 0:
            structures[i].append(c)
            popped_value = structures[i].popleft()
        else:
            structures[i].append(c)
            popped_value = structures[i].pop()
        
        result.append(popped_value)
print(*result)


import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
sequence_A = list(map(int, input().split()))
sequence_B = list(map(int, input().split()))
M = int(input())
sequence_C = list(map(int, input().split()))
queue = deque([])
for i in range(N):
    if sequence_A[i] == 0:
        queue.appendleft(sequence_B[i])
for i in range(M):
    queue.append(sequence_C[i])
    print(queue.popleft(), end=" ")


n= int(input())
print(n*(n-1))


n= int(input())
print(2**n)


n = int(input())
a = 1
for i in range(1, n+1):
    a *= i
print(a)


import math
print(math.factorial(int(input())))


import math
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(math.comb(M, N))


a = [input() for _ in range(3)]
def fb(x):
    if x % 15 == 0:
        return 'FizzBuzz'
    if x % 3 == 0:
        return 'Fizz'
    if x % 5 == 0:
        return 'Buzz'
    return str(x)
i = 1
while True:
    if [fb(i), fb(i+1), fb(i+2)] == a:
        print(fb(i+3))
        break
    i += 1


for i in range(3, 0, -1):
    x = input()
    if x not in ['Fizz', 'Buzz', 'FizzBuzz']:
        n = int(x) + i
print('Fizz'*(n % 3 == 0) + 'Buzz'*(n % 5 == 0) or n)


import sys
def roundUp(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
n = int(sys.stdin.readline().rstrip())
if n == 0:
    print(0)
else:
    arr = []
    for i in range(n):
        arr.append(int(sys.stdin.readline().rstrip()))
    arr.sort()
    border = roundUp(n * 0.15)
    if len(arr) <= 2 * border:
        print(0)
    else:
        print(roundUp(sum(arr[border:n-border]) / len(arr[border:n-border])))


L = int(input())
string = input()
r = 31
M = 1234567891
hash_value = 0
for i in range(L):
    char_value = ord(string[i]) - ord('a') + 1
    hash_value = (hash_value + char_value * pow(r, i, M)) % M
print(hash_value)


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
count = 0 
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1
print(count)


from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
n, m = map(int, input().split()) 
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
count = 0 
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        bfs(graph, i, visited) 
        count += 1
print(count)


n, r, c = map(int, input().split())
def z(n, r, c):
    if n == 0:
        return 0
    half = 2 ** (n - 1)
    if r < half and c < half:
        return z(n - 1, r, c)
    elif r < half and c >= half:
        return half * half + z(n - 1, r, c - half)
    elif r >= half and c < half:
        return 2 * half * half + z(n - 1, r - half, c)
    else:
        return 3 * half * half + z(n - 1, r - half, c - half)
print(z(n, r, c))


n, m = map(int, input().split())
nums = sorted(map(int, input().split()))
visited = [False] * n
result = []
def backtrack(path):
    if len(path) == m:
        print(*path)
        return
    prev = 0
    for i in range(n):
        if not visited[i] and nums[i] != prev:
            visited[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            visited[i] = False
            prev = nums[i]
backtrack([])


from collections import deque
n, k = map(int, input().split())
MAX = 100001
dist = [-1] * MAX
dq = deque()
dq.append(n)
dist[n] = 0
while dq:
    current = dq.popleft()
    if current == k:
        print(dist[current])
        break
    for next_pos in (current * 2, current - 1, current + 1):
        if 0 <= next_pos < MAX and dist[next_pos] == -1:
            if next_pos == current * 2:
                dist[next_pos] = dist[current]
                dq.appendleft(next_pos) 
            else:
                dist[next_pos] = dist[current] + 1
                dq.append(next_pos)


n = int(input())
count = 0
cols = [0] * n
def is_safe(row):
    for i in range(row):
        if cols[i] == cols[row] or abs(cols[i] - cols[row]) == row - i:
            return False
    return True
def solve(row):
    global count
    if row == n:
        count += 1
        return
    for i in range(n):
        cols[row] = i
        if is_safe(row):
            solve(row + 1)
solve(0)
print(count)


import sys
input = sys.stdin.readline
def has_negative_cycle(n, edges):
    INF = 1e9
    dist = [INF] * (n + 1)
    dist[1] = 0

    for i in range(n):
        for u, v, w in edges:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                if i == n - 1:
                    return True
    return False
tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))
    if has_negative_cycle(n, edges):
        print("YES")
    else:
        print("NO")


def multiply(a, b):
    return [
        [(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % MOD, (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % MOD],
        [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % MOD, (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % MOD]]
def matrix_power(matrix, n):
    result = [[1, 0], [0, 1]] 
    while n > 0:
        if n % 2 == 1:
            result = multiply(result, matrix)
        matrix = multiply(matrix, matrix)
        n //= 2
    return result
def fibonacci(n):
    if n == 0:
        return 0
    base = [[1, 1], [1, 0]]
    result = matrix_power(base, n-1)
    return result[0][0]  # F(n)
MOD = 1000000007
n = int(input())
print(fibonacci(n))


import sys
input = sys.stdin.readline
n = int(input())
p = 1000000007
def mul(A, B):
    n = len(A)
    Z = [[0]*n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += A[row][i] * B[i][col]
            Z[row][col] = e % p            
    return Z
def square(A, k):
    if k == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= p
        return A    
    tmp = square(A, k//2)
    if k % 2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)    
fib_matrix = [[1, 1], [1, 0]]
print(square(fib_matrix, n)[0][1])


N = int(input())
count = 0
row = [0] * N
def is_safe(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True
def solve(x):
    global count
    if x == N:
        count += 1
        return
    for i in range(N):
        row[x] = i
        if is_safe(x):
            solve(x + 1)
solve(0)
print(count)


N = int(input())
count = 0
col = [False] * N
diag1 = [False] * (2 * N - 1)
diag2 = [False] * (2 * N - 1)
def solve(row):
    global count
    if row == N:
        count += 1
        return
    for i in range(N):
        if not col[i] and not diag1[row + i] and not diag2[row - i + N - 1]:
            col[i] = diag1[row + i] = diag2[row - i + N - 1] = True
            solve(row + 1)
            col[i] = diag1[row + i] = diag2[row - i + N - 1] = False
solve(0)
print(count)


from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
queue = deque()
queue.append((0, 0, 0))
visited[0][0][0] = 1
while queue:
    x, y, broken = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                visited[nx][ny][broken] = visited[x][y][broken] + 1
                queue.append((nx, ny, broken))
            if graph[nx][ny] == 1 and broken == 0 and visited[nx][ny][1] == 0:
                visited[nx][ny][1] = visited[x][y][broken] + 1
                queue.append((nx, ny, 1))
res1 = visited[n - 1][m - 1][0]
res2 = visited[n - 1][m - 1][1]
if res1 and res2:
    print(min(res1, res2))
elif res1:
    print(res1)
elif res2:
    print(res2)
else:
    print(-1)


import sys
input = sys.stdin.read
def solve():
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        M = int(data[idx])
        N = int(data[idx+1])
        x = int(data[idx+2])
        y = int(data[idx+3])
        idx += 4
        found = False
        k = x
        while k <= M * N:
            if (k - y) % N == 0:
                results.append(k)
                found = True
                break
            k += M
        if not found:
            results.append(-1)
    for r in results:
        print(r)
solve()


t = int(input())
ns = [int(input()) for _ in range(t)]
max_n = max(ns)
p = [0] * (max_n + 1)
p[1] = p[2] = p[3] = 1
for i in range(4, max_n + 1):
    p[i] = p[i - 2] + p[i - 3]
for n in ns:
    print(p[n])


import sys
n = int(sys.stdin.readline())
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = i
    j = 1
    while j * j <= i:
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1
print(dp[n])


n = int(input())
dp = [0] * (n + 1)
for i in range(1, n + 1):
    min_val = i
    j = 1
    while j * j <= i:
        min_val = min(min_val, dp[i - j * j] + 1)
        j += 1
    dp[i] = min_val
print(dp[n])


import sys
N, M, B = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]
min_time = sys.maxsize
best_height = -1
for target_height in range(257):
    inventory = B
    time = 0
    for i in range(N):
        for j in range(M):
            diff = land[i][j] - target_height
            if diff > 0:
                inventory += diff
                time += 2 * diff
            elif diff < 0:
                inventory -= (-diff)
                time += (-diff)
    if inventory < 0:
        continue
    if time < min_time:
        min_time = time
        best_height = target_height
    elif time == min_time and target_height > best_height:
        best_height = target_height
print(min_time, best_height)


N = int(input())
M = int(input())
S = input()
i = 0
count = 0
result = 0
while i < M - 1:
    if S[i] == 'I':
        cnt = 0
        while i + 2 < M and S[i+1] == 'O' and S[i+2] == 'I':
            cnt += 1
            i += 2
            if cnt == N:
                result += 1
                cnt -= 1
        i += 1
    else:
        i += 1
print(result)


import sys
input = sys.stdin.readline
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N, M = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
maxValue = 0
def dfs(i, j, dsum, cnt):
    global maxValue
    if cnt == 4:
        maxValue = max(maxValue, dsum)
        return
    for n in range(4):
        ni = i+move[n][0]
        nj = j+move[n][1]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            visited[ni][nj] = True
            dfs(ni, nj, dsum + board[ni][nj], cnt+1)
            visited[ni][nj] = False
def exce(i, j):
    global maxValue
    for n in range(4):
        tmp = board[i][j]
        for k in range(3):
            t = (n+k)%4
            ni = i+move[t][0]
            nj = j+move[t][1]
            if not (0 <= ni < N and 0 <= nj < M):
                tmp = 0
                break
            tmp += board[ni][nj]
        maxValue = max(maxValue, tmp)
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False
        exce(i, j)
print(maxValue)


import sys
import heapq

def isEmpty(nums):
    for item in nums:
        if item[1] > 0:
            return False
    return True

t = int(sys.stdin.readline())
for i in range(t):
    min_heap = []
    max_heap = []
    nums = dict()
    k = int(sys.stdin.readline())
    for j in range(k):
        oprt, oprd = sys.stdin.readline().split()
        num = int(oprd)
        if oprt == 'I':
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1
                heapq.heappush(min_heap, num)
                heapq.heappush(max_heap, -num)
        elif oprt == 'D':
            if not isEmpty(nums.items()):
                if num == 1:
                    while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
                        temp = -heapq.heappop(max_heap)
                        if temp in nums:
                            del(nums[temp])
                    nums[-max_heap[0]] -= 1
                else:
                    while min_heap[0] not in nums or nums[min_heap[0]] < 1:
                        temp = heapq.heappop(min_heap)
                        if temp in nums:
                            del(nums[temp])
                    nums[min_heap[0]] -= 1
    if isEmpty(nums.items()):
        print('EMPTY')
    else:
        while min_heap[0] not in nums or nums[min_heap[0]] < 1:
            heapq.heappop(min_heap)
        while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
            heapq.heappop(max_heap)
        print(-max_heap[0], min_heap[0])


import heapq
INF = int(1e9)
def dijkstra(start, graph, N):
    distance = [INF] * (N + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next_node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))
    return distance
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())
d1 = dijkstra(1, graph, N)
dv1 = dijkstra(v1, graph, N)
dv2 = dijkstra(v2, graph, N)
route1 = d1[v1] + dv1[v2] + dv2[N]
route2 = d1[v2] + dv2[v1] + dv1[N]
result = min(route1, route2)
print(result if result < INF else -1)


r, c = map(int, input().split())
maps = []
for _ in range(r):
    maps.append(list(input()))
ans = 0
alphas = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not maps[nx][ny] in alphas:
            alphas.add(maps[nx][ny])
            dfs(nx, ny, count+1)
            alphas.remove(maps[nx][ny])
alphas.add(maps[0][0])
dfs(0, 0, 1)
print(ans)


# 모듈러
MOD = 1000000007
def mod_inverse(x, mod):
    return pow(x, mod - 2, mod)
M = int(input())
total = 0
for _ in range(M):
    N, S = map(int, input().split())
    inv_N = mod_inverse(N, MOD)
    total = (total + S * inv_N) % MOD
print(total)


INF = float('inf')
def floyd_warshall(n, dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
n, m, r = map(int, input().split())
items = list(map(int, input().split()))
dist = [[INF] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0
for _ in range(r):
    a, b, l = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = min(dist[a][b], l)
    dist[b][a] = min(dist[b][a], l)
floyd_warshall(n, dist)
max_items = 0
for i in range(n):
    total_items = items[i]
    for j in range(n):
        if i != j and dist[i][j] <= m:
            total_items += items[j]
    max_items = max(max_items, total_items)
print(max_items)


import sys
input = sys.stdin.readline
def diffuse():
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    amount = [[board[i][j] // 5 for j in range(C)] for i in range(R)]
    updated = [[0] * C for _ in range(R)]
    filter = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == -1:
                filter.append(i)
                updated[i][j] = -1
                continue
            count = 4
            added = 0
            for d in directions:
                x, y = i + d[0], j + d[1]
                if x < 0 or x >= R or y < 0 or y >= C or board[x][y] == -1:
                    count -= 1
                else:
                    added += amount[x][y]
            updated[i][j] = board[i][j] - (amount[i][j] * count) + added
    return filter[0], filter[1], updated
def activate(filter_x, filter_y):
    for r in range(filter_x - 1, 0, -1):
        board[r][0] = board[r - 1][0]
    for c in range(C - 1):
        board[0][c] = board[0][c + 1]
    for r in range(filter_x):
        board[r][-1] = board[r + 1][-1]
    for c in range(C - 1, 0, -1):
        board[filter_x][c] = board[filter_x][c - 1]
    board[filter_x][1] = 0
    for r in range(filter_y + 1, R - 1):
        board[r][0] = board[r + 1][0]
    for c in range(C - 1):
        board[-1][c] = board[-1][c + 1]
    for r in range(R - 1, filter_y, - 1):
        board[r][-1] = board[r - 1][-1]
    for c in range(C - 1, 0, -1):
        board[filter_y][c] = board[filter_y][c - 1]
    board[filter_y][1] = 0
def sum_dust():
    result = 0
    for row in board:
        result += sum(row)
    return result + 2
R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
for _ in range(T):
    x, y, board = diffuse()
    activate(x, y)
print(sum_dust())


def sol(arr1, arr2, res = []):
    if (not arr1) or (not arr2):
        return res
    tmp1, tmp2 = max(arr1), max(arr2)
    idx1, idx2 = arr1.index(tmp1), arr2.index(tmp2)
    if tmp1 == tmp2:
        res.append(tmp1)
        return sol(arr1[idx1 + 1:], arr2[idx2 + 1:], res)
    elif tmp1 > tmp2:
        arr1.pop(idx1)
        return sol(arr1, arr2, res)
    else:
        arr2.pop(idx2)
        return sol(arr1, arr2, res)
n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
ans = sol(arr1, arr2)
print(len(ans))
if ans:
    print(*ans)


from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs():
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if cheeze[nx][ny] >= 1: 
                    cheeze[nx][ny] += 1
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = True
def melt_cheeze():
    melted = 0
    for i in range(n):
        for j in range(m):
            if cheeze[i][j] >= 3:
                cheeze[i][j] = 0
                melted += 1
            elif cheeze[i][j] >= 2:
                cheeze[i][j] = 1
    return melted
time = 0
while True:
    bfs()
    melted = melt_cheeze()
    if melted:
        time += 1
    else:
        print(time)
        break


n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
total_cost = 0
min_price = prices[0]
for i in range(n - 1):
    if prices[i] < min_price:
        min_price = prices[i]
    total_cost += min_price * distances[i]
print(total_cost)


n, m = map(int, input().split())
print(abs(n - m))


st = input()
answer = ''
for s in st:
    if s.islower():
        answer += s.upper()
    else:
        answer += s.lower()
print(answer)


grade = input()
grade_to_score = {
    'A+': 4.3, 'A0': 4.0, 'A-': 3.7, 'B+': 3.3, 'B0': 3.0, 'B-': 2.7, 'C+': 2.3, 'C0': 2.0, 'C-': 1.7, 'D+': 1.3, 'D0': 1.0, 'D-': 0.7, 'F': 0.0
print(grade_to_score[grade])


n, m = map(int, input().split())
print((n+m)*(n-m))


n, m = map(int, input().split())
print(n**2 - m**2)


n = int(input())
divisors = list(map(int, input().split()))
print(min(divisors) * max(divisors))



n = int(input())
cnt = 0
users = set()
for _ in range(n):
    line = input()
    if line == "ENTER":
        users.clear()
    elif line not in users:
        users.add(line)
        cnt += 1
print(cnt)


import sys
from collections import defaultdict
n, m = map(int, sys.stdin.readline().split())
words = defaultdict(int)
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if len(word) >= m:
        words[word] += 1
sorted_words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for word, _ in sorted_words:
    print(word)


import sys
n = int(sys.stdin.readline())
dance = set(['ChongChong'])
for _ in range(n):
    a, b = sys.stdin.readline().split()
    if a in dance or b in dance:
        dance.add(a)
        dance.add(b)
print(len(dance))


isbn = input().strip()
m = int(isbn[-1])
weights = [1 if i % 2 == 0 else 3 for i in range(12)]
missing_index = -1
total = 0
for i in range(12):
    if isbn[i] == '*':
        missing_index = i
    else:
        total += int(isbn[i]) * weights[i]
for digit in range(10):
    if (total + digit * weights[missing_index] + m) % 10 == 0:
        print(digit)
        break


print("강한친구 대한육군")
print("강한친구 대한육군")


N = int(input())
for i in range(N, 0, -1):
    print(i)


N = int(input())
num = N
count = 0
while True:
    a = num // 10
    b = num % 10
    new_num = (b * 10) + ((a + b) % 10)
    count += 1
    num = new_num
    if num == N:
        break
print(count)


N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()
def can_place(distance):
    count = 1
    last = houses[0]
    for i in range(1, N):
        if houses[i] - last >= distance:
            count += 1
            last = houses[i]
    return count >= C
left, right = 1, houses[-1] - houses[0]
result = 0
while left <= right:
    mid = (left + right) // 2
    if can_place(mid):
        result = mid
        left = mid + 1
    else:
        right = mid - 1
print(result)


N = int(input())
K = int(input())
left, right = 1, N * N
answer = 0
while left <= right:
    mid = (left + right) // 2
    count = 0
    for i in range(1, N+1):
        count += min(N, mid // i)
    if count >= K:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
print(answer)


import sys
import bisect
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
sub = []
for x in A:
    pos = bisect.bisect_left(sub, x)
    if pos == len(sub):
        sub.append(x)
    else:
        sub[pos] = x
print(len(sub))


import sys
import heapq
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    M = int(input())
    nums = []
    while len(nums) < M:
        nums += list(map(int, input().split()))
    left_heap = []   
    right_heap = []
    result = []
    for i, num in enumerate(nums):
        if not left_heap or num <= -left_heap[0]:
            heapq.heappush(left_heap, -num)
        else:
            heapq.heappush(right_heap, num)
        if len(left_heap) > len(right_heap) + 1:
            heapq.heappush(right_heap, -heapq.heappop(left_heap))
        elif len(right_heap) > len(left_heap):
            heapq.heappush(left_heap, -heapq.heappop(right_heap))
        if (i + 1) % 2 == 1:
            result.append(-left_heap[0])
    print(len(result))
    for i in range(0, len(result), 10):
        print(*result[i:i+10])


import sys
import heapq
input = sys.stdin.readline
N, K = map(int, input().split())
jewels = []
bags = []
for _ in range(N):
    m, v = map(int, input().split())
    jewels.append((m, v)) 
for _ in range(K):
    c = int(input())
    bags.append(c)
jewels.sort()    
bags.sort()     
result = 0
heap = []
idx = 0
for c in bags:
    while idx < N and jewels[idx][0] <= c:
        heapq.heappush(heap, -jewels[idx][1])
        idx += 1
    if heap:
        result += -heapq.heappop(heap) 
print(result)


import sys
input=sys.stdin.readline
v,e=map(int,input().split())
p=list(range(v+1))
def f(x):
    while p[x]!=x:
        p[x]=p[p[x]]
        x=p[x]
    return x
r=0
for a,b,c in sorted([tuple(map(int,input().split())) for _ in range(e)],key=lambda x:x[2]):
    a,b=f(a),f(b)
    if a!=b:
        p[b]=a
        r+=c
print(r)


n = int(input())
arr = list(map(int, input().split()))
l, r = 0, n - 1
ans = (arr[l], arr[r])
min_val = abs(arr[l] + arr[r])
while l < r:
    s = arr[l] + arr[r
    if abs(s) < min_val:
        min_val = abs(s)
        ans = (arr[l], arr[r])
    if s > 0:
        r -= 1
    else:
        l += 1
print(*ans)


import sys
input = sys.stdin.readline
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
area = 0
for i in range(n):
    x1, y1 = points[i]
    x2, y2 = points[(i + 1) % n]
    area += x1 * y2 - x2 * y1
area = abs(area) / 2
print(f"{area:.1f}")


import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1
queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
result = []
while queue:
    cur = queue.popleft()
    result.append(cur)
    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)
print(*result)


import sys
input = sys.stdin.readline
C, N = map(int, input().split())
cities = [tuple(map(int, input().split())) for _ in range(N)]
INF = 1e9
dp = [INF] * (C + 101)
dp[0] = 0
for cost, customer in cities:
    for i in range(customer, C + 101):
        dp[i] = min(dp[i], dp[i - customer] + cost)
print(min(dp[C:]))


import sys
input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
total = 0
answer = N + 1
for right in range(N):
    total += arr[right]
    while total >= S:
        answer = min(answer, right - left + 1)
        total -= arr[left]
        left += 1
print(0 if answer == N + 1 else answer)


import sys
input = sys.stdin.readline

board = [list(map(int, input().strip())) for _ in range(9)]

row = [0]*9
col = [0]*9
box = [0]*9
empty = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            empty.append((i, j))
        else:
            num = board[i][j]
            bit = 1 << num
            row[i] |= bit
            col[j] |= bit
            box[(i//3)*3 + j//3] |= bit

def dfs(idx):
    if idx == len(empty):
        for r in board:
            print("".join(map(str, r)))
        sys.exit()
    x, y = empty[idx]
    b = (x//3)*3 + y//3
    for num in range(1, 10):
        bit = 1 << num
        if row[x] & bit or col[y] & bit or box[b] & bit:
            continue
        board[x][y] = num
        row[x] |= bit
        col[y] |= bit
        box[b] |= bit
        dfs(idx+1)
        board[x][y] = 0
        row[x] ^= bit
        col[y] ^= bit
        box[b] ^= bit
dfs(0)


import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [[0]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1
for length in range(3, n+1):
    for i in range(n - length + 1):
        j = i + length - 1
        if arr[i] == arr[j] and dp[i+1][j-1]:
            dp[i][j] = 1
m = int(input())
out = []
for _ in range(m):
    s, e = map(int, input().split())
    out.append(str(dp[s-1][e-1]))
print("\n".join(out))


import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
best = float('inf')
ans = (0, 0, 0)
for i in range(n - 2):
    l, r = i + 1, n - 1
    while l < r:
        s = arr[i] + arr[l] + arr[r]
        if abs(s) < best:
            best = abs(s)
            ans = (arr[i], arr[l], arr[r])
        if s < 0:
            l += 1
        else:
            r -= 1
print(*ans)


import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
def dfs(x):
    global cnt
    visited[x] = 1
    cycle.append(x)
    nxt = arr[x]
    if visited[nxt] == 0:
        dfs(nxt)
    elif visited[nxt] == 1:
        for i in range(len(cycle)):
            if cycle[i] == nxt:
                cnt += len(cycle) - i
                break
    visited[x] = 2
    cycle.pop()
T = int(input())
for _ in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)
    cnt = 0
    for i in range(1, n + 1):
        if visited[i] == 0:
            cycle = []
            dfs(i)
    print(n - cnt)
