def solution(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char) 
    if stack:
        return 0
    else:
        return 1 


def solution(n, a, b):
    answer = 0
    while a != b:
        a = (a + 1) // 2 
        b = (b + 1) // 2 
        answer += 1  
    return answer