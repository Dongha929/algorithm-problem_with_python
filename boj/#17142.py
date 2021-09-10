from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lab = []
for _ in range(n):
    lab.append(list(map(int, input().split())))
x_array = [0, 0, -1, 1]
y_array = [-1, 1, 0, 0]
virus = []

for i in range(n):
  for j in range(n):
    if lab[i][j] == 2:
      virus.append([i, j])

def spread(q, v, d):
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            nx = now_x + x_array[i]
            ny = now_y + y_array[i]
            if nx < 0 or nx >= n or ny >= n or ny < 0:
              continue
            if lab[nx][ny] != 1 and v[nx][ny] == 0:
              v[nx][ny] = 1
              d[nx][ny] = d[now_x][now_y] + 1
              q.append([nx, ny])
            
answer = 1e9 
for case in combinations(virus, m):
  visited = [[0] * n for _ in range(n)]
  distance = [[-1] * n for _ in range(n)]
  q = deque()
  for x, y in case:
    visited[x][y] = 1
    distance[x][y] = 0
    q.append([x, y])

  spread(q, visited, distance)

  c = 0
  for i in range(n):
    for j in range(n):
      if visited[i][j] == 0 and lab[i][j] == 0:
        c += 1
  if c == 0:
    max_num = 0
    for i in range(n):
      for j in range(n):
        if [i, j] not in virus:
          max_num = max(distance[i][j], max_num)
    answer = min(answer, max_num)

print(answer if answer != 1e9 else -1)
# 논쟁의 핵심은  
# 1. 바이러스가 옆칸에 있더라도 거리를 추가한다
# 바이러스가 활성화되지 않은 바이러스 칸으로 가야 활성화됨 즉, 가는데 걸리는 시간 존재
# 2. 최종 거리에서 바이러스를 포함하지 않는다
# 활성화되지 않은 바이러스라도 바이러스라서 문제 조건인 모든 칸을 바이러스로 채우는데 영향을 주지않음
