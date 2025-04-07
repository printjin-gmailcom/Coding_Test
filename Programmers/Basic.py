str = input()
print(str)


a, b = map(int, input().strip().split(' '))
print("a = " + str(a) + "\nb = " + str(b))


string, n = input().strip().split(' ')
n = int(n)  
print(string * n)


def solution():
    str_input = input()
    result = ""
    for i in range(len(str_input)):
        if str_input[i].isupper():
            result += str_input[i].lower() 
        else:
            result += str_input[i].upper() 
    return result
print(solution())  


print('!@#$%^&*(\\\'"<>?:;')


a, b = map(int, input().strip().split(' '))
print("{} + {} = {}".format(a, b, a + b))


str1, str2 = input().strip().split(' ')
ans = str1 + str2
print(ans.strip())  


str = input()
for s in str:
    print(s)


a = int(input())
if a % 2 == 0:
    print(str(a) + ' is even')
else:
    print(str(a) + ' is odd')


def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    return answer


def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i]
        answer += str2[i]
    return answer


def solution(arr):
    answer = ''
    for i in range(len(arr)):
        answer += arr[i] 
    return answer


def solution(my_string, k):
    answer = ''
    answer = my_string * k
    return answer


def solution(a, b):
    answer = 0
    ans1 = str(a) + str(b)
    ans2 = str(b) + str(a)
    answer = max(int(ans1), int(ans2)) 
    return answer  


def solution(a, b):
    answer = 0
    ans1 = str(a) +str(b)
    ans2 = 2*a*b
    answer = max(int(ans1), ans2)
    return answer


def solution(num, n):
    answer = 0
    if num % n == 0 :
        answer = 1
    return answer


def solution(number, n, m):
    answer = 0
    if number % n == 0:
        if number % m == 0 :
            answer = 1
        else:
            answer = 0
    return answer


def solution(n):
    answer = 0
    if n % 2 == 0:
        for i in range(0,n+1,2):
            answer += i**2
    else:
        for i in range(1,n+1,2):
            answer += i        
    return answer


def solution(ineq, eq, n, m):
    answer = 0
    if n <= m and ineq == '<' and eq == '=':
        answer = 1
    elif n >= m and ineq == '>' and eq == '=':
        answer = 1
    elif n < m and ineq == '<' and eq == '!':
        answer = 1
    elif n > m and ineq == '>' and eq == '!':
        answer = 1
    else:
        answer = 0
    return answer


def solution(a, b, flag):
    answer = 0
    if flag == True:
        answer = int(a)+int(b)
    else:
        answer = int(a)-int(b)
    return answer


def solution(a, b, c):
    answer = 0
    if a != b and b != c and a != c:
        answer = a + b + c
    elif a == b == c: 
        answer = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    else:
        answer = (a + b + c) * (a**2 + b**2 + c**2)
    return answer


def solution(num_list):
    a = sum(num_list) ** 2
    b = 1
    for num in num_list: 
        b *= num
    return 1 if b < a else 0


def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]: 
            answer += a + d * i 
    return answer


def solution(num_list):
    odd = ''
    even = ''
    for num in num_list:
        if num % 2 == 0:
            even += str(num)
        else:
            odd += str(num)
    answer = int(odd) + int(even)
    return answer


def solution(num_list):
    if num_list[-1] > num_list[-2]:
        a = num_list[-1] - num_list[-2]
        num_list.append(a)
    else:
        a = num_list[-1]*2
        num_list.append(a)
    return num_list


def solution(n, control):
    answer = n 
    con = {'w': 1, 's': -1, 'd': 10, 'a': -10}
    for cont in control:
        if cont in con:
            answer += con[cont]  
    return answer


def solution(numLog):
    answer = ''
    con = {1: 'w', -1: 's', 10: 'd', -10: 'a'}
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i-1]
        if diff in con:
            answer += con[diff] 
    return answer


def solution(arr, queries):
    for query in queries:
        i, j = query
        arr[i], arr[j] = arr[j], arr[i] 
    return arr


def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        j = [arr[i] for i in range(s, e + 1) if arr[i] > k]
        if j:
            answer.append(min(j))  
        else:
            answer.append(-1)
    return answer


def solution(arr, queries):
    for query in queries:
        s, e, k = query
        for i in range(s, e+1):
            if i % k == 0:
                arr[i] += 1
    return arr


def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        if all(digit in '50' for digit in str(i)):
            answer.append(i)
    if not answer:
        return [-1]
    return answer


def solution(start_num, end_num):
    answer = []
    for i in range(start_num, end_num+1):
        answer.append(i)
    return answer


