import copy, sys

input = sys.stdin.readline
N = int(input())
B = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0

def move(x, y, d, save):
  if B[x][y] != 0:
    nx = x + dx[d]
    ny = y + dy[d]
    if B[nx][ny] == 0:
      B[x][y], B[nx][ny] = B[nx][ny], B[x][y]
    elif B[nx][ny] == B[x][y] and [nx, ny] not in save:
      B[x][y], B[nx][ny] = 0, B[x][y] + B[nx][ny]
      save.append([nx, ny])

def move_line(d):
  if d == 0: # up
    temp = []
    for i in range(1, N):
      for j in range(i, 0, -1):
        # j번째 row을 위로 보냄
        for x, y in [[j, k] for k in range(N)]:
          move(x, y, d, temp)
  elif d == 1: # down
    temp = []
    for i in range(N - 2, -1, -1):
      for j in range(i, N - 1):
        # j번째 row를 아래로 보냄
        for x, y in [[j, k] for k in range(N)]:
          move(x, y, d, temp)
  elif d == 2: # left
    temp = []
    for i in range(1, N):
      for j in range(i, 0, -1):
        # j번째 col을 왼쪽으로 보냄
        for x, y in [[k, j] for k in range(N)]:
          move(x, y, d, temp)
  elif d == 3: # right
    temp = []
    for i in range(N - 2, -1, -1):
      for j in range(i, N - 1):
        # j번째 col를 오른쪽로 보냄
        for x, y in [[k, j] for k in range(N)]:
          move(x, y, d, temp)

def DFS(depth):
  global ans, B
  if depth == 5:
    for num in B:
      ans = max(ans, max(num))
    return
  nb = copy.deepcopy(B)
  for i in range(4):
    move_line(i)
    DFS(depth + 1)
    B = copy.deepcopy(nb)

DFS(0)
print(ans)
