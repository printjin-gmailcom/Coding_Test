def calPoints(ops: list[str]) -> int:
    record = []
    
    i = 0
    while i < len(ops):
        if ops[i] == "C":
            record.pop()
        elif ops[i] == "D":
            record.append(2 * record[-1])
        elif ops[i] == "+":
            record.append(record[-1] + record[-2])
        else:
            record.append(int(ops[i]))
        i += 1
    
    return sum(record)