def solution(n):
    answer = [n]
    while n != 1:
        if n % 2 == 0 :
            n = n // 2
            answer.append(n)
        elif n % 2 == 1:
            n = 3*n + 1
            answer.append(n)
    return answer


def solution(arr):
    stk = []  
    i = 0 
    
    while i < len(arr):
        if not stk:  
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]: 
            stk.append(arr[i])
            i += 1
        else: 
            stk.pop()
    
    return stk



def solution(x1, x2, x3, x4):
    if (x1 or x2) and (x3 or x4):
        return True
    else:
        return False


def solution(a, b, c, d):
    dice = sorted([a, b, c, d])
    if dice[0] == dice[3]:
        return 1111 * dice[0]
    if dice[0] == dice[2] or dice[1] == dice[3]:  
        p = dice[1]
        q = dice[0] if dice[0] != p else dice[3]  
        return (10 * p + q) ** 2
    if dice[0] == dice[1] and dice[2] == dice[3]:
        return (dice[0] + dice[2]) * abs(dice[0] - dice[2])
    if dice[0] == dice[1] or dice[1] == dice[2] or dice[2] == dice[3]: 
        if dice[0] == dice[1]:
            p, q, r = dice[0], dice[2], dice[3]
        elif dice[1] == dice[2]:
            p, q, r = dice[1], dice[0], dice[3]
        else:
            p, q, r = dice[2], dice[0], dice[1]
        return q * r
    return dice[0]


def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        answer += my_string[i]
    return answer


def solution(number):
    answer = 0
    answer = int(number) % 9
    return answer


def solution(my_string, queries):
    my_string = list(my_string)
    for querie in queries:
        s, e = querie 
        my_string[s:e+1] = my_string[s:e+1][::-1]
    return ''.join(my_string)


def solution(intStrs, k, s, l):
    answer = []
    for str in intStrs:
        st = str[s:s + l]
        if int(st) > k:
            answer.append(int(st))
    return answer


def solution(my_strings, parts):
    answer = ''
    for i in range(len(parts)):
        answer += my_strings[i][parts[i][0]:parts[i][1]+1]
    return answer


def solution(my_string, n):
    answer = my_string[-n:]
    return answer


def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i:])
    return sorted(answer) 


def solution(my_string, is_suffix):
    if my_string.endswith(is_suffix): 
        return 1
    return 0


def solution(my_string, n):
    answer = ''
    answer = my_string[:n]
    return answer


def solution(my_string, is_prefix):
    answer = 0
    if my_string[:len(is_prefix)] == is_prefix:
        answer = 1
    return answer


def solution(my_string, s, e):
    my_string = list(my_string)
    my_string[s:e + 1] = my_string[s:e + 1][::-1]
    return ''.join(my_string)


def solution(my_string, m, c):
    answer = ''
    for i in range(c-1, len(my_string), m):
        answer += my_string[i]
    return answer


def solution(q, r, code):
    answer = ''
    for i in range(len(code)):
        if i % q == r:
            answer += code[i]
    return answer


def solution(my_string):
    answer = [0] * 52
    for char in my_string:
        if 'A' <= char <= 'Z':
            answer[ord(char) - ord('A')] += 1
        elif 'a' <= char <= 'z':
            answer[ord(char) - ord('a') + 26] += 1
    return answer


def solution(n, k):
    answer = []
    for i in range(1, n+1):
        if i % k == 0:
            answer.append(i)
    return answer


def solution(my_string, indices):
    my_string = list(my_string) 
    for i in sorted(indices, reverse=True): 
        my_string.pop(i) 
    return ''.join(my_string) 


def solution(start_num, end_num):
    answer = []
    for i in range(start_num, end_num-1, -1):
        answer.append(i)
    return answer


def solution(n, slicer, num_list):
    a, b, c = slicer 
    if n == 1:
        answer = num_list[:b+1]
    elif n == 2:
        answer = num_list[a:]
    elif n == 3:
        answer = num_list[a:b+1]
    elif n == 4:
        answer = num_list[a:b+1:c]
    return answer


def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i 
    return -1 


def solution(arr, intervals):
    answer = arr[intervals[0][0]:intervals[0][1]+1] +arr[intervals[1][0]:intervals[1][1]+1]
    return answer


def solution(arr):
    if 2 not in arr:
        return [-1]
    first_index = arr.index(2) 
    last_index = len(arr) - 1 - arr[::-1].index(2)  
    if first_index == last_index:
        return [arr[first_index]]
    return arr[first_index:last_index + 1]


def solution(num_list, n):
    answer = num_list[n-1:] 
    return answer


def solution(num_list, n):
    answer = []
    a = num_list[:n]
    b = num_list[n:] 
    answer = b + a
    return answer


