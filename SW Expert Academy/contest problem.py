T = int(input())
for test_case in range(1, T + 1):
    n = input()
    if "9" in n:
        print(f"#{test_case} Yes")
    else:
        print(f"#{test_case} No")


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    total = 0
    for _ in range(N):
        L, R = map(int, input().split())
        total += R - L + 1
    print(f"#{test_case} {total}")
  
