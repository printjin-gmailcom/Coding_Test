def calculate_cost(STD, BASE_COST, DISTS):
    costs = []
    for dist in DISTS:
        if dist <= STD:
            costs.append(BASE_COST)
        else:
            extra_distance = dist - STD
            extra_cost = extra_distance * 1000  # 1KM당 1000원 추가
            total_cost = BASE_COST + extra_cost
            costs.append(total_cost)
    return costs

# 예제 데이터
STD = 10
BASE_COST = 5000
DISTS = [8, 10, 12, 15, 20]

costs = calculate_cost(STD, BASE_COST, DISTS)

print(costs)

def calculate_areas_from_points(POINTS):
    areas = []

    for i in range(len(POINTS) - 2):
        p1, p2, p3 = POINTS[i], POINTS[i+1], POINTS[i+2]

        area = abs(p3 - p1)
        areas.append(area)

    areas = sorted(list(set(areas)))
    return areas

# 예제 실행
POINTS = [1, 12, 4, 14, 5, 17, 9]
areas = calculate_areas_from_points(POINTS)
print(areas)

def update_font_size(TEXT, COMMANDS):
    default_font_size = 16

    id_font_size = {}
    class_font_size = {}

    for command in COMMANDS:
        selector, font_size = command.split(", ")
        font_size = int(font_size)

        if selector.startswith("#"):
            id_font_size[selector[1:]] = font_size
        elif selector.startswith("."):
            class_font_size[selector[1:]] = font_size

    final_font_sizes = []

    for text in TEXT:
        parts = text.split()
        id_ = parts[0]
        class_ = parts[1]

        if id_ in id_font_size:
            font_size = id_font_size[id_]
        elif class_ in class_font_size:
            font_size = class_font_size[class_]
        else:
            font_size = default_font_size

        final_font_sizes.append(font_size)

    return final_font_sizes

# 예제 데이터
TEXT = ["Z 1 2 3", "D 3 10"]
COMMANDS = [".3, 17", "#D, 99"]

final_font_sizes = update_font_size(TEXT, COMMANDS)
print(final_font_sizes)

def rearrange_array(N, arr):
    remainder_dict = {i: [] for i in range(N)}

    for num in arr:
        remainder = num % N
        remainder_dict[remainder].append(num)

    for key in remainder_dict:
        remainder_dict[key].sort()

    result = [-1] * N
    for i in range(N):
        if remainder_dict[i]:
            result[i] = remainder_dict[i][0]
            remainder_dict[i].pop(0)

    leftovers = []
    for key in remainder_dict:
        leftovers.extend(remainder_dict[key])
    leftovers.sort()

    for i in range(N):
        if result[i] == -1:
            result[i] = leftovers.pop(0)

    return result

# 예제 실행
N = 7
arr = [2, 5, 6, 13, 14, 16, 35]
result = rearrange_array(N, arr)
print(result)
