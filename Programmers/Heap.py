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


def solution(operations):
    queue = []
    for op in operations:
        cmd, num = op.split()
        num = int(num)
        if cmd == "I":
            queue.append(num)
        elif cmd == "D" and queue:
            if num == 1:
                queue.remove(max(queue))
            else:
                queue.remove(min(queue))
    if not queue:
        return [0, 0]
    else:
        return [max(queue), min(queue)]


import heapq
def solution(operations):
    min_heap, max_heap = [], []
    visited = {}
    id_counter = 0
    for op in operations:
        cmd, num = op.split()
        num = int(num)
        if cmd == "I":
            heapq.heappush(min_heap, (num, id_counter))
            heapq.heappush(max_heap, (-num, id_counter))
            visited[id_counter] = True
            id_counter += 1
        elif cmd == "D":
            if num == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    _, idx = heapq.heappop(max_heap)
                    visited[idx] = False
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    _, idx = heapq.heappop(min_heap)
                    visited[idx] = False
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    if not min_heap or not max_heap:
        return [0, 0]
    else:
        return [-max_heap[0][0], min_heap[0][0]]


import heapq
def solution(jobs):
    jobs.sort(key=lambda x: x[0])
    n = len(jobs)
    heap = []
    time, idx, total_turnaround = 0, 0, 0
    while idx < n or heap:
        while idx < n and jobs[idx][0] <= time:
            start, length = jobs[idx]
            heapq.heappush(heap, (length, start)) 
            idx += 1
        if heap:
            length, start = heapq.heappop(heap)
            time += length
            total_turnaround += time - start
        else:
            time = jobs[idx][0]
    return total_turnaround // n
