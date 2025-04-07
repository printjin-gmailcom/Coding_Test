message = "Let's go!"
print("3\n2\n1")
print(message)


def solution(route):
    east = 0
    north = 0
    for i in route:
        if i == "N":
            north += 1
        elif i == "S" :
            north -= 1
        elif i == "E" :
            east += 1
        elif i == "W" :
            east -= 1
    return [east, north]



start = int(input())
before = int(input())
after = int(input())
money = start
month = 1
while money < 70:
    money += before
    month += 1
while money < 100:    
    money += after
    month += 1
print(month)


code = input()
last_four_words = code[-4:]
if last_four_words == "_eye":
    print("Ophthalmologyc")
elif last_four_words == "head":
    print("Neurosurgery")
elif last_four_words == "infl":
    print("Orthopedics")
elif last_four_words == "skin":
    print("Dermatology")
else:
    print("direct recommendation")


a = int(input())
c = int(input())
b_square = c**2 - a**2
print(b_square)


year = int(input())
age_type = input()
if age_type == "Korea":
    answer = 2030 - year + 1
elif age_type == "Year":
    answer = 2030 - year
print(answer)


def func1(humidity, val_set):
    if humidity < val_set:
        return 3  
    return 1  
def func2(humidity):
    if humidity >= 50:
        return 0
    elif humidity >= 40:
        return 1
    elif humidity >= 30:
        return 2
    elif humidity >= 20:
        return 3
    elif humidity >= 10:
        return 4
    else:
        return 5
def func3(humidity, val_set):
    if humidity < val_set:
        return 1  
    return 0  
def solution(mode_type, humidity, val_set):
    answer = 0
    if mode_type == "auto":
        answer = func2(humidity) 
    elif mode_type == "target":
        answer = func1(humidity, val_set)  
    elif mode_type == "minimum":
        answer = func3(humidity, val_set)  
    return answer


angle1 = int(input())
angle2 = int(input())
sum_angle = (angle1 + angle2)%360
print(sum_angle)


def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    for action in cpr:
        for i in range(len(basic_order)):
            if action == basic_order[i]:
                answer.append(i+1)
    return answer


def solution(nickname):
    answer = ""
    for letter in nickname:
        if letter == "l":
            answer += "I"
        elif letter == "w":
            answer += "vv"
        elif letter == "W":
            answer += "VV"
        elif letter == "O":
            answer += "0"
        else:
            answer += letter
    while len(answer) < 4:
        answer += "o"
    if len(answer) > 8:
        answer = answer[:8]
    return answer


def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        if our_score[i] == score_list[numbers[i]-1]:
            answer.append("Same")
        else:
            answer.append("Different")
    return answer


number = int(input())
answer = 0
for i in range(len(str(number))//2):
    answer += number % 100
    number //= 100
print(answer)


string_msg = "Spring is beginning"
int_val = int(3)
string_val = str(3)
print(string_msg)
print(int_val + 10)
print(string_val + "10")


def solution(storage, num):
    clean_storage = []
    clean_num = []
    for i in range(len(storage)):
        if storage[i] in clean_storage:
            pos = clean_storage.index(storage[i])
            clean_num[pos] += num[i]
        else:
            clean_storage.append(storage[i])
            clean_num.append(num[i])
    max_num = max(clean_num)
    answer = clean_storage[clean_num.index(max_num)]
    return answer


def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)):
        usage = int(usage * (100 + change[i]) / 100)
        total_usage += usage
        if total_usage > storage:
            return i
    return -1


def func1(num):
    if 0 > num:
        return 0
    else:
        return num
def func2(num):
    if num > 0:
        return 0
    else:
        return num
def func3(station):
    num = 0
    for people in station:
        if people == "Off":
            num += 1
    return num
def func4(station):
    num = 0
    for people in station:
        if people == "On":
            num += 1
    return num
def solution(seat, passengers):
    num_passenger = 0
    for station in passengers:
        num_passenger += func4(station)  
        num_passenger -= func3(station)  
    answer = func1(seat - num_passenger)  
    return answer


def solution(data, ext, val_ext, sort_by):
    filtered_data = []
    for row in data:
        if ext == "code" and row[0] < val_ext:
            filtered_data.append(row)
        elif ext == "date" and row[1] < val_ext:
            filtered_data.append(row)
        elif ext == "maximum" and row[2] < val_ext:
            filtered_data.append(row)
        elif ext == "remain" and row[3] < val_ext:
            filtered_data.append(row)
    if sort_by == "code":
        filtered_data.sort(key=lambda x: x[0]) 
    elif sort_by == "date":
        filtered_data.sort(key=lambda x: x[1])  
    elif sort_by == "maximum":
        filtered_data.sort(key=lambda x: x[2])  
    elif sort_by == "remain":
        filtered_data.sort(key=lambda x: x[3])  
    return filtered_data


def solution(board, h, w):
    n = len(board)
    count = 0
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]
    for i in range(4):  
        h_check, w_check = h + dh[i], w + dw[i]
        if 0 <= h_check < n and 0 <= w_check < n:
            if board[h][w] == board[h_check][w_check]:
                count += 1
    return count


def solution(bandage, health, attacks):
    max_health = health 
    last_time = 0 
    sequence = 0  
    for attack_time, damage in attacks:
        duration = attack_time - last_time - 1  
        if duration > 0:
            heal_amount = duration * bandage[1]
            extra_heal = (duration // bandage[0]) * bandage[2]
            health = min(max_health, health + heal_amount + extra_heal)
        health -= damage
        if health <= 0:
            return -1 
        last_time = attack_time  
        sequence = 0  
    return health


def time_to_seconds(time_str):
    minutes, seconds = map(int, time_str.split(":"))
    return minutes * 60 + seconds
def seconds_to_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"  
def solution(video_len, pos, op_start, op_end, commands):
    video_len_sec = time_to_seconds(video_len)
    p = time_to_seconds(pos)
    st = time_to_seconds(op_start)
    en = time_to_seconds(op_end)
    if st <= p <= en: 
        p = en
    for command in commands:
        if command == 'next':
            if p + 10 <= video_len_sec:
                p += 10
            else:
                p = video_len_sec
        elif command == 'prev':
            if p - 10 >= 0:
                p -= 10
            else:
                p = 0
        if st <= p <= en: 
            p = en
    return seconds_to_time(p)


def solution(mats, park):
    n, m = len(park), len(park[0])
    dp = [[0] * m for _ in range(n)] 
    max_square = 0 
    for i in range(n):
        for j in range(m):
            if park[i][j] == "-1":
                if i == 0 or j == 0:
                    dp[i][j] = 1 
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1  
                max_square = max(max_square, dp[i][j]) 
    mats.sort(reverse=True)  
    for size in mats:
        if size <= max_square:
            return size
    return -1


def solution(wallet, bill):
    answer = 0
    while min(bill) > min(wallet) or max(bill) > max(wallet):
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1
    return answer


