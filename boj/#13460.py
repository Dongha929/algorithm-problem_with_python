from collections import deque

n, m = list(map(int, input().split()))
board = [list(input().rstrip()) for _ in range(n)]

irx, iry, ibx, iby = -1, -1, -1, -1
for i in range(n):
  for j in range(m):
    if board[i][j] == 'R':
      irx, iry = i, j
    elif board[i][j] == 'B':
      ibx, iby = i, j

dir_x = [-1, 1, 0, 0]
dir_y = [0, 0, -1, 1]

def move(x, y, dx, dy):
  step = 0
  while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
    x += dx
    y += dy
    step += 1
  return x, y, step

visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

# q = [[red], [blue], iteration]
def BFS(q):
  while q:
    now_red, now_blue, count = q.popleft()
    if count > 10:
      break
    for i in range(4):
      rx, ry, rstep = move(now_red[0], now_red[1], dir_x[i], dir_y[i]) 
      bx, by, bstep = move(now_blue[0], now_blue[1], dir_x[i], dir_y[i]) 
      if board[bx][by] != 'O':
        if board[rx][ry] == 'O':
          return print(count)
        if rx == bx and ry == by:
          if rstep > bstep:
            rx -= dir_x[i]
            ry -= dir_y[i]
          else:
            bx -= dir_x[i]
            by -= dir_y[i]
        if not visited[rx][ry][bx][by]:
          visited[rx][ry][bx][by] = True
          q.append(([rx, ry], [bx, by], count + 1))
  print(-1)

visited[irx][iry][ibx][iby] = True
q = deque([])
q.append(([irx, iry], [ibx, iby], 1))
BFS(q)
