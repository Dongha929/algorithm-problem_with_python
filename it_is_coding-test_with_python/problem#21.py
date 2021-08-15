from collections import deque

n, left, right = map(int, input().split())
board = []
for _ in range(n):
  board.append(list(map(int, input().split())))

direction = [[0, 1, 0 ,-1], [1, 0, -1, 0]]

def BFS(union, start, count):
  union[start[0]][start[1]] = count
  q = deque([start])
  while q:
    x, y = q.popleft()
    for d in range(4):
      dx = x + direction[0][d]
      dy = y + direction[1][d]
      if dx >= 0 and dx < n and dy >= 0 and dy < n:
        difference = abs(board[x][y] - board[dx][dy])
        if union[dx][dy] == 0 and left <= difference <= right:
          union[dx][dy] = count
          q.append([dx, dy])

def makeunionlist(union, count):
  union_list = [[] for _ in range(count + 1)]
  for i in range(n):
    for j in range(n):
      union_list[union[i][j]].append([i, j])
  return union_list
  
result = 0
while True:
  union = [[0] * n for _ in range(n)]

  # BFS를 통해 연합을 계산함
  count = 1
  for i in range(n):
    for j in range(n):
      if union[i][j] == 0:
        BFS(union, [i, j], count)
        count += 1

  if count > n * n:
    break

  # 인구 이동
  union_list = makeunionlist(union, count - 1)
  for c in range(1, count):
    sum_value = 0
    for ex, ey in union_list[c]:
      sum_value += board[ex][ey]
    for ex, ey in union_list[c]:
      board[ex][ey] = sum_value // len(union_list[c])
  
  result += 1
  
print(result)