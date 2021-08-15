from itertools import combinations

n = int(input())
board = []
for i in range(n):
  board.append(list(input().split()))
teachers = []
empties = []

for i in range(n):
  for j in range(n):
    if board[i][j] == 'T':
      teachers.append([i, j])
    elif board[i][j] == 'X':
      empties.append([i, j])

direction = [[0, 1, 0, -1], [1, 0, -1, 0]]
def DFS(now, d):
  x = now[0]
  y = now[1]
  if x < n and x >= 0 and y < n and y >= 0:
    if board[x][y] == 'S':
      return True
    elif board[x][y] == 'O':
      return False
    else:
      return DFS([x + direction[0][d], y + direction[1][d]], d)
  else:
    return False

def see_all():
  for teacher in teachers:
    if DFS(teacher, 0) or DFS(teacher, 1) or DFS(teacher, 2) or DFS(teacher, 3):
      return True
  return False

result = False
for obstacles in list(combinations(empties, 3)):
  for obstacle in obstacles:
    board[obstacle[0]][obstacle[1]] = 'O'
  if not see_all():
    result = True
    break
  for obstacle in obstacles:
    board[obstacle[0]][obstacle[1]] = 'X'

if result:
  print("YES")
else:
  print("NO")