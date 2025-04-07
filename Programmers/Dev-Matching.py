def solution(lottos, win_nums):
    a = lottos.count(0)
    ans = sum(1 for lotto in lottos if lotto in win_nums)
    highest_rank = 7 - (ans + a) if ans + a > 1 else 6
    lowest_rank = 7 - ans if ans > 1 else 6
    return [highest_rank, lowest_rank]


