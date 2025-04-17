def date_to_days(date_str):
    year, month, day = map(int, date_str.split('.'))
    return year * 12 * 28 + month * 28 + day
def solution(today, terms, privacies):
    term_dict = {}
    for term in terms:
        term_type, duration = term.split()
        term_dict[term_type] = int(duration)
    today_in_days = date_to_days(today)
    expired_indices = []
    for i, privacy in enumerate(privacies):
        privacy_date, privacy_type = privacy.split()
        expiration_date_in_days = date_to_days(privacy_date) + term_dict[privacy_type] * 28 - 1
        if expiration_date_in_days < today_in_days:
            expired_indices.append(i + 1)
    return expired_indices


from collections import deque
def solution(n, m, x, y, r, c, k):
    directions = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]
    distance_to_target = abs(x - r) + abs(y - c)
    if distance_to_target > k or (k - distance_to_target) % 2 != 0:
        return "impossible"
    queue = deque([(x, y, "", k)])
    visited = set()
    while queue:
        x, y, path, remaining_moves = queue.popleft()
        if remaining_moves == 0:
            if (x, y) == (r, c):
                return path
        for direction, dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= n and 1 <= ny <= m and (nx, ny, remaining_moves - 1) not in visited:
                visited.add((nx, ny, remaining_moves - 1))
                queue.append((nx, ny, path + direction, remaining_moves - 1))
    return "impossible"


def solution(alp, cop, problems):
    max_alp = max(p[0] for p in problems)
    max_cop = max(p[1] for p in problems)
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    dp = [[float('inf')] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j + 1 <= max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    new_alp = min(max_alp, i + alp_rwd)
                    new_cop = min(max_cop, j + cop_rwd)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)
    return dp[max_alp][max_cop]


from collections import deque
def solution(queue1, queue2):
    total_sum = sum(queue1) + sum(queue2)
    if total_sum % 2 != 0:
        return -1
    target_sum = total_sum // 2
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    n = len(queue1)
    max_operations = n * 3
    operations = 0 
    i, j = 0, 0
    while i < max_operations and j < max_operations:
        if sum1 == target_sum:
            return operations
        elif sum1 > target_sum:
            val = q1.popleft()
            q2.append(val)
            sum1 -= val
            sum2 += val
            i += 1
        else:
            val = q2.popleft()
            q1.append(val)
            sum1 += val
            sum2 -= val
            j += 1
        operations += 1
    return -1


def solution(survey, choices):
    scores = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0
    }
    for i in range(len(survey)):
        left, right = survey[i][0], survey[i][1]
        choice = choices[i]
        if choice < 4:
            scores[left] += 4 - choice
        elif choice > 4:
            scores[right] += choice - 4
    result = ''
    result += 'R' if scores['R'] >= scores['T'] else 'T'
    result += 'C' if scores['C'] >= scores['F'] else 'F'
    result += 'J' if scores['J'] >= scores['M'] else 'M'
    result += 'A' if scores['A'] >= scores['N'] else 'N'
    return result


def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for parent, child in edges:
        graph[parent].append(child)
    def dfs(node, sheep, wolf, visitable):
        nonlocal max_sheep
        if info[node] == 0:
            sheep += 1
        else:
            wolf += 1
        if wolf >= sheep:
            return
        max_sheep = max(max_sheep, sheep)
        for next_node in visitable:
            next_visitable = visitable.copy()
            next_visitable.remove(next_node)
            next_visitable.extend(graph[next_node])
            dfs(next_node, sheep, wolf, next_visitable)
    max_sheep = 0
    dfs(0, 0, 0, graph[0])
    return max_sheep


