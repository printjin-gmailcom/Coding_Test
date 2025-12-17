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

def solution(record):
    answer = []
    user_nick = {}
    actions = []
    for entry in record:
        parts = entry.split()
        action = parts[0]
        uid = parts[1]
        if action in ("Enter", "Change"):
            nickname = parts[2]
            user_nick[uid] = nickname
        if action in ("Enter", "Leave"):
            actions.append((action, uid))
    for action, uid in actions:
        nickname = user_nick[uid]
        if action == "Enter":
            answer.append(f"{nickname}님이 들어왔습니다.")
        elif action == "Leave":
            answer.append(f"{nickname}님이 나갔습니다.")
    return answer


from itertools import combinations
from collections import Counter
def solution(orders, course):
    result = []
    for c in course:
        combs = []
        for order in orders:
            order = sorted(order)
            combs += combinations(order, c)
        combs_counter = Counter(combs)
        if combs_counter:
            max_count = max(combs_counter.values())
            if max_count >= 2:
                for comb in combs_counter:
                    if combs_counter[comb] == max_count:
                        result.append(''.join(comb))
    return sorted(result)


def solution(m, musicinfos):
    def time_to_minutes(time_str):
        hour, minute = map(int, time_str.split(':'))
        return hour * 60 + minute
    def convert_melody(melody):
        converted = ''
        i = 0
        while i < len(melody):
            if i + 1 < len(melody) and melody[i + 1] == '#':
                converted += melody[i].lower()
                i += 2
            else:
                converted += melody[i]
                i += 1
        return converted
    answer = '(None)'
    max_play_time = -1
    m_converted = convert_melody(m)
    for info in musicinfos:
        start, end, title, melody = info.split(',')
        play_time = time_to_minutes(end) - time_to_minutes(start)
        melody_converted = convert_melody(melody)
        full_melody = (melody_converted * (play_time // len(melody_converted))) + melody_converted[:play_time % len(melody_converted)]
        if m_converted in full_melody:
            if play_time > max_play_time:
                max_play_time = play_time
                answer = title
    return answer


import re
def solution(files):
    def parse(file):
        head, number = re.match(r'([^\d]+)(\d{1,5})', file).groups()
        return (head.lower(), int(number))
    return sorted(files, key=lambda file: parse(file))


def solution(m, n, board):
    board = [list(row) for row in board]
    total_removed = 0
    while True:
        remove = set()
        for i in range(m - 1):
            for j in range(n - 1):
                block = board[i][j]
                if block == '0':
                    continue
                if block == board[i][j+1] and block == board[i+1][j] and block == board[i+1][j+1]:
                    remove |= {(i, j), (i, j+1), (i+1, j), (i+1, j+1)}
        if not remove:
            break
        total_removed += len(remove)
        for i, j in remove:
            board[i][j] = '0'
        for j in range(n):
            stack = [board[i][j] for i in range(m) if board[i][j] != '0']
            for i in range(m - 1, -1, -1):
                board[i][j] = stack.pop() if stack else '0'
    return total_removed


def solution(s):
    if len(s) == 1:
        return 1
    min_len = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[:step]
        count = 1
        for i in range(step, len(s), step):
            curr = s[i:i+step]
            if curr == prev:
                count += 1
            else:
                compressed += (str(count) + prev) if count > 1 else prev
                prev = curr
                count = 1
        compressed += (str(count) + prev) if count > 1 else prev
        min_len = min(min_len, len(compressed))
    return min_len


from itertools import combinations
def solution(relation):
    n_col = len(relation[0])
    candidates = []
    for i in range(1, n_col + 1):
        for comb in combinations(range(n_col), i):
            tmp = [tuple(item[col] for col in comb) for item in relation]
            if len(set(tmp)) == len(relation):
                is_minimal = True
                for c in candidates:
                    if set(c).issubset(set(comb)):
                        is_minimal = False
                        break
                if is_minimal:
                    candidates.append(comb)
    return len(candidates)


def solution(places):
    def is_valid(place):
        for i in range(5):
            for j in range(5):
                if place[i][j] != 'P':
                    continue
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < 5 and 0 <= nj < 5 and place[ni][nj] == 'P':
                        return 0
                for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]: 
                    ni, nj = i + dx, j + dy
                    mi, mj = i + dx // 2, j + dy // 2
                    if 0 <= ni < 5 and 0 <= nj < 5 and place[ni][nj] == 'P':
                        if place[mi][mj] != 'X':
                            return 0
                for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]: 
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < 5 and 0 <= nj < 5 and place[ni][nj] == 'P':
                        if place[i][nj] != 'X' or place[ni][j] != 'X':
                            return 0
        return 1
    return [is_valid(place) for place in places]


