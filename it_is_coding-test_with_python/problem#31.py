import sys

rep = int(sys.stdin.readline().rstrip())
answer = []
for _ in range(rep):
  n, m = map(int, sys.stdin.readline().rstrip().split())
  data = list(map(int, sys.stdin.readline().rstrip().split()))
  bank = [[data[i + 4 * j] for i in range(m)] for j in range(n)]
  result = bank.copy()

  for i in range(1, m):
    for j in range(n):
      if j == 0:
        result[j][i] += max(result[j][i - 1], result[j + 1][i - 1])
      elif j == n - 1:
        result[j][i] += max(result[j - 1][i - 1], result[j][i - 1])
      else:
        result[j][i] += max(result[j - 1][i - 1], result[j][i - 1], result[j + 1][i - 1])
 
  answer.append(max([result[i][m - 1] for i in range(n)]))

for a in answer:
  print(a)