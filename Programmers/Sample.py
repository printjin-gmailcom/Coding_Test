message = "let's go!"
print("3 \n 2 \n 1")
print(message)


code = input()
last_four_words = code[-4:]
if last_four_words == '_eye':
    print("Ophthalmologyc")
elif last_four_words == 'head':
    print("Neurosurgery")
elif last_four_words == 'infl':
    print("Orthopedics")
elif last_four_words == 'skin':
    print("Dermatology")
else:
    print("direct recommendation")


def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    for action in cpr
        for i in range(len(basic_order))
            if action == basic_order[i]:
                answer.append(i+1)
    return answer


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


angle1 = int(input())
angle2 = int(input())
sum_angle = (angle1 + angle2)%360
print(sum_angle)


number = int(input())
answer = 0
while number > 0:
    answer += number % 100
    number //= 100
print(answer)


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
    if len(answer) < 3:
        answer += "o" * (4 - len(answer))
    if len(answer) > 8:
        answer = answer[:8]
    return answer


def solution(wallet, bill):
    answer = 0
    while True:
        if (bill[0] <= wallet[0] and bill[1] <= wallet[1]) or (bill[1] <= wallet[0] and bill[0] <= wallet[1]):
            break
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1
    return answer


def can_place(mat_size, park, x, y):
    for i in range(x, x + mat_size):
        for j in range(y, y + mat_size):
            if i >= len(park) or j >= len(park[0]) or park[i][j] != "-1":
                return False
    return True
def solution(mats, park):
    answer = -1
    mats.sort(reverse=True)
    for mat_size in mats:
        for i in range(len(park) - mat_size + 1):
            for j in range(len(park[0]) - mat_size + 1):
                if can_place(mat_size, park, i, j):
                    answer = mat_size
                    return answer
    return answer


a = int(input())
c = int(input())
b_square = c**2 - a**2
print(b_square)


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
    elif humidity >= 0:
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
        elif i == "W":
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


year = int(input())
age_type = input()
if age_type == "Korea":
    answer = 2030 - year + 1
elif age_type == "Year":
    answer = 2030-year    
print(answer)


string_msg = 'Spring is beginning'
int_val = int(3)
string_val = '3'
print(string_msg)
print(int_val + 10)
print(string_val + "10")


def solution(board, h, w):
    n = len(board)
    count = 0
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    target_color = board[h][w]
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if 0 <= h_check < n and 0 <= w_check < n:
            if board[h_check][w_check] == target_color:
                count += 1
    return count


def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        if our_score[i] == score_list[numbers[i] - 1]:
            answer.append("Same")
        else:
            answer.append("Different")
    return answer


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