def calPoints(ops: list[str]) -> int:
    record = []
    
    [record.append(int(op)) if op not in ["C", "D", "+"] else (record.pop() if op == "C" else record.append(2 * record[-1]) if op == "D" else record.append(record[-1] + record[-2])) for op in ops]
    
    return sum(record)
