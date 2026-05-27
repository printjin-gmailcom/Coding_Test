# 1291

a, b = map(int, input().split())

while True:
    if a > 1 and a < 10 and b > 1 and b < 10:
        if a > b:
            for i in range(1, 10):
                for j in range(a, b-1, -1):
                    print(f"{j} * {i} = {i*j:>2}", end="   ")
                print()
            break
        else:
            for i in range(1, 10):
                for j in range(a, b+1):
                    print(f"{j} * {i} = {i*j:>2}", end="   ")
                print()
            break
    else:
        print("INPUT ERROR!")
        a, b = map(int, input().split())


# 1341

inputValue = input()
x = int(inputValue.split(' ')[0])
y = int(inputValue.split(' ')[1])

for idx in range(abs(x - y)+1):
    if x-y > 0: idx = idx * -1
    for num in range(1, 10):
        print(f"{x + idx} * {num} = {str((x + idx) * num).rjust(2)}   ", end="")
        if num % 3 == 0: print("", end="\n")
    print("")


# 1303

n, m = map(int, input().split())

for i in range(n):
    for j in range(m):
        print(i * m + j + 1, end=" ")
    print()


# 1856

inputValue = input()
x = int(inputValue.split(' ')[0])
y = int(inputValue.split(' ')[1])

count = 0
for idx in range(1, x+1):
    for sub_idx in range(1, y+1):
        if idx % 2 == 0:
            count -= 1
            print(count, end=" ")
        else:
            count += 1
            print(count, end=" ")
    if idx % 2 == 1:
        count = count + y + 1
    else:
        count = count + y - 1
    print("")


# 1304

n = int(input())

for i in range(1, n + 1):
    for j in range(i, n * n + 1, n):
        print(j, end=" ")
    print()


# 5931

n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i, end=" ")
    print()


# 5932
#https://jungol.co.kr/problem/5932?cursor=eyJwcm9ibGVtc2V0IjoiNiIsImZpZWxkIjowLCJpZHgiOjZ9


# 5933

n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end=" ")
    print()


# 1307

while 1:
    n = int(input())
    if n < 1 or n > 100:
        continue
    else:
        for i in range(1, n+1):
            for j in range(1, n+1):
                print(chr(((n-i) + n*(n-j))%26 + 65), end=' ')
            print()
        break


# 1314

n = int(input())
alphabet = [chr(ord('A') + i) for i in range(26)]
square = [['' for _ in range(n)] for _ in range(n)]

idx = 0
for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            square[j][i] = alphabet[idx % 26]
        else:
            square[n - j - 1][i] = alphabet[idx % 26]
        idx += 1
for row in square:
    print(*row)


# 1338

n=int(input())
for i in range(n):
    v=i
    w=n
    for j in range(n):
        if i+j+1>=n:
            print(chr(v%26+65), end=' ')
            w-=1; v+=w
        else:
            print(' ', end=' ')
    print()


# 1339

n=int(input())
if 1<=n<=100 and n%2!=0:
    for i in range(n):
        for j in range(n):
            v=abs(j-n//2)**2
            if abs(i-n//2)+j<=n//2:
                print(chr((v+i-j)%26+65), end=' ')
            else: print(' ', end=' ')
        print()
else: print("INPUT ERROR")


# 9501

print("첫 번째 프로그램입니다.")


# 700

print("Python")


# 9502

print("두 번째 프로그램입니다.")
print(2)
print("번째 프로그램입니다.")


# 701

print("Score:")
print(100)
print("GREAT!")


# 702

print("My height")
print(170)
print("My weight")
print(68.6)


# 9503

print("3 번째 프로그램입니다.")
print("3 번째 프로그램입니다.")


# 703

print("1plus1", '=' , "Gwi yo mi")


# 9504

print('   @@')
print('  @  @')
print(' @    @')
print('@      @')
print(' @    @')
print('  @  @')
print('   @@')


# 704

print("(@) (@)\n(=^.^=)\n(-m-m-)")


# 9505

print("수식을 계산해봅시다.\n5 + 2\n7")


# 705

print("5 Dan")
print("5 * 2 =", 5 * 2)


# 706

print("6 + 2 =", 6 + 2 )
print("6 - 2 =", 6 - 2 )
print("6 * 2 =", 6 * 2)
print("6 / 2 =", 6 / 2)


# 707

print("My name is Hong")


# 708

print("My hometown\nFlowering mountain")


# 709

print("TTTTTTTTTT\nTTTTTTTTTT\n    TT\n    TT\n    TT")


# 710

print("kor 90\nmat 80\neng 100\nsum", 90 + 80 + 100)
