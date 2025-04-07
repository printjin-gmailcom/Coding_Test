def solution(babbling):
    answer = 0
    sounds = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        for sound in sounds:
            if sound * 2 in word:
                break
            word = word.replace(sound, " ")
        if word.strip() == "":
            answer += 1
    return answer


def solution(common):
    answer = 0
    if common[1] - common[0] == common[2] - common[1]:
        difference = common[1] - common[0]
        answer = common[-1] + difference
    else:  
        ratio = common[1] // common[0]
        answer = common[-1] * ratio
    return answer


def solution(num, total):
    start = (total - (num * (num - 1)) // 2) // num
    return [start + i for i in range(num)]


def solution(M, N):
    answer = 0
    if M == 1 and N == 1:
        answer = 0
    elif M != 1 and N == 1:
        answer = M-1
    elif M == 1 and N != 1:
        answer = N-1
    else:
        answer = (M-1) + M*(N-1)
    return answer


def solution(A, B):
    if A == B :
        return 0
    else:
        for i in range(len(A)):
            A = A[-1] + A[:-1]
            if A == B:
                return i + 1 
        return -1


import textwrap
def solution(my_str, n):
    return textwrap.wrap(my_str, n)


def solution(array):
    answer = 0
    for i in array:
        answer += str(i).count('7')
    return answer


def solution(my_string):
    string = list(my_string.lower())
    string.sort()
    answer = ''.join(string)
    return answer


def solution(n, t):
    answer = 0
    answer = n * (2 ** t)
    return answer


import math
def solution(n):
    answer = 0
    if math.isqrt(n)**2 == n:
        answer = 1
    else:
        answer = 2
    return answer


def solution(str1, str2):
    answer = 0
    if str2 in str1:
        answer = 1
    else:
        answer = 2
    return answer


def solution(quiz):
    answer = []
    for i in quiz:
        m = i.split(' = ')
        expression = m[0]
        result = int(m[1])
        calculated_result = eval(expression)
        if calculated_result == result:
            answer.append("O")
        else:
            answer.append("X")
    return answer


def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer


def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)
        else:
            answer = answer
    return answer


def solution(num, k):
    num_str = str(num)  
    if str(k) in num_str:  
        return num_str.index(str(k)) + 1  
    else:
        return -1 


def solution(s1, s2):
    answer = 0
    for i in s1:
        for j in s2:
            if i == j:
                answer += 1
            else:
                answer = answer
    return answer


def solution(my_string):
    elements = my_string.split()
    answer = int(elements[0])
    for i in range(1, len(elements), 2):
        operator = elements[i]
        num = int(elements[i + 1])
        if operator == '+':
            answer += num
        elif operator == '-':
            answer -= num
    return answer


def solution(array):
    answer = []
    max_value = max(array)
    max_index = array.index(max_value)
    answer.append(max_value)
    answer.append(max_index)
    return answer


def solution(message):
    answer = 0
    answer = len(message)*2
    return answer


def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            answer.append(i)
        else:
            answer = answer
    return answer


from collections import Counter
def solution(s):
    count = Counter(s)
    answer = [a for a, b in count.items() if b == 1]
    answer.sort()
    return ''.join(answer)


def solution(my_string, num1, num2):
    str_list = list(my_string)
    str_list[num1], str_list[num2] = str_list[num2], str_list[num1]
    return ''.join(str_list)


def solution(numbers):
    answer = 0
    num = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    for word in num:
        if word in numbers:
            numbers = numbers.replace(word, str(num[word]))
    answer = int(numbers)
    return answer


def solution(my_string):
    answer = ''
    for i in my_string:
        if i.islower() == True:
            answer += i.upper()
        else:
            answer += i.lower()
    return answer


def solution(cipher, code):
    answer = ''
    for i in range(code - 1, len(cipher), code): 
        answer += cipher[i]
    return answer


def solution(order):
    answer = 0
    for i in str(order):
        if i == '3' or i == '6' or i == '9': 
            answer += 1
        else:
            answer += 0
    return answer


