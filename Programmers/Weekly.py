def solution(price, money, count):
    total = 0
    for i in range(1, count + 1): 
        total += price * i 
    if total > money:  
        answer = total - money 
    else:
        answer = 0  
    return answer


def solution(arr):
    def compress(x, y, size):
        start = arr[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != start:
                    size //= 2
                    a1 = compress(x, y, size)
                    a2 = compress(x, y + size, size)
                    a3 = compress(x + size, y, size)
                    a4 = compress(x + size, y + size, size)
                    return [a1[0] + a2[0] + a3[0] + a4[0], a1[1] + a2[1] + a3[1] + a4[1]]
        if start == 0:
            return [1, 0]
        else:
            return [0, 1]
    return compress(0, 0, len(arr))
