def calPoints(ops: list[str]) -> int:
    record = []
    
    for op in ops:
        try:
            record.append(int(op))
        except ValueError:
            if op == "C":
                record.pop()
            elif op == "D":
                record.append(2 * record[-1])
            elif op == "+":
                record.append(record[-1] + record[-2])
    
    return sum(record)
