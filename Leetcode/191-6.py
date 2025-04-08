def hammingWeight(n: int) -> int:
    return sum(map(int, bin(n)[2:]))
