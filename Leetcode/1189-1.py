from collections import Counter

def maxNumberOfBalloons(text: str) -> int:
    count = Counter(text)
    return min(count['b'], count['a'], count['l'] // 2, count['o'] // 2, count['n'])