def solution(str_list):
    if 'l' not in str_list and 'r' not in str_list:
        return []
    left_index = str_list.index('l') if 'l' in str_list else float('inf')
    right_index = str_list.index('r') if 'r' in str_list else float('inf')
    if left_index < right_index:
        return str_list[:left_index]
    elif right_index < left_index:
        return str_list[right_index + 1:]
    else:
        return []


def solution(num_list, n):
    answer = []
    for i in range(0, n):
        answer.append(num_list[i])
    return answer


def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i])
    return answer


def solution(num_list):
    answer = 0
    even = 0
    odd = 0
    for i in range(0, len(num_list), 2):
        even += num_list[i]
    for j in range(1, len(num_list), 2): 
        odd += num_list[j]
    if even > odd:
        answer = even
    elif even < odd:
        answer = odd
    else:
        answer = even
    return answer


def solution(names):
    answer = []
    for i in range(0,len(names),5):
        answer.append(names[i])
    return answer


def solution(todo_list, finished):
    answer = []
    for i in range(len(todo_list)):
        if not finished[i]:  
            answer.append(todo_list[i])
    return answer


def solution(numbers, n):
    answer = 0
    for num in numbers:
        answer += num
        if answer > n:  
            break
    return answer


def solution(arr, queries):
    for query in queries:
        start, end = query
        for i in range(start, end + 1):
            arr[i] += 1
    return arr


def solution(arr):
    answer = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            answer.append(i // 2)  
        elif i < 50 and i % 2 == 1:
            answer.append(i * 2) 
        else:
            answer.append(i) 
    return answer


def solution(num_list):
    answer = 0
    for num in num_list:
        while num > 1:
            if num % 2 == 0:
                num = num // 2 
            else:
                num = (num - 1) // 2 
            answer += 1
    return answer


def solution(num_list):
    answer = 0
    if len(num_list) >= 11:
        for num in num_list:
            answer += num
    else:
        answer = 1
        for num in num_list:
            answer *= num
    return answer


def solution(myString, pat):
    answer = 0
    myString = myString.lower()
    pat = pat.lower()
    if pat in myString:
        answer = 1
    return answer


def solution(myString):
    myString = myString.upper()
    return myString


def solution(myString):
    answer = myString.lower()
    return answer


def solution(strArr):
    for i in range(0, len(strArr), 2):
        strArr[i] = strArr[i].lower() 
        if i + 1 < len(strArr):  
            strArr[i+1] = strArr[i+1].upper() 
    return strArr


def solution(myString):
    return myString.lower().replace('a', 'A')


def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())


def solution(my_string, pat):
    str = my_string.rfind(pat)  
    return my_string[:str + len(pat)] 


def solution(myString, pat):
    count = 0
    idx = 0
    while idx != -1:
        idx = myString.find(pat, idx)
        if idx != -1:
            count += 1
            idx += 1 
    return count


def solution(strArr):
    answer = []
    for arr in strArr:
        if 'ad' not in arr:
            answer.append(arr)
    return answer


def solution(my_string):
    answer = []
    answer = my_string.split()
    return answer


def solution(my_string):
    answer = []
    answer = my_string.split()
    return answer


def solution(myString):
    answer = []
    str = myString.split('x')
    for i in range(len(str)):
        answer.append(len(str[i]))
    return answer


def solution(myString):
    answer = []
    answer += sorted([s for s in myString.split('x') if s]) 
    return answer


def solution(binomial):
    answer = 0
    a, op, b = binomial.split(' ')
    if op == '+' :
        answer = int(a) + int(b)
    elif op == '-':
        answer = int(a) - int(b)
    elif op == '*':
        answer = int(a)*int(b)
    return answer


def solution(myString, pat):
    string = myString.replace('A', '#').replace('B', 'A').replace('#', 'B')
    return 1 if pat in string else 0


def solution(rny_string):
    return rny_string.replace('m', 'rn')


def solution(myStr):
    for char in ['a', 'b', 'c']:
        myStr = myStr.replace(char, ' ') 
    answer = [str for str in myStr.split(' ') if str] 
    if not answer: 
        answer = ["EMPTY"]
    return answer


def solution(arr):
    answer = []
    for i in arr:
        for j in range(i):
            answer.append(i)
    return answer


def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        if flag[i] == True:
            answer += [arr[i]] * (arr[i] * 2) 
        else:
            for _ in range(arr[i]): 
                if answer:
                    answer.pop()
    return answer


def solution(arr):
    answer = []
    
    for num in arr:
        if not answer:  
            answer.append(num)
        elif answer[-1] == num: 
            answer.pop()
        else:  
            answer.append(num)
    if not answer: 
        return [-1]
    return answer


