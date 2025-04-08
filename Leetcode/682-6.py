def calPoints(ops: list[str]) -> int:
    def process_ops(ops, record):
        if not ops:
            return sum(record)
        
        op = ops.pop(0)
        
        if op == "C":
            record.pop()
        elif op == "D":
            record.append(2 * record[-1])
        elif op == "+":
            record.append(record[-1] + record[-2])
        else:
            record.append(int(op))
        
        return process_ops(ops, record)
    
    return process_ops(ops, [])
