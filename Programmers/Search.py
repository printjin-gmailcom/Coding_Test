def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == pattern1[i % len(pattern1)]:
            scores[0] += 1
        if answers[i] == pattern2[i % len(pattern2)]:
            scores[1] += 1
        if answers[i] == pattern3[i % len(pattern3)]:
            scores[2] += 1
    max_score = max(scores)
    return [i + 1 for i, score in enumerate(scores) if score == max_score]


def dfs(k, dungeons, visited):
    max_count = 0
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            max_count = max(max_count, 1 + dfs(k - dungeons[i][1], dungeons, visited))
            visited[i] = False
    return max_count
def solution(k, dungeons):
    visited = [False] * len(dungeons)
    return dfs(k, dungeons, visited)


def solution(sizes):
    answer = 0
    ans = [0, 0] 
    for size in sizes:
        if size[0] > size[1]:
            size[0], size[1] = size[1], size[0] 
        ans[0] = max(ans[0], size[0])  
        ans[1] = max(ans[1], size[1]) 
    answer = ans[0] * ans[1]
    return answer


import math
def solution(brown, yellow):
    answer = []
    ans = brown + yellow
    for i in range(3, int(math.sqrt(ans)) + 1):
        if ans % i == 0:
            if (ans // i - 2) * (i - 2) == yellow:
                return [ans // i, i]
    return answer