def solution(array, n):
    answer = array[0]
    min_diff = abs(array[0] - n)
    for i in array[1:]:
        diff = abs(i - n)
        if diff < min_diff:
            min_diff = diff
            answer = i
        elif diff == min_diff: 
            answer = min(answer, i)
    return answer


def solution(sides):
    answer = 0
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
        answer = 1
    else:
        answer = 2
    return answer


def solution(my_string):
    answer = ''
    li = set()
    for i in my_string:
        if i not in li:
            li.add(i)
            answer += i
    return answer


def solution(i, j, k):
    answer = 0
    for l in range(i, j+1):
        answer += str(l).count(str(k))
    return answer


def solution(before, after):
    answer = 0
    if sorted(before) == sorted(after):
        answer = 1
    else:
        answer = 0
    return answer


def solution(bin1, bin2):
    answer = ''
    answer = bin(int(bin1,2)+int(bin2,2))
    return answer[2:]


def solution(chicken):
    answer = 0
    while chicken >= 10:  
        free_chickens = chicken // 10  
        answer += free_chickens 
        chicken = free_chickens + (chicken % 10)  
    return answer


def solution(id_pw, db):
    for user in db:
        if user[0] == id_pw[0]: 
            if user[1] == id_pw[1]: 
                return 'login'
            else: 
                return 'wrong pw'
    return 'fail'


def solution(score):
    answer = []
    averages = [(sum(user) / 2) for user in score]  
    sorted_averages = sorted(averages, reverse=True)  
    for avg in averages:
        answer.append(sorted_averages.index(avg) + 1)
    return answer


def solution(numlist, n):
    answer = []
    a = []
    for num in numlist:
        ab = abs(num - n)
        a.append((ab, num))
    a.sort(key=lambda x: (x[0], -x[1]))
    for ab, num in a:
        answer.append(num)
    return answer


import math
def solution(a, b):
    gcd = math.gcd(a, b)
    a //= gcd
    b //= gcd
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    if b == 1:
        return 1
    else:
        return 2 


def solution(lines):
    answer = 0
    line_map = [0] * 201
    for start, end in lines:
        for i in range(start + 100, end + 100):
            line_map[i] += 1
    for i in range(len(line_map)):
        if line_map[i] > 1:
            answer += 1
    return answer


def solution(dots):
    def slope(dot1, dot2):
        return (dot2[1] - dot1[1]) / (dot2[0] - dot1[0]) if dot2[0] != dot1[0] else float('inf')
    combinations = [
        (0, 1, 2, 3),  # 점 1-2와 점 3-4
        (0, 2, 1, 3),  # 점 1-3과 점 2-4
        (0, 3, 1, 2)   # 점 1-4와 점 2-3
    ]
    for comb in combinations:
        dot1, dot2, dot3, dot4 = dots[comb[0]], dots[comb[1]], dots[comb[2]], dots[comb[3]]
        if slope(dot1, dot2) == slope(dot3, dot4):
            return 1
    return 0


def solution(n):
    answer = 0
    count = 0 
    num = 1 
    while count < n:
        if '3' not in str(num) and num % 3 != 0:
            count += 1
            if count == n:
                answer = num
        num += 1
    return answer


def solution(spell, dic):
    answer = 2 
    for i in dic:
        if set(i) == set(spell):
            answer = 1 
            break 
    return answer


def solution(sides):
    sides.sort() 
    a, b = sides[0], sides[1]  
    return (a + b - 1) - (abs(a - b) + 1) + 1


def solution(board):
    answer = 0
    count = 0
    n = len(board)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                count += 1
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 0:
                        answer += 1
                        board[ni][nj] = -1
    return n*n - count - answer


def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())


def solution(polynomial):
    po = polynomial.split(' + ')
    x_sum = 0 
    constant_sum = 0  
    answer = ""  
    
    for i in po:
        if 'x' in i:
            if i == 'x':  
                x_sum += 1
            else:  
                x_sum += int(i[:-1])
        else: 
            constant_sum += int(i)

    if x_sum > 0:
        if x_sum == 1:
            answer += "x"
        else:
            answer += f"{x_sum}x"

    if constant_sum > 0:
        if x_sum > 0:
            answer += " + "
        answer += str(constant_sum)

    return answer





