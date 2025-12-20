def solution(n, m, section):
    answer = 0
    last_painted = 0 
    for s in section: 
        if s > last_painted: 
            last_painted = s + m - 1 
            answer += 1 
    return answer


def solution(s):
    answer = int(s)
    return answer


def solution(n):
    if n == 0:
        return 0
    return sum(i for i in range(1, n + 1) if n % i == 0)


def solution(n):
    answer = sum(int(digit) for digit in str(n))
    return answer


def solution(num):
    answer = ''
    if num % 2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer


from statistics import mean
def solution(arr):
    answer = mean(arr)
    return answer    


def solution(n):
    answer = []
    for i in str(n)[::-1]:
        answer.append(int(i))
    return answer


def solution(a, b):
    answer = 0
    if a == b:
        answer = a
    elif a < b:
        for i in range(a, b+1):
            answer += int(i)
    else:
        for j in range(b, a+1):
            answer += int(j)
    return answer


def solution(s):
    s = s.lower()  
    return s.count('p') == s.count('y')


def solution(n):
    ans = sorted(str(n), reverse=True) 
    return int("".join(ans))


import math
def solution(n):
    a = math.sqrt(n) 
    if a.is_integer():
        return int((a + 1) ** 2) 
    return -1


def solution(x):
    answer = False
    sum = 0
    for i in str(x):
        sum += int(i)
    if x % sum == 0:
        answer = True
    return answer


def solution(arr, divisor):
    answer = [a for a in arr if a % divisor == 0] 
    answer.sort()
    if not answer: 
        answer = [-1]
    return answer


def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            ans = i
            break
    answer = f'김서방은 {ans}에 있다'
    return answer


def solution(num):
    answer = 0
    n = 0
    while n < 500 and num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num*3 +1
        n += 1
    if n >= 500:
        answer = -1
    elif num == 1:
        answer =  n
    return answer


def solution(arr):
    if len(arr) == 1:
        return [-1]
    min_val = min(arr) 
    arr.remove(min_val)
    return arr 


def solution(phone_number):
    answer = '*' * (len(phone_number) - 4) + phone_number[-4:]
    return answer


def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        a = len(s)//2
        answer = s[a-1:a+1]
    else:
        a = len(s)//2
        answer = s[a]
    return answer


def solution(n):
    answer = ''
    if n % 2 == 0:
        answer = '수박'*(n//2)
    else:
        answer = '수박'*(n//2) +'수'
    return answer


def solution(s):
    answer = ''.join(sorted(s, reverse=True))  
    return answer


def solution(s):
    answer = False  
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        answer = True
    return answer


def solution(arr1, arr2):
    return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]


def solution(s):
    numbers = list(map(int, s.split()))
    minv = min(numbers)
    maxv = max(numbers)
    return f"{minv} {maxv}"


a, b = map(int, input().strip().split(' '))
for _ in range(b):
    for _ in range(a):
        print('*', end='')
    print()     


def solution(A, B):
    A.sort()  
    B.sort(reverse=True) 
    answer = 0
    for i in range(len(A)):
        answer += A[i] * B[i]  
    return answer


from math import gcd
def lcm(n, m):
    return abs(n * m) // gcd(n, m)
def solution(n, m):
    answer = [gcd(n, m), lcm(n, m)]
    return answer


def solution(t, p):
    answer = 0
    for i in range(len(t) - len(p) + 1):
        if t[i:i+len(p)] <= p:  
            answer += 1
    return answer


def solution(n):
    answer = 0
    start, end, sum_val = 1, 1, 1  
    while start <= n: 
        if sum_val < n:  
            end += 1
            sum_val += end  
        elif sum_val > n:  
            sum_val -= start  
            start += 1  
        else:  
            answer += 1  
            sum_val -= start  
            start += 1  
    return answer


def solution(s):
    answer = []
    words = s.split(" ") 
    for word in words:
        new_word = ""
        for i in range(len(word)):  
            if i % 2 == 0:  
                new_word += word[i].upper() 
            else:  
                new_word += word[i].lower()  
        answer.append(new_word) 
    return " ".join(answer)  


from itertools import combinations
def solution(number):
    answer = 0
    for comb in combinations(number, 3):  
        if sum(comb) == 0:  
            answer += 1  
    return answer


def solution(n):
    answer = float('inf')
    for i in range(n + 1, 2 * n + 1):
        if bin(i).count('1') == bin(n).count('1'): 
            answer = i 
            break 
    return answer


def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ': 
            answer += ' '
        elif 'a' <= s[i] <= 'z': 
            new_char = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a')) 
            answer += new_char
        elif 'A' <= s[i] <= 'Z':  
            new_char = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))  
            answer += new_char
    return answer