from itertools import permutations
def solution(expression):
    tokens = []
    num = ''
    for ch in expression:
        if ch in '+-*':
            tokens.append(int(num))
            tokens.append(ch)
            num = ''
        else:
            num += ch
    tokens.append(int(num))
    operators = set([t for t in tokens if isinstance(t, str)])
    max_val = 0
    for order in permutations(operators):
        temp = tokens[:]
        for op in order:
            stack = []
            i = 0
            while i < len(temp):
                if temp[i] == op:
                    prev = stack.pop()
                    next_num = temp[i + 1]
                    if op == '+':
                        stack.append(prev + next_num)
                    elif op == '-':
                        stack.append(prev - next_num)
                    else:
                        stack.append(prev * next_num)
                    i += 2
                else:
                    stack.append(temp[i])
                    i += 1
            temp = stack
        max_val = max(max_val, abs(temp[0]))
    return max_val


def solution(gems):
    total_types = len(set(gems))
    gem_counter = {}
    answer = [0, len(gems) - 1]
    start, end = 0, 0
    gem_counter[gems[0]] = 1
    while start < len(gems) and end < len(gems):
        if len(gem_counter) == total_types:
            if (end - start) < (answer[1] - answer[0]):
                answer = [start, end]
            gem_counter[gems[start]] -= 1
            if gem_counter[gems[start]] == 0:
                del gem_counter[gems[start]]
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            gem_counter[gems[end]] = gem_counter.get(gems[end], 0) + 1
    return [answer[0] + 1, answer[1] + 1]


def solution(stones, k):
    left, right = 1, max(stones)
    answer = 0
    while left <= right:
        mid = (left + right) // 2 
        cnt = 0
        possible = True
        for s in stones:
            if s - mid < 0:
                cnt += 1
                if cnt >= k:
                    possible = False
                    break
            else:
                cnt = 0
        if possible:  
            answer = mid
            left = mid + 1
        else:  
            right = mid - 1
    return answer


