from collections import defaultdict

def maxNumberOfBalloons(text: str) -> int:
    freq = defaultdict(int)
    
    for char in text:
        if char in "balloon":
            freq[char] += 1
    
    return min(freq['b'], freq['a'], freq['l'] // 2, freq['o'] // 2, freq['n'])
