import math
def solution(progresses, speeds):
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    result = []
    current_deploy_day = days[0]
    count = 0
    for day in days:
        if day <= current_deploy_day:
            count += 1
        else:
            result.append(count)
            count = 1
            current_deploy_day = day
    result.append(count)
    return result