def solution(p):
    if not p:
        return ""
    def is_correct(s):
        stack = []
        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                if not stack:
                    return False
                stack.pop()
        return not stack
    def split_uv(w):
        left, right = 0, 0
        for i, ch in enumerate(w):
            if ch == '(':
                left += 1
            else:
                right += 1
            if left == right:
                return w[:i+1], w[i+1:]
    u, v = split_uv(p)
    if is_correct(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + "".join('(' if c == ')' else ')' for c in u[1:-1])


def solution(board):
    from heapq import heappush, heappop
    n = len(board)
    INF = 10**9
    dist = [[[INF]*4 for _ in range(n)] for __ in range(n)]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    heap = []
    for d,(dr,dc) in enumerate(dirs):
        nr, nc = dr, dc
        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
            dist[nr][nc][d] = 100
            heappush(heap, (100, nr, nc, d))
    while heap:
        cost, r, c, dir0 = heappop(heap)
        if cost > dist[r][c][dir0]:
            continue
        if r == n-1 and c == n-1:
            return cost
        for nd,(dr,dc) in enumerate(dirs):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
                nc_cost = cost + (100 if nd == dir0 else 600)
                if nc_cost < dist[nr][nc][nd]:
                    dist[nr][nc][nd] = nc_cost
                    heappush(heap, (nc_cost, nr, nc, nd))
    ans = min(dist[n-1][n-1])
    return ans if ans != INF else 0


from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    cache = deque()
    time = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(city)
            time += 5
    return time


from itertools import product
def solution(users, emoticons):
    answer = [0, 0]
    discounts = [10, 20, 30, 40]
    for rates in product(discounts, repeat=len(emoticons)):
        subs, sales = 0, 0
        for perc, limit in users:
            total = 0
            for rate, price in zip(rates, emoticons):
                if rate >= perc:
                    total += price * (100 - rate) // 100
            if total >= limit:
                subs += 1
            else:
                sales += total
        if subs > answer[0] or (subs == answer[0] and sales > answer[1]):
            answer = [subs, sales]
    return answer


def solution(n, s, a, b, fares):
    INF = 10**9
    dist = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dist[i][i] = 0
    for c, d, f in fares:
        dist[c][d] = f
        dist[d][c] = f
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    answer = INF
    for k in range(1, n+1):
        cost = dist[s][k] + dist[k][a] + dist[k][b]
        if cost < answer:
            answer = cost
    return answer


def solution(n, t, m, timetable):
    crew = sorted([int(x[:2]) * 60 + int(x[3:]) for x in timetable])
    bus_time = 540
    idx = 0 
    for i in range(n):
        cnt = 0  
        while cnt < m and idx < len(crew) and crew[idx] <= bus_time:
            last = crew[idx]
            idx += 1
            cnt += 1
        if i == n - 1:
            if cnt < m: 
                return f"{bus_time // 60:02d}:{bus_time % 60:02d}"
            else: 
                return f"{(last - 1) // 60:02d}:{(last - 1) % 60:02d}"
        bus_time += t


def rotate(matrix):
    return list(zip(*matrix[::-1]))

def check(new_lock):
    n = len(new_lock) // 3
    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
    for rotation in range(4):
        key = rotate(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                if check(new_lock):
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False


def solution(board, skill):
    n, m = len(board), len(board[0])
    diff = [[0] * (m + 1) for _ in range(n + 1)]
    for type_, r1, c1, r2, c2, degree in skill:
        if type_ == 1:
            degree = -degree
        diff[r1][c1] += degree
        diff[r1][c2 + 1] -= degree
        diff[r2 + 1][c1] -= degree
        diff[r2 + 1][c2 + 1] += degree
    for i in range(n):
        for j in range(1, m):
            diff[i][j] += diff[i][j - 1]
    for j in range(m):
        for i in range(1, n):
            diff[i][j] += diff[i - 1][j]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + diff[i][j] > 0:
                cnt += 1
    return cnt


import sys
sys.setrecursionlimit(10000)
def solution(nodeinfo):
    nodes = sorted([(x, y, i+1) for i, (x, y) in enumerate(nodeinfo)], key=lambda x: (-x[1], x[0]))
    root = [*nodes[0], None, None] 
    for n in nodes[1:]:
        node = [*n, None, None]
        cur = root
        while True:
            if node[0] < cur[0]:  
                if cur[3] is None:
                    cur[3] = node
                    break
                else:
                    cur = cur[3]
            else:  
                if cur[4] is None:
                    cur[4] = node
                    break
                else:
                    cur = cur[4]
    preorder, postorder = [], []
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        preorder.append(node[2])
        if node[4]:
            stack.append(node[4])
        if node[3]:
            stack.append(node[3])
    def post(node):
        if node is None: return
        post(node[3])
        post(node[4])
        postorder.append(node[2])
    post(root)
    return [preorder, postorder]


def solution(n, k, cmd):
    prev = [i-1 for i in range(n)]
    next = [i+1 for i in range(n)]
    next[-1] = -1
    removed = []
    for c in cmd:
        if c[0] == 'U':
            x = int(c.split()[1])
            for _ in range(x):
                k = prev[k]
        elif c[0] == 'D':
            x = int(c.split()[1])
            for _ in range(x):
                k = next[k]
        elif c[0] == 'C':
            removed.append((k, prev[k], next[k]))
            if prev[k] != -1:
                next[prev[k]] = next[k]
            if next[k] != -1:
                prev[next[k]] = prev[k]
            k = next[k] if next[k] != -1 else prev[k]
        else: 
            idx, p, q = removed.pop()
            if p != -1:
                next[p] = idx
            if q != -1:
                prev[q] = idx
    ans = ['O'] * n
    for idx, _, _ in removed:
        ans[idx] = 'X'
    return ''.join(ans)


def solution(cap, n, deliveries, pickups):
    answer = 0
    d, p = 0, 0 
    for i in range(n - 1, -1, -1):
        d += deliveries[i]
        p += pickups[i]
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            answer += (i + 1) * 2  
    return answer


import heapq
def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    for a, b, w in paths:
        graph[a].append((b, w))
        graph[b].append((a, w))
    gates, summits = set(gates), set(summits)
    dist = [float('inf')] * (n+1)
    pq = []
    for g in gates:
        dist[g] = 0
        heapq.heappush(pq, (0, g))
    while pq:
        intensity, node = heapq.heappop(pq)
        if node in summits or intensity > dist[node]:
            continue
        for nxt, w in graph[node]:
            if nxt in gates:
                continue
            new_intensity = max(intensity, w)
            if new_intensity < dist[nxt]:
                dist[nxt] = new_intensity
                heapq.heappush(pq, (new_intensity, nxt))
    result = min([(dist[s], s) for s in summits])
    return [result[1], result[0]]


from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    data = {}
    for i in info:
        parts = i.split()
        score = int(parts[-1])
        conditions = parts[:-1]
        for n in range(5):
            for comb in combinations(range(4), n):
                temp = conditions.copy()
                for idx in comb:
                    temp[idx] = '-'
                key = ' '.join(temp)
                if key not in data:
                    data[key] = []
                data[key].append(score)
    for k in data:
        data[k].sort()
    answer = []
    for q in query:
        q = q.replace(' and', '')
        parts = q.split()
        key = ' '.join(parts[:-1])
        score = int(parts[-1])
        if key in data:
            scores = data[key]
            idx = bisect_left(scores, score)
            answer.append(len(scores) - idx)
        else:
            answer.append(0)
    return answer


import heapq
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    sum_value = 0 
    previous = 0  
    length = len(food_times)
    while q:
        time = (q[0][0] - previous) * length
        if sum_value + time > k:
            break
        sum_value += time
        now = heapq.heappop(q)[0]
        length -= 1
        previous = now
    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]


def solution(enroll, referral, seller, amount):
    parent = {}
    profit = {}
    for e, r in zip(enroll, referral):
        parent[e] = r
        profit[e] = 0
    for s, a in zip(seller, amount):
        money = a * 100  
        cur = s
        while cur != "-" and money > 0:
            give = money // 10  
            profit[cur] += money - give  
            cur = parent[cur]
            money = give  
    return [profit[name] for name in enroll]


def solution(n, tops):
    MOD = 10007
    if n == 0:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = (3 + tops[0]) % MOD
    for i in range(2, n + 1):
        dp[i] = (dp[i-1] * (3 + tops[i-1]) - dp[i-2]) % MOD
        if dp[i] < 0:
            dp[i] += MOD
    return dp[n]


def solution(n, build_frame):
    def possible(structure):
        for x, y, a in structure:
            if a == 0:  
                if (
                    y == 0 or
                    [x, y - 1, 0] in structure or
                    [x - 1, y, 1] in structure or
                    [x, y, 1] in structure
                ):
                    continue
                return False
            else:  
                if (
                    [x, y - 1, 0] in structure or
                    [x + 1, y - 1, 0] in structure or
                    ([x - 1, y, 1] in structure and [x + 1, y, 1] in structure)
                ):
                    continue
                return False
        return True
    structure = []
    for x, y, a, b in build_frame:
        if b == 1: 
            structure.append([x, y, a])
            if not possible(structure):
                structure.remove([x, y, a])
        else: 
            structure.remove([x, y, a])
            if not possible(structure):
                structure.append([x, y, a])
    return sorted(structure)


def solution(n, t, m, p):
    digits = "0123456789ABCDEF"
    seq = ""
    num = 0
    while len(seq) < t * m:
        x = num
        if x == 0:
            seq += "0"
        else:
            s = ""
            while x > 0:
                x, r = divmod(x, n)
                s = digits[r] + s
            seq += s
        num += 1
    answer = ""
    for i in range(p - 1, t * m, m):
        answer += seq[i]
        if len(answer) == t:
            break
    return answer
    

def solution(commands):
    parent = {(r, c): (r, c) for r in range(1, 51) for c in range(1, 51)}
    value = {(r, c): "" for r in range(1, 51) for c in range(1, 51)}
    ans = []
    def f(x):
        if parent[x] != x:
            parent[x] = f(parent[x])
        return parent[x]
    for cmd in commands:
        p = cmd.split()
        if p[0] == "UPDATE":
            if len(p) == 4:
                r, c, v = int(p[1]), int(p[2]), p[3]
                value[f((r, c))] = v
            else:
                v1, v2 = p[1], p[2]
                for k in value:
                    if value[f(k)] == v1:
                        value[f(k)] = v2
        elif p[0] == "MERGE":
            r1, c1, r2, c2 = map(int, p[1:])
            a, b = f((r1, c1)), f((r2, c2))
            if a != b:
                va, vb = value[a], value[b]
                parent[b] = a
                value[b] = ""
                if va == "" and vb != "":
                    value[a] = vb
        elif p[0] == "UNMERGE":
            r, c = int(p[1]), int(p[2])
            root = f((r, c))
            v = value[root]
            cells = [k for k in parent if f(k) == root]
            for k in cells:
                parent[k] = k
                value[k] = ""
            value[(r, c)] = v
        else: 
            r, c = int(p[1]), int(p[2])
            v = value[f((r, c))]
            ans.append(v if v else "EMPTY")
    return ans


from itertools import permutations
def solution(n, weak, dist):
    wlen = len(weak)
    extended = weak + [x + n for x in weak]
    for k in range(1, len(dist) + 1):
        for friends in permutations(dist, k):
            for start in range(wlen):
                targets = extended[start:start + wlen]
                coverage = targets[0] + friends[0]
                friend_idx = 0
                for t in targets:
                    if t > coverage:
                        friend_idx += 1
                        if friend_idx >= k:
                            break
                        coverage = t + friends[friend_idx]
                else:
                    return k
    return -1


def solution(k, room_number):
    room_dict = {}
    def find_room(n):
        if n not in room_dict:
            room_dict[n] = n + 1
            return n
        next_room = find_room(room_dict[n])
        room_dict[n] = next_room
        return next_room
    answer = []
    for num in room_number:
        assigned = find_room(num)
        answer.append(assigned)
    return answer


def solution(k, room_number):
    room_dict = {}
    def find_room(n):
        path = []
        while n in room_dict:
            path.append(n)
            n = room_dict[n]
        for p in path:
            room_dict[p] = n + 1
        room_dict[n] = n + 1
        return n
    answer = []
    for num in room_number:
        assigned = find_room(num)
        answer.append(assigned)
    return answer


def solution(play_time, adv_time, logs):
    def to_sec(t):
        h,m,s = map(int, t.split(':'))
        return h*3600 + m*60 + s
    def to_hms(s):
        h = s//3600
        m = (s%3600)//60
        sec = s%60
        return f"{h:02d}:{m:02d}:{sec:02d}"
    P = to_sec(play_time)
    A = to_sec(adv_time)
    arr = [0] * (P + 1)
    for log in logs:
        s, e = log.split('-')
        ss = to_sec(s)
        ee = to_sec(e)
        arr[ss] += 1
        if ee <= P:
            arr[ee] -= 1
    for i in range(1, P):
        arr[i] += arr[i-1]
    prefix = [0] * (P + 1)
    prefix[0] = arr[0]
    for i in range(1, P):
        prefix[i] = prefix[i-1] + arr[i]
    max_sum = prefix[A-1]
    max_start = 0
    for start in range(1, P - A + 1):
        cur = prefix[start + A - 1] - prefix[start - 1]
        if cur > max_sum:
            max_sum = cur
            max_start = start
    return to_hms(max_start)


from bisect import bisect_left, bisect_right
def solution(words, queries):
    words_by_length = {}
    reversed_words_by_length = {}
    for w in words:
        l = len(w)
        if l not in words_by_length:
            words_by_length[l] = []
            reversed_words_by_length[l] = []
        words_by_length[l].append(w)
        reversed_words_by_length[l].append(w[::-1])
    for l in words_by_length:
        words_by_length[l].sort()
        reversed_words_by_length[l].sort()
    def count_by_range(arr, left, right):
        return bisect_right(arr, right) - bisect_left(arr, left)
    answer = []
    for q in queries:
        l = len(q)
        if l not in words_by_length:  
            answer.append(0)
            continue
        if q[0] != '?':
            left = q.replace('?', 'a')
            right = q.replace('?', 'z')
            cnt = count_by_range(words_by_length[l], left, right)
        else:
            rq = q[::-1]
            left = rq.replace('?', 'a')
            right = rq.replace('?', 'z')
            cnt = count_by_range(reversed_words_by_length[l], left, right)
        answer.append(cnt)
    return answer


from collections import deque
def solution(board):
    n = len(board)
    board = [[1]*(n+2)] + [[1] + row + [1] for row in board] + [[1]*(n+2)]
    def get_next(pos):
        pos = list(pos)
        (x1, y1), (x2, y2) = pos
        nxt = []
        moves = [(1,0),(-1,0),(0,1),(0,-1)]
        for dx, dy in moves:
            nx1, ny1 = x1+dx, y1+dy
            nx2, ny2 = x2+dx, y2+dy
            if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
                nxt.append({(nx1, ny1), (nx2, ny2)})
        if x1 == x2:
            for d in [-1,1]:
                if board[x1+d][y1] == 0 and board[x2+d][y2] == 0:
                    nxt.append({(x1, y1), (x1+d, y1)})
                    nxt.append({(x2, y2), (x2+d, y2)})
        if y1 == y2:
            for d in [-1,1]:
                if board[x1][y1+d] == 0 and board[x2][y2+d] == 0:
                    nxt.append({(x1, y1), (x1, y1+d)})
                    nxt.append({(x2, y2), (x2, y2+d)})
        return nxt
    start = {(1,1),(1,2)}
    q = deque([(start, 0)])
    visited = set()
    visited.add(frozenset(start))
    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost
        for nxt in get_next(pos):
            f = frozenset(nxt)
            if f not in visited:
                visited.add(f)
                q.append((nxt, cost+1))
    return 0


def solution(edges):
    from collections import defaultdict, deque
    n = 0
    for a, b in edges:
        n = max(n, a, b)
    outdeg = [0] * (n + 1)
    indeg = [0] * (n + 1)
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        outdeg[a] += 1
        indeg[b] += 1
    generated = 0
    for node in range(1, n + 1):
        if indeg[node] == 0 and outdeg[node] >= 2:
            generated = node
            break
    donuts = 0
    sticks = 0
    eights = 0
    visited = set()
    for start in graph[generated]:
        if start in visited:
            continue
        q = deque([start])
        comp_nodes = set()
        while q:
            cur = q.popleft()
            if cur in comp_nodes:
                continue
            comp_nodes.add(cur)
            for nxt in graph[cur]:
                if nxt not in comp_nodes:
                    q.append(nxt)
        visited |= comp_nodes
        out0 = 0    
        out2 = 0   
        for node in comp_nodes:
            if outdeg[node] == 0:
                out0 += 1
            if outdeg[node] >= 2:
                out2 += 1
        if out0 >= 1:
            sticks += 1
        elif out2 >= 1:
            eights += 1
        else:
            donuts += 1
    return [generated, donuts, sticks, eights]


from itertools import combinations
from bisect import bisect_left, bisect_right
def solution(dice):
    n = len(dice)
    half = n // 2
    idx = list(range(n))
    best_win = -1
    best_choice = None
    def all_sums(selected):
        sums = [0]
        for d in selected:
            nxt = []
            for s in sums:
                for v in dice[d]:
                    nxt.append(s + v)
            sums = nxt
        sums.sort()
        return sums
    for comb in combinations(idx, half):
        a = comb
        b = [i for i in idx if i not in a]
        A = all_sums(a)
        B = all_sums(b)
        win = 0
        for s in A:
            win += bisect_left(B, s)
        if win > best_win:
            best_win = win
            best_choice = a
    return [x + 1 for x in best_choice]


import re
from collections import defaultdict
def solution(word, pages):
    word = word.lower()
    url_idx = {}
    base = []
    links = []
    for i, page in enumerate(pages):
        url = re.search(r'<meta property="og:url" content="(.*?)"/>', page).group(1)
        url_idx[url] = i
        text = re.sub(r'<[^>]*>', ' ', page).lower()
        words = re.findall(r'[a-z]+', text)
        base.append(words.count(word))
        link = re.findall(r'<a href="(.*?)">', page)
        links.append(link)
    score = [float(b) for b in base]
    for i in range(len(pages)):
        if links[i]:
            share = base[i] / len(links[i])
            for l in links[i]:
                if l in url_idx:
                    score[url_idx[l]] += share
    return score.index(max(score))


from collections import deque
from itertools import permutations
import copy
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs(board, sr, sc, tr, tc):
    visited = [[False]*4 for _ in range(4)]
    q = deque()
    q.append((sr, sc, 0))
    visited[sr][sc] = True
    while q:
        r, c, d = q.popleft()
        if r == tr and c == tc:
            return d
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 4 and 0 <= nc < 4 and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc, d + 1))
        for i in range(4):
            nr, nc = r, c
            while True:
                nr += dr[i]
                nc += dc[i]
                if not (0 <= nr < 4 and 0 <= nc < 4):
                    nr -= dr[i]
                    nc -= dc[i]
                    break
                if board[nr][nc] != 0:
                    break
            if not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc, d + 1))
    return 10**9
