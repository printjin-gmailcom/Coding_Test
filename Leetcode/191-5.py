def hammingWeight(n: int) -> int:
    if n == 0:
        return 0
    return (n & 1) + hammingWeight(n >> 1)
