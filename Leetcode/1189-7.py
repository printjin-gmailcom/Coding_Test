from collections import Counter

def maxNumberOfBalloons(text: str) -> int:
    count = Counter(text)
    
    count['l'] //= 2
    count['o'] //= 2
    
    return min(count[c] for c in 'balon')
