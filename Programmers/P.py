from itertools import combinations
def solution(n, q, ans):
    possible_answers = set(combinations(range(1, n + 1), 5))
    for attempt, count in zip(q, ans):
        new_possible_answers = set()
        for candidate in possible_answers:
            if len(set(candidate) & set(attempt)) == count: 
                new_possible_answers.add(candidate)
        possible_answers = new_possible_answers 
    return len(possible_answers)


def convertTime(n): 
    h = n // 100
    m = n % 100
    return h * 60 + m
def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        s = startday
        schedule = convertTime(schedules[i])
        for time in timelogs[i]:
            if s == 6 or s == 7:  
                s += 1
                if s == 8: 
                    s = 1
                continue
            t = convertTime(time)
            if schedule + 10 < t:  
                break
            else:
                s += 1
                if s == 8: 
                    s = 1
        else:
            answer += 1  
    return answer


