def hammingWeight(n: int) -> int:
    return sum([1 for bit in bin(n) if bit == '1'])
