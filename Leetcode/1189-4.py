def maxNumberOfBalloons(text: str) -> int:
    freq = [0] * 5  # 'b', 'a', 'l', 'o', 'n' 순서
    
    for char in text:
        if char == 'b':
            freq[0] += 1
        elif char == 'a':
            freq[1] += 1
        elif char == 'l':
            freq[2] += 1
        elif char == 'o':
            freq[3] += 1
        elif char == 'n':
            freq[4] += 1
    
    freq[2] //= 2  # 'l'
    freq[3] //= 2  # 'o'
    
    return min(freq)
