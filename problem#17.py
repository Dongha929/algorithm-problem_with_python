from collections import deque

direction = [[-1, 1, 0, 0], [0, 0, -1, 1]]
n, k = map(int, input().split())
lab = []
for i in range(n):
  lab.append(list(map(int, input().split())))
position = [0, 0]
answer_time, position[0], position[1] = map(int, input().split())

q_list = [deque() for _ in range(k + 1)]
for i in range(n):
  for j in range(n):
    if lab[i][j] != 0:
      q_list[lab[i][j]].append([i, j])

def BFS(lab, queue_list):
  for num in range(1, k + 1):
    temp_list = []
    while q_list[num]:
      now = q_list[num].popleft()
      for i in range(4):
        dx = now[0] + direction[0][i]
        dy = now[1] + direction[1][i]
        if dx < 0 or dy < 0 or dx >= n or dy >= n:
          continue
        if lab[dx][dy] == 0:
          lab[dx][dy] = num
          temp_list.append([dx, dy])
    for pos in temp_list:
      q_list[num].append(pos)

for t in range(answer_time):
  BFS(lab, q_list)

print(lab[position[0] - 1][position[1] - 1])