def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
        if len(answer) == k:
            break 
    while len(answer) < k:
        answer.append(-1)
    return answer


def solution(arr):
    length = len(arr)
    next = 1
    while next < length:
        next *= 2
    while len(arr) < next:
        arr.append(0)
    return arr


def solution(arr1, arr2):
    answer = 0
    if len(arr1) != len(arr2):
        if len(arr1) > len(arr2):
            answer = 1
        else:
            answer = -1
    else:
        sum1 = sum(arr1)
        sum2 = sum(arr2)
        if sum1 > sum2:
            answer = 1
        elif sum1 < sum2:
            answer = -1
        else:
            answer = 0
    return answer


from collections import Counter
def solution(strArr):
    count = Counter(len(s) for s in strArr) 
    answer = max(count.values()) 
    return answer


def solution(arr, n):
    if len(arr) % 2 == 0:
        for i in range(0, len(arr), 2):
            arr[i+1] = arr[i+1]+n
    else:
        for i in range(0, len(arr), 2):
            arr[i] = arr[i]+n        
    return arr


def solution(num_list):
    answer = []
    num_list.sort()
    answer = num_list[:5]
    return answer


def solution(num_list):
    answer = []
    num_list.sort()
    answer = num_list[5:]
    return answer


def solution(rank, attendance):
    answer = 0
    a = []
    for i in range(len(rank)):
        if attendance[i]:
            a.append((i, rank[i]))    
    a.sort(key=lambda x: x[1])
    answer = 10000 * a[0][0] + 100 * a[1][0] + a[2][0]
    return answer


def solution(flo):
    answer = int(flo)
    return answer


def solution(num_str):
    answer = 0
    for i in num_str:
        answer += int(i)
    return answer


def solution(n_str):
    answer = 0
    answer = int(n_str)
    return answer 


def solution(n_str):
    answer = ''
    answer = n_str.lstrip('0')
    return answer


def solution(a, b):
    answer = str(int(a) + int(b))
    return answer


def solution(n):
    return str(n)


def solution(arr, delete_list):
    answer = []
    for element in arr:
        if element not in delete_list:
            answer.append(element)
    return answer


def solution(my_string, target):
    answer = 0
    if target in my_string:
        answer = 1
    return answer


def solution(str1, str2):
    answer = 0
    if str1 in str2:
        answer = 1
    return answer


def solution(str_list, ex):
    answer = ''
    for str_item in str_list:
        if ex not in str_item:
            answer += str_item
    return answer


def solution(num_list, n):
    answer = 0
    for num in num_list:
        if n is num:
            answer = 1
            break
    return answer


def solution(a, b):
    if a % 2 != 0 and b % 2 != 0:
        answer = a**2 + b**2
    elif a % 2 != 0 or b % 2 != 0:
        answer = 2 * (a + b)
    else:
        answer = abs(a - b)
    return answer


def solution(date1, date2):
    if date1[0] < date2[0]:  
        return 1
    elif date1[0] > date2[0]:
        return 0
    elif date1[1] < date2[1]:  
        return 1
    elif date1[1] > date2[1]:
        return 0
    elif date1[2] < date2[2]: 
        return 1
    elif date1[2] > date2[2]:
        return 0
    else:
        return 0  


def solution(order):
    answer = 0
    for drink in order:
        if 'americano' in drink:
            answer += 4500
        elif 'latte' in drink:
            answer += 5000
        elif 'anything' in drink:
            answer += 4500
    return answer


def solution(picture, k):
    answer = []
    for row in picture:
        new_row = ""
        for char in row:
            new_row += char * k  
        for _ in range(k): 
            answer.append(new_row)
    return answer


def solution(arr, k):
    answer = []
    if k % 2 == 0:
        for i in range(len(arr)):
            answer.append(arr[i] + k)  
    else:
        for i in range(len(arr)):
            answer.append(arr[i] * k)
    return answer


def solution(myString):
    answer = ''
    alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    for char in myString:
        if char in alp:
            answer += 'l'
        else:
            answer += char
    return answer


def solution(n):
    answer = [[0] * n for _ in range(n)] 
    for i in range(n):
        for j in range(n):
            if i == j:
                answer[i][j] = 1
    return answer


def solution(arr):
    answer = 1 
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != arr[j][i]:
                answer = 0  
                return answer 
    return answer


def solution(arr):
    rows = len(arr)  
    cols = len(arr[0]) if rows > 0 else 0  
    if rows > cols:
        for i in range(rows):
            arr[i].extend([0] * (rows - cols))    
    elif cols > rows:
        for i in range(cols):
            if i >= rows:
                arr.append([0] * cols) 
    return arr


def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i + j) <= k :
                answer += board[i][j]
    return answer