def solution(s):
    answer = []
    li = {}
    for i, a in enumerate(s): 
        if a in li:
            answer.append(i - li[a])  
        else:
            answer.append(-1) 
        li[a] = i 
    return answer


def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2) 
    answer += '0'
    for i in range(len(food) - 1, 0, -1): 
        answer += str(i) * (food[i] // 2)
    return answer


def solution(strings, n):
    strings.sort(key=lambda x: (x[n], x))  
    return strings


def solution(a, b, n):
    answer = 0  
    while n >= a:  
        exchange = (n // a) * b 
        answer += exchange 
        n = n % a + exchange 
    return answer


from math import gcd
from functools import reduce
def solution(arr):
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    answer = reduce(lcm, arr)
    return answer


from collections import Counter
def solution(k, tangerine):
    counter = Counter(tangerine)
    frequency = sorted(counter.values(), reverse=True)
    count = 0
    types = 0
    for f in frequency:
        count += f
        types += 1
        if count >= k:
            break
    return types


def solution(cards1, cards2, goal):
    idx1 = idx2 = 0
    for word in goal:
        if idx1 < len(cards1) and cards1[idx1] == word:
            idx1 += 1
        elif idx2 < len(cards2) and cards2[idx2] == word:
            idx2 += 1
        else:
            return "No"
    return "Yes"


def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        a = 0
        for n in range(len(name)):
            if name[n] in photo[i]: 
                a += yearning[n] 
        answer.append(a) 
    return answer


def solution(n, m, section):
    answer = 0
    last_painted = 0 
    for s in section: 
        if s > last_painted: 
            last_painted = s + m - 1 
            answer += 1 
    return answer


def solution(land):
    for i in range(1, len(land)):
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])
    
    return max(land[-1])


def solution(n, s):
    if s < n:
        return [-1]
    quotient, remainder = divmod(s, n)
    result = [quotient] * n
    for i in range(remainder):
        result[i] += 1
    return sorted(result)


def solution(n):
    MOD = 1000000007
    if n == 1:
        return 1
    elif n == 2:
        return 2
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    return dp[n]


from collections import Counter
def solution(weights):
    count = 0
    weight_count = Counter(weights)
    for weight in weight_count:
        if weight_count[weight] > 1:
            count += weight_count[weight] * (weight_count[weight] - 1) // 2
    for weight in weight_count:
        if weight * 2 / 3 in weight_count:
            count += weight_count[weight] * weight_count[weight * 2 / 3]
        if weight * 2 / 4 in weight_count:
            count += weight_count[weight] * weight_count[weight * 2 / 4]
        if weight * 3 / 4 in weight_count:
            count += weight_count[weight] * weight_count[weight * 3 / 4]
    return count


def solution(players, callings):
    player_index = {player: i for i, player in enumerate(players)}
    for calling in callings:
        current_index = player_index[calling]
        if current_index > 0:
            player_in_front = players[current_index - 1]
            players[current_index], players[current_index - 1] = players[current_index - 1], players[current_index]
            player_index[calling] -= 1
            player_index[player_in_front] += 1
    return players


def solution(sequence):
    n = len(sequence)
    pulse1 = [0] * n
    pulse2 = [0] * n
    for i in range(n):
        if i % 2 == 0:
            pulse1[i] = sequence[i]
            pulse2[i] = -sequence[i]
        else:
            pulse1[i] = -sequence[i]
            pulse2[i] = sequence[i]
    def max_subarray_sum(arr):
        max_ending_here = max_so_far = arr[0]
        for x in arr[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
    return max(max_subarray_sum(pulse1), max_subarray_sum(pulse2))


def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1
    for coin in money:
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin]
            dp[i] %= 1000000007
    return dp[n]


