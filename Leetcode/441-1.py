def arrangeCoins(n: int) -> int:
    row = 0
    while n >= row + 1:
        row += 1
        n -= row
    return row
