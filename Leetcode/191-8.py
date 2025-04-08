def hammingWeight(n: int) -> int:
    return len([x for x in bin(n) if x == '1'])
