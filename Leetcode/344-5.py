def reverseString(s: list[str]) -> None:
    stack = list(s)
    for i in range(len(s)):
        s[i] = stack.pop()