def solution(n, info):
    max_diff = -1
    best_shot = [-1]
    def calculate_score(ryan, apeach):
        ryan_score = 0
        apeach_score = 0
        for i in range(11):
            if ryan[i] > apeach[i]:
                ryan_score += 10 - i
            elif apeach[i] > 0:
                apeach_score += 10 - i
        return ryan_score, apeach_score
    def backtrack(index, arrows_left, ryan_shot):
        nonlocal max_diff, best_shot
        if index == 11:
            if arrows_left > 0:
                ryan_shot[10] += arrows_left  
            ryan_score, apeach_score = calculate_score(ryan_shot, info)
            diff = ryan_score - apeach_score
            if diff > 0 and diff > max_diff:
                max_diff = diff
                best_shot = ryan_shot[:]
            elif diff > 0 and diff == max_diff:
                for i in range(10, -1, -1):
                    if ryan_shot[i] > best_shot[i]:
                        best_shot = ryan_shot[:]
                        break
                    elif ryan_shot[i] < best_shot[i]:
                        break
            if arrows_left > 0:
                ryan_shot[10] -= arrows_left  
            return
        if arrows_left > info[index]:
            ryan_shot[index] = info[index] + 1
            backtrack(index + 1, arrows_left - ryan_shot[index], ryan_shot)
            ryan_shot[index] = 0 
        backtrack(index + 1, arrows_left, ryan_shot)
    backtrack(0, n, [0] * 11)
    return best_shot


import math
def time_to_minutes(time):
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes
def calculate_fee(time, fees):
    basic_time, basic_fee, unit_time, unit_fee = fees
    if time <= basic_time:
        return basic_fee
    else:
        extra_time = time - basic_time
        return basic_fee + math.ceil(extra_time / unit_time) * unit_fee
def solution(fees, records):
    in_times = {}
    total_times = {}
    for record in records:
        time, car_number, status = record.split()
        car_number = int(car_number)
        if status == "IN":
            in_times[car_number] = time_to_minutes(time)
        else: 
            in_time = in_times.pop(car_number)
            parked_time = time_to_minutes(time) - in_time
            if car_number in total_times:
                total_times[car_number] += parked_time
            else:
                total_times[car_number] = parked_time
    end_of_day = time_to_minutes("23:59")
    for car_number, in_time in in_times.items():
        parked_time = end_of_day - in_time
        if car_number in total_times:
            total_times[car_number] += parked_time
        else:
            total_times[car_number] = parked_time
    result = []
    for car_number in sorted(total_times.keys()):
        total_time = total_times[car_number]
        fee = calculate_fee(total_time, fees)
        result.append(fee)
    return result


def solution(id_list, report, k):
    report_dict = {user: set() for user in id_list}
    for r in report:
        user, reported_user = r.split()
        report_dict[reported_user].add(user)
    suspended_users = [user for user, reporters in report_dict.items() if len(reporters) >= k]
    result = [0] * len(id_list)
    for i, user in enumerate(id_list):
        for suspended_user in suspended_users:
            if user in report_dict[suspended_user]:
                result[i] += 1
    return result


def solution(s):
    num_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    for word, num in num_dict.items():
        s = s.replace(word, num)
    return int(s)


def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    sets = [set(map(int, x.split(','))) for x in s]
    sets.sort(key=len)
    seen = set()
    for subset in sets:
        for num in subset:
            if num not in seen:
                answer.append(num)
                seen.add(num)
                break
    return answer


def solution(N, stages):
    counts = [0] * (N + 2)
    for stage in stages:
        counts[stage] += 1
    failure_rates = []  
    total_players = len(stages) 
    for i in range(1, N + 1):
        if total_players == 0: 
            failure_rates.append((0, i))
        else:
            failure_rates.append((counts[i] / total_players, i))  
            total_players -= counts[i]
    failure_rates.sort(key=lambda x: (-x[0], x[1]))
    return [stage for _, stage in failure_rates]


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def solution(n, k):
    answer = 0
    k_base = ""
    while n > 0:
        k_base = str(n % k) + k_base
        n //= k
    for num in k_base.split('0'):
        if num and is_prime(int(num)): 
            answer += 1
    return answer


from collections import Counter
def make_bigrams(s):
    bigrams = []
    s = s.lower()
    for i in range(len(s) - 1):
        pair = s[i:i+2]
        if pair.isalpha(): 
            bigrams.append(pair)
    return Counter(bigrams)
def solution(str1, str2):
    st1 = make_bigrams(str1)
    st2 = make_bigrams(str2)
    intersection = sum((st1 & st2).values()) 
    union = sum((st1 | st2).values())
    if union == 0:
        return 65536 
    return int((intersection / union) * 65536)