import heapq
def solution(k, score):
    answer = []
    hall_of_fame = []
    for s in score:
        heapq.heappush(hall_of_fame, s)
        if len(hall_of_fame) > k:
            heapq.heappop(hall_of_fame) 
        answer.append(hall_of_fame[0])
    return answer


def solution(s):
    answer = 0
    count_x = 0
    count_other = 0     
    for i in range(len(s)):
        if count_x == count_other: 
            answer += 1
            count_x = 0
            count_other = 0
        if s[i] == s[0]: 
            count_x += 1
        else: 
            count_other += 1
    if count_x != count_other:
        answer += 1
    return answer


def solution(s):
    answer = 0
    x_cnt = 0
    non_x_cnt = 0
    x = s[0]
    for idx, char in enumerate(s):
        if char == x:
            x_cnt += 1
        else:
            non_x_cnt += 1
        if x_cnt == non_x_cnt:
            answer += 1
            x_cnt, non_x_cnt = 0, 0
            if idx + 1 < len(s):  
                x = s[idx + 1]
    if x_cnt != 0 or non_x_cnt != 0:
        answer += 1
    return answer


import calendar
def solution(a, b):
    day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    y, m, d = 2016, a, b
    return day[calendar.weekday(y,m,d)]


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def solution(n):
    answer = 0
    for i in range(2, n + 1): 
        if is_prime(i):
            answer += 1
    return answer


def solution(s, skip, index):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    available_chars = [ch for ch in alphabet if ch not in skip]    
    answer = ''
    for char in s:
        new_idx = (available_chars.index(char) + index) % len(available_chars)
        answer += available_chars[new_idx]
    return answer


def solution(k, m, score):
    score.sort(reverse=True)  
    answer = 0
    for i in range(0, len(score) - m + 1, m):
        answer += score[i + m - 1] * m 
    return answer


def solution(topping):
    answer = 0
    left = set()
    right = {}
    for t in topping:
        right[t] = right.get(t, 0) + 1
    for t in topping:
        left.add(t)  
        right[t] -= 1  
        if right[t] == 0:
            del right[t]  
        if len(left) == len(right):
            answer += 1
    return answer


def solution(elements):
    ans = set()
    i = len(elements)
    for length in range(1, i + 1): 
        for start in range(i): 
            end = (start + length) % i
            if start < end:
                ans.add(sum(elements[start:end])) 
            else:
                ans.add(sum(elements[start:] + elements[:end]))
    return len(ans)


def solution(order):
    answer = 0
    stack = []  
    current = 1  
    for target in order:
        while current <= target:
            stack.append(current)
            current += 1
        if stack and stack[-1] == target:
            stack.pop()
            answer += 1
        else:
            break  
    return answer


def solution(arr1, arr2):
    m = len(arr1)  
    n = len(arr1[0]) 
    p = len(arr2[0]) 
    answer = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n): 
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer


def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        found = False
        for j in range(i+1, len(numbers)):
            if numbers[i] < numbers[j]:
                answer.append(numbers[j])
                found = True
                break
        if not found:
            answer.append(-1)
    return answer

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            index = stack.pop()
            answer[index] = numbers[i]
        stack.append(i)
    return answer


def solution(park, routes):
    road = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}
    h, w = len(park), len(park[0])
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                start = (i, j)
    for route in routes:
        direction, steps = route.split()
        steps = int(steps)
        dx, dy = road[direction]
        nx, ny = start
        valid = True
        for _ in range(steps):
            nx, ny = nx + dx, ny + dy
            if not (0 <= nx < h and 0 <= ny < w) or park[nx][ny] == 'X':
                valid = False
                break
        if valid:
            start = (nx, ny)
    return list(start)


def solution(X, Y):
    count_x = [0] * 10 
    count_y = [0] * 10 
    for digit in X:
        count_x[int(digit)] += 1
    for digit in Y:
        count_y[int(digit)] += 1
    common_digits = []
    for i in range(9, -1, -1):
        common_count = min(count_x[i], count_y[i]) 
        if common_count > 0:
            common_digits.append(str(i) * common_count)  
    if not common_digits:
        return '-1'
    result = ''.join(common_digits)
    if result[0] == '0':
        return '0'    
    return result


