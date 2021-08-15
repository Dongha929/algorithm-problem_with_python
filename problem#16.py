from collections import deque
from itertools import combinations

n, m = map(int, input().split())
lab_map = []
for _ in range(n):
  lab_map.append(list(map(int, input().split())))
 
direction = [[0, 1, 0, -1], [1, 0, -1, 0]]

def BFS(lab_map, start):
  q = deque([start])
  lab_map[start[0]][start[1]] = 2
  while q:
    now = q.popleft()
    for i in range(4):
      nx = now[0] + direction[0][i]
      ny = now[1] + direction[1][i]
      if nx < 0 or nx >= n or ny >= m or ny < 0:
        continue
      if lab_map[nx][ny] == 0:
        q.append([nx, ny])
        lab_map[nx][ny] = 2

virus_index = []
blank_index = []
for i in range(n):
  for j in range(m):
    if lab_map[i][j] == 2:
      virus_index.append([i, j])
    elif lab_map[i][j] == 0:
      blank_index.append([i, j])

safety = 0
new_map = [[0] * m for _ in range(n)]
for combi in combinations(blank_index, 3):
  for i in range(n):
    for j in range(m):
      new_map[i][j] = lab_map[i][j]
      if [i, j] in combi:
        new_map[i][j] = 1

  for index in virus_index:
    BFS(new_map, index)

  count = 0
  for i in range(n):
    for j in range(m):
      if new_map[i][j] == 0:
        count += 1
  safety = max(safety, count)

print(safety)