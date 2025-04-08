from collections import deque

def calPoints(ops: list[str]) -> int:
    record = deque()
    
    for op in ops:
        if op == "C":
            record.pop()
        elif op == "D":
            record.append(2 * record[-1])
        elif op == "+":
            record.append(record[-1] + record[-2])
        else:
            record.append(int(op))
    
    return sum(record)