def solution(ingredient):
    answer = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        while len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            del stack[-4:]  
            answer += 1  
    return answer


def solution(wallpaper):
    x, y = [], []
    for row_num, row in enumerate(wallpaper):
        if '#' in row:
            x.extend([row.index('#'), row.rindex('#') + 1])
            y.extend([row_num, row_num + 1])
    return [min(y), min(x), max(y), max(x)]


def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        count = 0
        for j in range(1, i+1):
            if i%j == 0:
                count += 1
        if count > limit:
            count = power
        answer += count
    return answer


def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1): 
        if n % i == 0:
            count += 2 if i * i != n else 1 
    return count
def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        count = count_divisors(i)
        if count > limit:
            count = power
        answer += count
    return answer


def solution(x, n):
    return [x * i for i in range(1, n + 1)]


def solution(keymap, targets):
    answer = []
    key_positions = {}
    for i, key in enumerate(keymap):
        for j, char in enumerate(key):
            if char not in key_positions:
                key_positions[char] = j + 1
            else:
                key_positions[char] = min(key_positions[char], j + 1)
    for target in targets:
        total_count = 0
        for char in target:
            if char in key_positions:
                total_count += key_positions[char] 
            else:
                total_count = -1
                break
        answer.append(total_count)
    return answer


from collections import deque
def solution(x, y, n):
    queue = deque()
    queue.append((x, 0))
    visited = set()
    visited.add(x)
    while queue:
        current, count = queue.popleft()
        if current == y:
            return count
        for next_value in (current + n, current * 2, current * 3):
            if next_value <= y and next_value not in visited:
                visited.add(next_value)
                queue.append((next_value, count + 1))
    return -1


import heapq
def solution(n, works):
    if sum(works) <= n:
        return 0  
    works = [-w for w in works]
    heapq.heapify(works)
    
    for _ in range(n):
        max_work = heapq.heappop(works)
        if max_work == 0:
            break
        heapq.heappush(works, max_work + 1)  
    return sum(w ** 2 for w in works)  


def solution(storey):
    answer = 0
    while storey > 0:
        digit = storey % 10
        if digit > 5:
            answer += (10 - digit)
            storey = storey // 10 + 1
        elif digit < 5:
            answer += digit
            storey = storey // 10
        else: 
            next_digit = (storey // 10) % 10
            if next_digit >= 5:
                answer += 5
                storey = storey // 10 + 1
            else:
                answer += 5
                storey = storey // 10
    return answer


def solution(n):
    answer = ''
    while n > 0:
        n, remainder = divmod(n, 3)
        if remainder == 0:
            remainder = 4
            n -= 1
        answer = str(remainder) + answer
    return answer


from collections import deque
def solution(board):
    n, m = len(board), len(board[0])
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i, j)
            if board[i][j] == 'G':
                goal = (i, j)
    queue = deque()
    queue.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        x, y, cnt = queue.popleft()
        if (x, y) == goal:
            return cnt
        for dx, dy in directions:
            nx, ny = x, y
            while True:
                tx, ty = nx + dx, ny + dy
                if 0 <= tx < n and 0 <= ty < m and board[tx][ty] != 'D':
                    nx, ny = tx, ty
                else:
                    break
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt + 1))
    return -1


import math
def solution(n, k):
    numbers = list(range(1, n + 1))
    answer = []
    k -= 1
    for i in range(n, 0, -1):
        fact = math.factorial(i - 1)
        index = k // fact
        answer.append(numbers[index])  
        numbers.pop(index)            
        k %= fact
    return answer


import heapq
def solution(book_time):
    times = []
    for start, end in book_time:
        s_h, s_m = map(int, start.split(':'))
        e_h, e_m = map(int, end.split(':'))
        s = s_h * 60 + s_m
        e = e_h * 60 + e_m + 10
        times.append((s, e))
    times.sort()
    rooms = []
    for s, e in times:
        if rooms and rooms[0] <= s:
            heapq.heappop(rooms)
        heapq.heappush(rooms, e)
    return len(rooms)


