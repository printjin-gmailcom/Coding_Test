# 두 사람이 번갈아가며 사탕을 가져갈 때, 가장 많은 가치를 얻은 사람이 이기는 게임에서 승자를 구하는 문제.

T = int(input())

for _ in range(T):
    N = int(input())
    candies = list(map(int, input().split())) # 사탕의 가치 리스트

    candies.sort(reverse=True)

    player1, player2 = 0, 0
    for i in range(N):
        if i % 2 == 0:
            player1 += candies[i]
        else:
            player2 += candies[i]

    if player1 > player2:
        print("Player 1 wins with", player1)
    elif player2 > player1:
        print("Player 2 wins with", player2)
    else:
        print("Draw")



# 주어진 물건들 중 가격이 가장 비싼 두 물건의 가치를 합하여 출력하는 문제.

N = int(input())
items = []

for _ in range(N):
    S, P = map(int, input().split())
    items.append((P, S))  

items.sort(reverse=True, key=lambda x: x[0])

result = items[0][1] + items[1][1]

print(result)


# 주어진 방향 지시에 따라 자율 주행 차가 이동한 후 최종 좌표를 출력하는 문제.

N = int(input())
commands = input().strip()
x, y = 0, 0
direction = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for command in commands:
    if command == 'F':
        x += dx[direction]
        y += dy[direction]
    elif command == 'L':
        direction = (direction - 1) % 4
    elif command == 'R':
        direction = (direction + 1) % 4

print(x, y)


# 구름이 나무의 높이를 제어하며 일정 규칙에 따라 나무의 높이를 변화시키고, 최종적으로 주어진 과정을 완료한 후 나무들의 상태를 출력하는 문제.

N, M = map(int, input().split())
trees = list(map(int, input().split()))

for _ in range(M):
    command, X, H = input().split() # 명령어, X: 나무 번호, H: 높이 또는 범위
    X = int(X) - 1 # 나무 번호는 0부터 시작하므로 1을 뺍니다.
    H = int(H)

    if command == 'L': # X번 나무 포함 좌측 모든 나무들 높이를 H만큼 자릅니다.
        for i in range(X + 1):
            trees[i] = min(trees[i], H)
    elif command == 'R':
        for i in range(X, N):
            trees[i] = min(trees[i], H)
    elif command == 'S':
        trees[X] = H

print(' '.join(map(str, trees)))


# 미로에서 주어진 출발 위치에서 목표 위치까지 탈출할 수 있는지를 판단하는 문제.

def escape_maze(N, K, commands, maze):
    start = None
    end = None
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 1:
                start = (i, j)
            elif maze[i][j] == 2:
                end = (i, j)

    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    x, y = start
    move_count = 0
    for command in commands:
        dx, dy = directions[command]
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 3:
            x, y = nx, ny
            move_count += 1
        if (x, y) == end:
            return "SUCCESS", move_count
    return "FAIL", move_count

N, K = map(int, input().split())  # N: 미로 크기, K: 명령어 개수
commands = input().strip()
maze = [list(map(int, input().split())) for _ in range(N)]
result, moves = escape_maze(N, K, commands, maze)
print(result, moves)
