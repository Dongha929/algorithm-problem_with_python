n = int(input())
board = [[0] * (n + 2) for _ in range(n + 2)]

m = int(input())
for _ in range(m):
  x, y = map(int, input().split())
  board[x][y] = 2

for i in range(n + 2):
  for j in range(n + 2):
    if i == 0 or i == n + 1 or j == 0 or j == n + 1:
      board[i][j] = 1

moving = []
k = int(input())
for _ in range(k):
  now = input().split()
  moving.append([int(now[0]), now[1]])

result = 0
hx, hy = 1, 1
tail = []
tail.append([hx, hy])
direc = 0
dx = [0, 1, 0 ,-1]
dy = [1, 0, -1, 0]
board[hx][hy] = 1

while 1:
  if len(moving):
    if moving[0][0] == result:
      if moving[0][1] == 'D':
        direc = (direc + 1) % 4
      else:
        direc = (direc - 1) % 4
      del(moving[0])

  hx += dx[direc]
  hy += dy[direc]
    
  if board[hx][hy] == 2:
    board[hx][hy] = 1
    tail.append([hx, hy])
  elif board[hx][hy] == 0:
    board[hx][hy] = 1
    tail.append([hx, hy])
    board[tail[0][0]][tail[0][1]] = 0
    del tail[0]
  else:
    print(result + 1)
    break
    
  result += 1