import heapq
def solution(n, k, enemy):
    heap = []
    total_soldiers_used = 0
    for round_number, e in enumerate(enemy):
        heapq.heappush(heap, -e)  
        total_soldiers_used += e
        if total_soldiers_used > n:
            if k > 0:
                max_enemy = -heapq.heappop(heap)
                total_soldiers_used -= max_enemy 
                k -= 1
            else:
                return round_number  
    return len(enemy) 


def solution(n):
    result = []
    def hanoi(n, start, mid, end):
        if n == 1:
            result.append([start, end])
            return
        hanoi(n - 1, start, end, mid)
        result.append([start, end])
        hanoi(n - 1, mid, start, end)
    hanoi(n, 1, 2, 3)
    return result


def solution(picks, minerals):
    fatigue_table = {
        'diamond': [1, 5, 25],
        'iron': [1, 1, 5],
        'stone': [1, 1, 1]
    }
    tool_limit = sum(picks)
    minerals = minerals[:tool_limit * 5]
    blocks = [minerals[i:i+5] for i in range(0, len(minerals), 5)]
    def calc_stress(block):
        stress = [0, 0, 0]
        for m in block:
            stress[0] += fatigue_table[m][0]
            stress[1] += fatigue_table[m][1]
            stress[2] += fatigue_table[m][2]
        return stress
    stress_blocks = [calc_stress(block) for block in blocks]
    stress_blocks.sort(key=lambda x: (-x[2], -x[1], -x[0]))  # stone 피로도 기준 정렬
    answer = 0
    idx = 0
    for i in range(3):
        for _ in range(picks[i]):
            if idx >= len(stress_blocks):
                break
            answer += stress_blocks[idx][i]
            idx += 1
    return answer


from math import gcd
from functools import reduce
def get_valid_gcd(arr1, arr2):
    g = reduce(gcd, arr1)
    for num in arr2:
        if num % g == 0:
            return 0
    return g
def solution(arrayA, arrayB):
    return max(get_valid_gcd(arrayA, arrayB), get_valid_gcd(arrayB, arrayA))


def solution(sequence, k):
    left = 0
    right = 0
    total = sequence[0]
    min_len = float('inf')
    answer = [0, 0]
    while right < len(sequence):
        if total < k:
            right += 1
            if right < len(sequence):
                total += sequence[right]
        elif total > k:
            total -= sequence[left]
            left += 1
        else:
            if right - left < min_len:
                min_len = right - left
                answer = [left, right]
            total -= sequence[left]
            left += 1
    return answer


def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    xor_result = 0
    for i in range(row_begin - 1, row_end):
        s_i = sum(value % (i + 1) for value in data[i])
        xor_result ^= s_i
    return xor_result


def solution(maps):
    from collections import deque
    n, m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]
    answer = []
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        visited[x][y] = True
        total = int(maps[x][y])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        while queue:
            cx, cy = queue.popleft()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    total += int(maps[nx][ny])
                    queue.append((nx, ny))
        return total
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != 'X':
                answer.append(bfs(i, j))
    return sorted(answer) if answer else [-1]


def solution(k, ranges):
    seq = [k]
    while k != 1:
        k = k // 2 if k % 2 == 0 else k * 3 + 1
        seq.append(k)
    areas = []
    for i in range(len(seq) - 1):
        areas.append((seq[i] + seq[i + 1]) / 2)
    n = len(areas)
    result = []
    for a, b in ranges:
        end = n + b
        if a > end:
            result.append(-1.0)
        else:
            result.append(sum(areas[a:end]))
    return result


from collections import Counter
def solution(want, number, discount):
    want_dict = dict(zip(want, number))
    answer = 0
    for i in range(len(discount) - 9):
        window = discount[i:i+10]
        if Counter(window) == want_dict:
            answer += 1
    return answer


def solution(n):
    answer = 0
    board = [] 
    def is_ok(row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):  
                return False
        return True
    def backtrack(row):
        nonlocal answer
        if row == n: 
            answer += 1
            return
        for col in range(n):
            if is_ok(row, col):
                board.append(col)
                backtrack(row + 1)
                board.pop()
    backtrack(0)
    return answer