def solution(msg):
    dictionary = {chr(i): i - 64 for i in range(65, 91)}
    next_index = 27
    answer = []
    i = 0
    while i < len(msg):
        w = msg[i]
        while i + 1 < len(msg) and w + msg[i + 1] in dictionary:
            i += 1
            w += msg[i] 
        answer.append(dictionary[w])  
        if i + 1 < len(msg):
            dictionary[w + msg[i + 1]] = next_index
            next_index += 1
        i += 1  
    return answer

def solution(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {k: v for (k, v) in zip(alphabet, list(range(1, 27)))} 
    answer = []
    while True:
        if msg in d: 
            answer.append(d[msg])
            break
        for i in range(1, len(msg) + 1): 
            if msg[0:i] not in d: 
                answer.append(d[msg[0:i - 1]])  
                d[msg[0:i]] = len(d) + 1 
                msg = msg[i - 1:] 
                break
    return answer


from itertools import permutations
def match(user, ban):
    return len(user) == len(ban) and all(b == '*' or u == b for u, b in zip(user, ban))
def solution(user_id, banned_id):
    possible_bans = [[user for user in user_id if match(user, ban)] for ban in banned_id]
    unique_cases = set()
    for case in permutations(user_id, len(banned_id)):
        if all(case[i] in possible_bans[i] for i in range(len(banned_id))):
            unique_cases.add(frozenset(case)) 
    return len(unique_cases)


import re
def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)
    new_id = re.sub(r'\.{2,}', '.', new_id)
    new_id = new_id.strip('.')
    if not new_id:
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15].rstrip('.')
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id


def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        move -= 1  
        for row in board:
            if row[move] != 0:
                item = row[move] 
                row[move] = 0 
                if stack and stack[-1] == item:
                    stack.pop()
                    answer += 2 
                else:
                    stack.append(item) 
                break
    return answer


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        bin1 = bin(arr1[i])[2:].zfill(n)  
        bin2 = bin(arr2[i])[2:].zfill(n) 
        row = ""
        for j in range(n):
            if int(bin1[j]) | int(bin2[j]): 
                row += '#'
            else:
                row += ' '
        answer.append(row)
    return answer


def solution(numbers, hand):
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        0: (3, 1)
    }
    left_pos = (3, 0)
    right_pos = (3, 2)
    answer = ''
    for num in numbers:
        target_pos = keypad[num]
        left_dist = abs(left_pos[0] - target_pos[0]) + abs(left_pos[1] - target_pos[1])
        right_dist = abs(right_pos[0] - target_pos[0]) + abs(right_pos[1] - target_pos[1])
        if num in [1, 4, 7]:
            answer += 'L'
            left_pos = target_pos
        elif num in [3, 6, 9]:
            answer += 'R'
            right_pos = target_pos
        else:
            if left_dist < right_dist:
                answer += 'L'
                left_pos = target_pos
            elif right_dist < left_dist:
                answer += 'R'
                right_pos = target_pos
            else:
                if hand == "left":
                    answer += 'L'
                    left_pos = target_pos
                else:
                    answer += 'R'
                    right_pos = target_pos
    return answer


def solution(friends, gifts):
    friends = sorted(friends)
    addr = {friend: i for i, friend in enumerate(friends)}
    arr = [[0] * len(friends) for _ in range(len(friends))]
    for gift in gifts:
        giver, receiver = gift.split(' ')
        arr[addr[giver]][addr[receiver]] += 1
    ab = [sum(arr[i]) - sum(arr[j][i] for j in range(len(friends))) for i in range(len(friends))]
    pre_nm = [0] * len(friends)
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            if arr[i][j] > arr[j][i]:
                pre_nm[i] += 1
            elif arr[j][i] > arr[i][j]:
                pre_nm[j] += 1
            else:
                if ab[i] > ab[j]:
                    pre_nm[i] += 1
                elif ab[i] < ab[j]:
                    pre_nm[j] += 1
    return max(pre_nm)


import re
def solution(dartResult):
    dart = re.findall(r'(\d{1,2})([SDT])([*#]?)', dartResult)
    scores = []
    for i, (num, bonus, option) in enumerate(dart):
        num = int(num)
        if bonus == 'S':
            num = num ** 1
        elif bonus == 'D':
            num = num ** 2
        elif bonus == 'T':
            num = num ** 3
        if option == '*':
            num *= 2
            if i > 0:
                scores[i - 1] *= 2
        elif option == '#':
            num *= -1
        scores.append(num)
    return sum(scores)

