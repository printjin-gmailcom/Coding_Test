def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] <= i:
            return i 
    return len(citations)


def solution(array, commands):
    answer = []
    for command in commands:
        temp = array[command[0]-1:command[1]]
        temp.sort()
        answer.append(temp[command[2]-1])
    return answer


def solution(numbers):
    numbers = list(map(str, numbers)) 
    numbers.sort(key=lambda x: x * 3, reverse=True) 
    return str(int(''.join(numbers))) 


