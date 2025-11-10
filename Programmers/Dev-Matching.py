def solution(lottos, win_nums):
    a = lottos.count(0)
    ans = sum(1 for lotto in lottos if lotto in win_nums)
    highest_rank = 7 - (ans + a) if ans + a > 1 else 6
    lowest_rank = 7 - ans if ans > 1 else 6
    return [highest_rank, lowest_rank]


def solution(rows, columns, queries):
    matrix = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    answer = []
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        prev = matrix[x1][y1]
        min_value = prev
        for y in range(y1 + 1, y2 + 1):
            matrix[x1][y], prev = prev, matrix[x1][y]
            min_value = min(min_value, prev)
        for x in range(x1 + 1, x2 + 1):
            matrix[x][y2], prev = prev, matrix[x][y2]
            min_value = min(min_value, prev)
        for y in range(y2 - 1, y1 - 1, -1):
            matrix[x2][y], prev = prev, matrix[x2][y]
            min_value = min(min_value, prev)
        for x in range(x2 - 1, x1 - 1, -1):
            matrix[x][y1], prev = prev, matrix[x][y1]
            min_value = min(min_value, prev)
        answer.append(min_value)
    return answer
