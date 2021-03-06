import sys

input = sys.stdin.readline
N, M, H = map(int, input().split())
board = [[False] * (N+1) for _ in range(H+1)]
for _ in range(M):
  h, n = map(int, input().split())
  board[h][n] = True
ans = 1e9

def cal_result():
  diff = 0
  for n in range(1, N+1):
    tmp = n
    for i in range(1, H+1):
      if board[i][tmp]:
        tmp += 1
      else:
        if tmp != 1 and board[i][tmp-1]:
          tmp -= 1
    if tmp != n:
      diff += 1
  return diff

def DFS(s, d):
  global ans
  if ans <= d or d == 3:
    return
  for h in range(s, H+1):
    for n in range(1, N):
      if not board[h][n] and not board[h][n+1] and not board[h][n-1]:
        board[h][n] = True
        if cal_result() == 0:
          ans = d + 1
          board[h][n] = False
          return
        else:
          DFS(h, d+1)
          board[h][n] = False

if M == 0:
  ans = 0
elif M == 1:
  ans = 1
else:
  du = cal_result()
  if du == 0:
    ans = 0
  elif du > 6:
    ans = -1
  else:
    DFS(1, 0)
print(ans if ans != 1e9 else -1)