def solution(k, d):
    answer = 0
    for x in range(0, d + 1, k):
        max_y = int((d**2 - x**2)**0.5)
        answer += (max_y // k) + 1
    return answer


def solution(plans):
    def to_minutes(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m
    plans = [(n, to_minutes(s), int(p)) for n, s, p in plans]
    plans.sort(key=lambda x: x[1])
    answer = []
    stack = []
    for i in range(len(plans)):
        name, start, playtime = plans[i]
        if i < len(plans) - 1:
            next_start = plans[i + 1][1]
        else:
            next_start = float('inf')
        stack.append([name, playtime])
        available = next_start - start
        while available > 0 and stack:
            cur, remain = stack.pop()
            if remain <= available:
                available -= remain
                answer.append(cur)
            else:
                stack.append([cur, remain - available])
                available = 0
    while stack:
        answer.append(stack.pop()[0])
    return answer


def solution(board):
    n, m = len(board), len(board[0])
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
    return max(map(max, board)) ** 2


def solution(targets):
    targets.sort(key=lambda x: x[1])
    answer = 0
    last = -1
    for s, e in targets:
        if last <= s:
            answer += 1
            last = e
    return answer


def solution(cards):
    n = len(cards)
    visited = [False] * n
    groups = []
    for i in range(n):
        if not visited[i]:
            cnt = 0
            cur = i
            while not visited[cur]:
                visited[cur] = True
                cur = cards[cur] - 1
                cnt += 1
            groups.append(cnt)
    groups.sort(reverse=True)
    if len(groups) < 2:
        return 0
    return groups[0] * groups[1]


def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        if i == 1:
            answer.append(0)
            continue
        block = 1
        for d in range(2, int(i ** 0.5) + 1):
            if i % d == 0:
                if i // d <= 10_000_000:
                    block = max(block, i // d)
                else:
                    block = max(block, d)
        answer.append(block)
    return answer


def solution(scores):
    arr = [(a, b, i == 0) for i, (a, b) in enumerate(scores)]
    arr.sort(key=lambda x: (-x[0], x[1]))
    max_b = -1
    sums = []
    wanho_sum = scores[0][0] + scores[0][1]
    for a, b, is_wanho in arr:
        if b < max_b:
            if is_wanho:
                return -1
            continue
        max_b = max(max_b, b)
        sums.append(a + b)
    sums.sort(reverse=True)
    prev = None
    rank = 0
    for i, s in enumerate(sums):
        if i == 0:
            rank = 1
        else:
            if s < prev:
                rank = i + 1
        if s == wanho_sum:
            return rank
        prev = s
    return -1


def solution(board):
    O_count = sum(row.count("O") for row in board)
    X_count = sum(row.count("X") for row in board)
    def win(player):
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):
                return True
            if all(board[j][i] == player for j in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2-i] == player for i in range(3)):
            return True
        return False
    O_win = win("O")
    X_win = win("X")
    if X_count > O_count or O_count > X_count + 1:
        return 0
    if O_win and O_count != X_count + 1:
        return 0
    if X_win and O_count != X_count:
        return 0
    if O_win and X_win:
        return 0
    return 1


def solution(r1, r2):
    answer = 0
    for x in range(-r2, r2 + 1):
        for y in range(-r2, r2 + 1):
            dist2 = x*x + y*y
            if r1*r1 <= dist2 <= r2*r2:
                answer += 1
    return answer


def solution(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    max_len = 0
    for i in range(len(s)):
        len1 = expand(i, i)
        len2 = expand(i, i + 1)
        max_len = max(max_len, len1, len2)
    return max_len


def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
    return dp[n]


def solution(n):
    MOD = 1_000_000_007
    if n % 2 == 1:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1
    if n >= 2:
        dp[2] = 3
    for i in range(4, n + 1, 2):
        dp[i] = (4 * dp[i-2] - dp[i-4]) % MOD
    return dp[n] % MOD


def solution(matrix_sizes):
    n = len(matrix_sizes)
    p = [matrix_sizes[0][0]] + [m[1] for m in matrix_sizes]
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):  
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n - 1]


