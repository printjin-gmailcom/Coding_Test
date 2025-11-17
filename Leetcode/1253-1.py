n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
for i in range(n):
    x = arr[i]
    l, r = 0, n - 1
    while l < r:
        if l == i:
            l += 1
            continue
        if r == i:
            r -= 1
            continue
        s = arr[l] + arr[r]
        if s == x:
            ans += 1
            break
        if s < x:
            l += 1
        else:
            r -= 1
print(ans)