def solution(board, r, c):
    card_pos = dict()
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                card_pos.setdefault(board[i][j], []).append((i, j))
    cards = list(card_pos.keys())
    min_count = 10**9
    for order in permutations(cards):
        tmp_board = copy.deepcopy(board)
        cr, cc = r, c
        count = 0
        for card in order:
            (r1, c1), (r2, c2) = card_pos[card]
            d1 = bfs(tmp_board, cr, cc, r1, c1) + 1
            d2 = bfs(tmp_board, r1, c1, r2, c2) + 1
            cost1 = d1 + d2
            d1 = bfs(tmp_board, cr, cc, r2, c2) + 1
            d2 = bfs(tmp_board, r2, c2, r1, c1) + 1
            cost2 = d1 + d2
            if cost1 <= cost2:
                count += cost1
                cr, cc = r2, c2
            else:
                count += cost2
                cr, cc = r1, c1
            tmp_board[r1][c1] = 0
            tmp_board[r2][c2] = 0
        min_count = min(min_count, count)
    return min_count


from collections import defaultdict, deque
def solution(n, path, order):
    graph = [[] for _ in range(n)]
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)
    need = {}
    unlock = {}
    for a, b in order:
        need[b] = a
        unlock[a] = b
    if 0 in need:
        return False
    visited = [False] * n
    wait = {}
    q = deque([0])
    visited[0] = True
    while q:
        cur = q.popleft()
        
        if cur in unlock:
            nxt = unlock[cur]
            if nxt in wait:
                q.append(nxt)
                visited[nxt] = True
                del wait[nxt]
        for nxt in graph[cur]:
            if visited[nxt]:
                continue
            if nxt in need and not visited[need[nxt]]:
                wait[nxt] = True
                continue
            visited[nxt] = True
            q.append(nxt)
    return all(visited)


def solution(board):
    n = len(board)
    answer = 0
    def can_remove(num):
        coords = [(i, j) for i in range(n) for j in range(n) if board[i][j] == num]
        xs = [x for x, y in coords]
        ys = [y for x, y in coords]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        blanks = []
        for i in range(min_x, max_x + 1):
            for j in range(min_y, max_y + 1):
                if board[i][j] == 0:
                    blanks.append((i, j))
                elif board[i][j] != num:
                    return False
        if len(blanks) != 2:
            return False
        for x, y in blanks:
            for i in range(x):
                if board[i][y] != 0:
                    return False
        for x, y in coords:
            board[x][y] = 0
        return True
    while True:
        removed = 0
        nums = set(sum(board, []))
        nums.discard(0)
        for num in nums:
            if can_remove(num):
                removed += 1
        if removed == 0:
            break
        answer += removed
    return answer
