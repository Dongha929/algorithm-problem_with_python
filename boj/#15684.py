import sys
from collections import deque

input = sys.stdin.readline
answer = 1e9
N, M, H = map(int, input().split())
lines = [[] for _ in range(H+1)]
for _ in range(M):
  h, n = map(int, input().split())
  lines[h].append(n)
std = [x for x in range(N+1)]

def cal_result(lines):
  result = std[:]
  for i in range(1, H+1):
    for x in lines[i]:
      result[x], result[x+1] = result[x+1], result[x]
  return (result == std)

def cal_case(lines):
  result = []
  for i in range(1, H+1):
    for j in range(1, N):
      if j not in lines[i] and j + 1 not in lines[i] and j - 1 not in lines[i]:
        result.append((i, j))
  return result

# visited가 너무 크다
visited = set()
def BFS(q):
  global answer
  while q:
    case = q.popleft()
    if len(case) == 4 or len(case) >= answer:
      break
    nlines = [x[:] for x in lines]
    for ele in case:
      h, n = ele
      nlines[h].append(n)
    if cal_result(nlines):
      answer = min(answer, len(case))
    else:
      for next in cal_case(nlines):
        ncase = case.copy()
        ncase.add(next)
        if ncase in visited:
          continue
        else:
          visited.add(frozenset(ncase))
          q.append(ncase)

q = deque([])
a = set()
q.append(a)
BFS(q)
print(answer if answer != 1e9 else -1)
