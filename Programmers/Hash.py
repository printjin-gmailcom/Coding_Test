def solution(nums):
    max_types = len(set(nums))
    max_selectable = len(nums) // 2
    answer = min(max_types, max_selectable)
    return answer


from collections import Counter
def solution(participant, completion):
    participant_count = Counter(participant)
    completion_count = Counter(completion)
    answer = list((participant_count - completion_count).keys())[0]
    return answer
