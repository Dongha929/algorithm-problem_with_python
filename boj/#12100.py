N = int(input())
B = [list(map(int, input().split())) for _ in range(N)]
def move(x, y, d):
  pass
def UP(N, B):
  for i in range(1, N):
    for j in range(i, 0, -1):
      # j번째 row을 위로 보냄
      for x, y in [[k, j] for k in range(N)]:
        move(x, y, 0)
      pass
def DOWN(N, B):
  for i in range(N - 2, -1, -1):
    for j in range(i, N - 2):
      # j번째 row를 아래로 보냄
      pass
def LEFT(N, B):
  for i in range(1, N):
    for j in range(i, 0, -1):
      # j번째 col을 왼쪽으로 보냄
      pass
def RIGHT(N, B):
  for i in range(N - 2, -1, -1):
    for j in range(i, N - 2):
      # j번째 col를 오른쪽로 보냄
      pass
