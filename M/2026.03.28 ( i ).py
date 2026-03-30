def grade_problem(s):
    total = len(s)
    correct = 0
    time_sum = 0
    for i in range(total):
        if s[i] != 0:
            correct += 1
            time_sum += s[i]
    if correct == 0:
        accuracy = 0
        avg_time = 0
    else:
        accuracy = correct / total
        avg_time = time_sum / correct
    if accuracy >= 0.8 and avg_time <= 20:
        return "A"
    elif accuracy >= 0.6 and avg_time <= 30:
        return "B"
    elif accuracy >= 0.4 and avg_time <= 40:
        return "C"
    elif accuracy >= 0.2:
        return "D"
    elif accuracy > 0:
        return "E"
    else:
        return "F"


def solution(playlist):
    count = {}
    order = {}
    idx = 0
    for s in playlist:
        for w in s.split():
            if w not in count:
                count[w] = 0
                order[w] = idx
                idx += 1
            count[w] += 1
    def sort_key(x):
        return (-count[x], order[x])
    result = sorted(count.keys(), key=sort_key)
    return result


# 정렬되지 않은 positions에서 3개씩 묶되, 남는 원소는 버릴 수 있고 각 그룹의 (최대값−최소값)을 최소화하도록 그룹을 구성
def solution(positions):
    positions.sort()
    n = len(positions)
    dp = [0] * n
    for i in range(n):
        dp[i] = dp[i-1] if i > 0 else 0
        if i >= 2:
            val = (dp[i-3] if i >= 3 else 0) + (positions[i] - positions[i-2])
            dp[i] = min(dp[i], val)
    return dp[-1]


# 각 사람은 다른 사람에 대해 알리바이(있음/없음)를 말하는데 시민은 반드시 진실만 말하고 범죄자는 아무 말이나 할 수 있음
# 어떤 m명의 집합을 범죄자로 정했을 때 남은 사람들(시민들)의 말이 서로 모순되지 않으면 그 집합은 가능한 범죄자 구성
from itertools import combinations
def find_criminals(statements, m):
    n = len(statements)
    people = list(range(n))
    valid_cases = []
    for criminals in combinations(people, m):
        criminals_set = set(criminals)
        civilians = [p for p in people if p not in criminals_set]
        ok = True
        alibi = {}
        for i in civilians:
            for j in civilians:
                if i == j:
                    continue
                val = statements[i][j]
                if val == 0:
                    continue
                if j not in alibi:
                    alibi[j] = val
                else:
                    if alibi[j] != val:
                        ok = False
                        break
            if not ok:
                break
        if ok:
            valid_cases.append(criminals)
    return valid_cases


'''
SELECT 
    STUDENT,
    MAX(
        CASE 
            WHEN SCORE <= 70 THEN 0
            WHEN SCORE <= 80 THEN 1
            WHEN SCORE <= 90 THEN 2
            ELSE 3
        END
    ) AS MAX_SCORE
FROM YOUR_TABLE
GROUP BY STUDENT
ORDER BY MAX_SCORE ASC, STUDENT ASC;
'''