def solution(polynomial):
    xnum = 0
    const = 0
    for c in polynomial.split(' + '):
        if c.isdigit():
            const+=int(c)
        else:
            xnum = xnum+1 if c=='x' else xnum+int(c[:-1])
    if xnum == 0:
        return str(const)
    elif xnum==1:
        return 'x + '+str(const) if const!=0 else 'x'
    else:
        return f'{xnum}x + {const}' if const!=0 else f'{xnum}x'


def solution(numbers):
    answer = 0
    numbers.sort()
    answer1 = numbers[-1]*numbers[-2]
    answer2 = numbers[0]*numbers[1]
    answer = max(answer1, answer2)
    return answer


def solution(keyinput, board):
    x, y = 0, 0 
    directions = {'left': (-1, 0), 'down': (0, -1), 'right': (1, 0), 'up': (0, 1)}
    max_x = board[0] // 2
    max_y = board[1] // 2
    for key in keyinput:
        if key in directions:
            dx, dy = directions[key]
            new_x, new_y = x + dx, y + dy
            
            if -max_x <= new_x <= max_x:
                x = new_x
            if -max_y <= new_y <= max_y:
                y = new_y
    return [x, y]


def solution(dots):
    x_coords = [dot[0] for dot in dots]
    y_coords = [dot[1] for dot in dots]
    width = max(x_coords) - min(x_coords)
    height = max(y_coords) - min(y_coords)
    return width * height


def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer


def solution(s):
    answer = 0
    last_added = 0  
    for i in s.split():
        if i == 'Z':  
            answer -= last_added
        else:
            answer += int(i) 
            last_added = int(i)   
    return answer


