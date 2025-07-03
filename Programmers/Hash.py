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


from collections import defaultdict
def solution(genres, plays):
    genre_total = defaultdict(int)
    genre_songs = defaultdict(list)
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_total[g] += p
        genre_songs[g].append((p, i))
    sorted_genres = sorted(genre_total.items(), key=lambda x: -x[1])
    answer = []
    for genre, _ in sorted_genres:
        songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        answer.extend([idx for _, idx in songs[:2]])
    return answer