import sys
sys.setrecursionlimit(200000)
def solution(n, lighthouse):
    graph = [[] for _ in range(n + 1)]
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)
    dp = [[0, 0] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    def dfs(node):
        visited[node] = True
        dp[node][0] = 0    
        dp[node][1] = 1     
        for nxt in graph[node]:
            if not visited[nxt]:
                dfs(nxt)
                dp[node][0] += dp[nxt][1]
                dp[node][1] += min(dp[nxt][0], dp[nxt][1])
    dfs(1)
    return min(dp[1][0], dp[1][1])


def solution(beginning, target):
    from copy import deepcopy
    n, m = len(beginning), len(beginning[0])
    min_count = float('inf')
    for mask in range(1 << n):  
        board = deepcopy(beginning)
        row_flip_count = 0
        for i in range(n):
            if mask & (1 << i):
                row_flip_count += 1
                for j in range(m):
                    board[i][j] ^= 1  
        col_flip_count = 0
        for j in range(m):
            if any(board[i][j] != target[i][j] for i in range(n)):
                col_flip_count += 1
                for i in range(n):
                    board[i][j] ^= 1
        if board == target:
            min_count = min(min_count, row_flip_count + col_flip_count)
    return min_count if min_count != float('inf') else -1


def solution(n, l, r):
    def count_ones(level, left, right):
        if level == 0:
            return 1
        unit = pow(5, level - 1)
        def get_block(idx):
            return (idx - 1) // unit + 1
        start_block = get_block(left)
        end_block = get_block(right)
        total = 0
        for block in range(start_block, end_block + 1):
            block_l = (block - 1) * unit + 1
            block_r = block * unit
            seg_l = max(left, block_l)
            seg_r = min(right, block_r)
            if block == 3:
                continue
            total += count_ones(level - 1, seg_l - block_l + 1, seg_r - block_l + 1)
        return total
    return count_ones(n, l, r)


def solution(target):
    INF = 10**9
    options = []
    for n in range(1, 21):
        options.append((n, False))
        options.append((2*n, False))
        options.append((3*n, False))
    options.append((50, True))
    options = [(v, True) if (1 <= v <= 20 and v in {n for n in range(1,21)}) else (v, is_single) for v, is_single in options]
    options = []
    for n in range(1,21):
        options.append((n, True))
        options.append((2*n, False))
        options.append((3*n, False))
    options.append((50, True))
    dp_darts = [INF] * (target + 1)
    dp_singles = [-1] * (target + 1)
    dp_darts[0] = 0
    dp_singles[0] = 0
    for i in range(1, target + 1):
        best_d = INF
        best_s = -1
        for score, is_single in options:
            if score <= i:
                prev = dp_darts[i - score]
                if prev != INF:
                    cand_d = prev + 1
                    cand_s = dp_singles[i - score] + (1 if is_single else 0)
                    if cand_d < best_d or (cand_d == best_d and cand_s > best_s):
                        best_d = cand_d
                        best_s = cand_s
        dp_darts[i] = best_d
        dp_singles[i] = best_s
    return [dp_darts[target], dp_singles[target]]


def solution(numbers):
    pos = {'1': (0,0),'2': (0,1),'3': (0,2), '4': (1,0),'5': (1,1),'6': (1,2), '7': (2,0),'8': (2,1),'9': (2,2), '0': (3,1)}
    dirs = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    from collections import deque
    cost = [[0]*10 for _ in range(10)]
    def bfs(start):
        dist = [[10**9]*3 for _ in range(4)]
        sx, sy = pos[str(start)]
        q = deque([(sx, sy)])
        dist[sx][sy] = 0
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < 4 and 0 <= ny < 3:
                    if (nx,ny) not in pos.values():
                        continue
                    w = 1 if (nx,ny)==(x,y) else (2 if abs(dx)+abs(dy)==1 else 3)
                    if dist[nx][ny] > dist[x][y] + w:
                        dist[nx][ny] = dist[x][y] + w
                        q.append((nx,ny))
        return dist
    for i in range(10):
        d = bfs(i)
        for j in range(10):
            x,y = pos[str(j)]
            cost[i][j] = d[x][y]
    dp = {}
    dp[(4,6)] = 0
    for ch in numbers:
        nxt = int(ch)
        new = {}
        for (l, r), c in dp.items():
            if l == nxt:
                v = (l, r)
                nc = c + 1
                if v not in new or new[v] > nc:
                    new[v] = nc
            elif r == nxt:
                v = (l, r)
                nc = c + 1
                if v not in new or new[v] > nc:
                    new[v] = nc
            else:
                nc = c + cost[l][nxt]
                v = (nxt, r)
                if v not in new or new[v] > nc:
                    new[v] = nc
                nc = c + cost[r][nxt]
                v = (l, nxt)
                if v not in new or new[v] > nc:
                    new[v] = nc
        dp = new
    return min(dp.values())


from itertools import permutations
def solution(n, submit):
    digits = '123456789'
    candidates = [''.join(p) for p in permutations(digits, 4)]
    for _ in range(n):
        guess = candidates[0]
        res = submit(int(guess))
        s, b = map(int, res.replace('S', '').replace('B', '').split())
        if s == 4:
            return int(guess)
        new_list = []
        for cand in candidates:
            ts = tb = 0
            for i in range(4):
                if cand[i] == guess[i]:
                    ts += 1
                elif cand[i] in guess:
                    tb += 1
            if ts == s and tb == b:
                new_list.append(cand)
        candidates = new_list
    return int(candidates[0])


def solution(e, starts):
    d = [0] * (e + 1)
    for i in range(1, e + 1):
        for j in range(i, e + 1, i):
            d[j] += 1
    best = [0] * (e + 1)
    best[e] = e
    for i in range(e - 1, 0, -1):
        if d[i] >= d[best[i + 1]]:
            best[i] = i
        else:
            best[i] = best[i + 1]
    return [best[s] for s in starts]


def solution(m, n, startX, startY, balls):
    answer = []
    for tx, ty in balls:
        res = []
        if not (tx == startX and ty < startY):
            dx = tx
            dy = -ty
            val = (startX - dx) ** 2 + (startY - dy) ** 2
            res.append(val)
        if not (tx == startX and ty > startY):
            dx = tx
            dy = 2 * n - ty
            val = (startX - dx) ** 2 + (startY - dy) ** 2
            res.append(val)
        if not (ty == startY and tx < startX):
            dx = -tx
            dy = ty
            val = (startX - dx) ** 2 + (startY - dy) ** 2
            res.append(val)
        if not (ty == startY and tx > startX):
            dx = 2 * m - tx
            dy = ty
            val = (startX - dx) ** 2 + (startY - dy) ** 2
            res.append(val)
        answer.append(min(res))
    return answer


def solution(n):
    mod = 1234567
    if n == 1:
        return 1
    if n == 2:
        return 2
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, (a + b) % mod
    return b


def solution(n, cores):
    if n <= len(cores):
        return n
    left, right = 1, max(cores) * n
    while left < right:
        mid = (left + right) // 2
        done = len(cores)
        for c in cores:
            done += mid // c
        if done >= n:
            right = mid
        else:
            left = mid + 1
    time = left
    done = len(cores)
    for c in cores:
        done += (time - 1) // c
    for i, c in enumerate(cores):
        if time % c == 0:
            done += 1
            if done == n:
                return i + 1


def solution(clockHands):
    n = len(clockHands)
    dx = [0, 0, 0, 1, -1]
    dy = [0, 1, -1, 0, 0]
    def rotate(board, x, y, cnt):
        for d in range(5):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] = (board[nx][ny] + cnt) % 4
    INF = 10**9
    answer = INF
    from itertools import product
    for first in product(range(4), repeat=n):
        board = [row[:] for row in clockHands]
        cnt = 0
        for j in range(n):
            if first[j]:
                rotate(board, 0, j, first[j])
                cnt += first[j]
        for i in range(1, n):
            for j in range(n):
                need = (4 - board[i-1][j]) % 4
                if need:
                    rotate(board, i, j, need)
                    cnt += need
        if all(board[n-1][j] == 0 for j in range(n)):
            answer = min(answer, cnt)
    return answer


def solution(n):
    MOD = 1000000007
    if n == 0:
        return 1
    dp = [0] * (max(n + 1, 7))
    dp[0] = 1
    dp[1] = 1
    dp[2] = 3
    dp[3] = 10
    dp[4] = 23
    dp[5] = 62
    dp[6] = 170
    for i in range(7, n + 1):
        dp[i] = (dp[i - 1] + 2 * dp[i - 2] + 6 * dp[i - 3] + dp[i - 4] - dp[i - 6]) % MOD
    return dp[n] % MOD