def solution(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return sorted(set(factors))


def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit():
            answer += int(i)
        else:
            answer = answer
    return answer


def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit() == True:
            answer.append(int(i))
    answer.sort()
    return answer


def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in 'aeiou':
            answer += i
    return answer


def solution(n):
    num = 1 
    i = 1 
    while num <= n:
        i += 1 
        num *= i  
    return i - 1  


def solution(numbers):
    numbers.sort()
    answer = numbers[-1] * numbers[-2]
    return answer


def solution(n):
    answer = 0
    for i in range(4, n+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count >= 3:
            answer += 1
    return answer


def solution(box, n):
    answer = 0
    answer = (box[0] // n) * (box[1] // n) * (box[2] //n) 
    return answer


def solution(numbers, direction):
    if direction == "left":
        return numbers[1:] + [numbers[0]]
    elif direction == "right":
        return [numbers[-1]] + numbers[:-1]


def solution(numbers, k):
    answer = (2 * (k - 1)) % len(numbers)
    return numbers[answer]


def solution(num_list, n):
    return [num_list[i:i+n] for i in range(0, len(num_list), n)]


def solution(dot):
    answer = 0
    if dot[0] > 0 and dot[1] > 0:
        answer = 1
    elif dot[0] < 0 and dot[1] > 0:
        answer = 2
    elif dot[0] < 0 and dot[1] < 0:
        answer = 3
    else:
        answer = 4
    return answer


import math
def solution(balls, share):
    return math.factorial(balls) // (math.factorial(share) * math.factorial(balls - share))


def solution(rsp):
    answer = ''
    for i in rsp:
        if i == '0':
            answer += '5'
        elif i == '2' :
            answer += '0'
        elif i == '5' :
            answer += '2'
    return answer


def solution(letter):
    answer = ''
    morse = { '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f', '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l', '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r', '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x', '-.--':'y','--..':'z'}
    result = letter.split(' ')
    for i in result:
        if i in morse:
            answer += morse[i]
    return answer


def solution(hp):
    answer = 0
    answer1 = hp // 5  
    hp1 = hp - answer1 * 5 
    answer2 = hp1 // 3 
    hp2 = hp1 - answer2 * 3 
    answer = answer1 + answer2 + hp2  
    return answer


def solution(n):
    answer = 0
    for a in range(1, n+1):
        if n % a == 0:
            answer += 1
        else:
            answer = answer
    return answer


def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    return [sorted_emergency.index(i) + 1 for i in emergency]


def solution(age):
    return ''.join(chr(ord('a') + int(digit)) for digit in str(age))


def solution(numbers, num1, num2):
    answer = []
    answer = numbers[num1 : num2+1]
    return answer


def solution(n):
    answer = 0
    for i in range(0, n+1, 2):
        answer += i
    return answer


def solution(n, k):
    answer = 0
    answer = int(n*12000 + (k-n//10)*2000)
    return answer


def solution(angle):
    answer = 0
    if angle < 90 and angle > 0 :
        answer = 1
    if angle == 90:
        answer = 2
    if angle < 180 and angle > 90 :
        answer = 3
    if angle == 180:
        answer = 4
    return answer


def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if letter != i:
            answer += i     
    return answer


def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i*n
    return answer


def solution(num_list):
    answer = []
    a = 0
    b = 0
    for i in num_list:
        if i % 2 == 0:
            a += 1
        else:
            b += 1
    answer.append(a)
    answer.append(b)
    return answer


n = int(input())
for i in range(1, n+1):
    print('*'*i)


def solution(my_string):
    answer = ''
    my_string = my_string[::-1]
    answer = my_string
    return answer


def solution(num_list):
    return num_list[::-1]


def solution(age):
    answer = 0
    answer = 2022 - int(age-1)
    return answer


def solution(money):
    answer = []
    a = money//5500
    b = money - 5500*a
    answer.append(a)
    answer.append(b)
    return answer


def solution(price):
    answer = 0
    if price >= 500000:
        return int(price * 0.8) 
    elif price >= 300000:
        return int(price * 0.9) 
    elif price >= 100000:
        return int(price * 0.95)
    else:
        return price  
    return answer


def solution(numbers):
    return sum(numbers) / len(numbers)


def solution(slice, n):
    answer = 0
    if n % slice == 0:
        answer = n // slice
    else:
        answer = n // slice + 1    
    return answer


import math
def solution(n):
    return (n * 6) // math.gcd(n, 6) // 6


def solution(n):
    answer = 0
    if n % 7 == 0:
        answer = n //7
    else:
        answer = n // 7 +1
    return answer


def solution(n):
    answer = []
    for i in range(0, n+1):
        if i % 2 == 1 :
            answer.append(i)
    return answer


from collections import Counter
def solution(array):
    counter = Counter(array)
    most_common = counter.most_common() 
    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        return -1
    return most_common[0][0]



def solution(array):
    answer = 0
    array.sort()
    a = len(array)//2
    answer = array[a]
    return answer


def solution(num1, num2):
    answer = -1
    answer = num1 % num2
    return answer


def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(number*2)
    return answer


import math
def solution(numer1, denom1, numer2, denom2):
    common_denominator = denom1 * denom2
    new_numer = numer1 * denom2 + numer2 * denom1
    gcd = math.gcd(new_numer, common_denominator)
    return [new_numer // gcd, common_denominator // gcd]


def solution(num1, num2):
    answer = 0
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    return answer


def solution(num1, num2):
    answer = 0
    answer = int(num1/num2*1000)
    return answer


def solution(num1, num2):
    answer = 0
    answer = int(num1)//int(num2)
    return answer


def solution(num1, num2):
    answer = 0
    answer = int(num1)*int(num2)
    return answer


def solution(num1, num2):
    answer = 0
    answer = int(num1 - num2)
    return answer


def solution(num1, num2):
    answer = -1
    answer = int(num1) + int(num2)
    return answer


def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
        else:
            answer = answer
    return answer


def solution(array, n):
    answer = 0
    for i in array:
        if i == n :
            answer += 1
        else:
            answer= answer
    return answer