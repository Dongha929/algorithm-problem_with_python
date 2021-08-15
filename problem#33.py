import sys

n = int(sys.stdin.readline().rstrip())
data = []
for _ in range(n):
  data.append(list(map(int, sys.stdin.readline().rstrip().split())))

result = [0] * n
if data[n - 1][0] == 1:
  result[n - 1] = data[n - 1][1]
for i in range(n - 2, -1, -1):
  t = data[i][0]
  if i + t < n:
    result[i] = max(result[i + 1], result[i + t] + data[i][1])
  elif i + t == n:
    result[i] = max(result[i + 1], data[i][1])
  else:
    result[i] = result[i + 1]

print(result[0])