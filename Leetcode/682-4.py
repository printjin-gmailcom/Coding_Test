def calPoints(ops: list[str]) -> int:
    record = []
    
    def process_C():
        record.pop()
    
    def process_D():
        record.append(2 * record[-1])
    
    def process_plus():
        record.append(record[-1] + record[-2])
    
    operations_map = {
        "C": process_C,
        "D": process_D,
        "+": process_plus
    }
    
    for op in ops:
        if op in operations_map:
            operations_map[op]()
        else:
            record.append(int(op))
    
    return sum(record)
