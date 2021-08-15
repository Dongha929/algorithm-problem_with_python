from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  start, end = map(int, input().split())
  graph[start].append(end)

distance = [-1] * (n + 1)
distance[x] = 0

def BFS(graph, x, distance):
  queue = deque([x])
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if distance[i] == -1:
        queue.append(i)
        distance[i] = distance[v] + 1

BFS(graph, x, distance)

if k not in distance:
  print(-1)
for i in range(1, len(distance)):
  if distance[i] == k:
    print(i)