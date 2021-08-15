n = int(input())
a_list = list(map(int, input().split()))
counts = list(map(int, input().split()))

max_value = -1e9
min_value = 1e9
def DFS(i, value):
  global max_value, min_value
  if i == n - 1:
    max_value = max(max_value, value)
    min_value = min(min_value, value)
  else:
    if counts[0] > 0:
      counts[0] -= 1
      DFS(i + 1, value + a_list[i + 1])
      counts[0] += 1
    if counts[1] > 0:
      counts[1] -= 1
      DFS(i + 1, value - a_list[i + 1])
      counts[1] += 1
    if counts[2] > 0:
      counts[2] -= 1
      DFS(i + 1, value * a_list[i + 1])
      counts[2] += 1
    if counts[3] > 0:
      counts[3] -= 1
      DFS(i + 1, int(value / a_list[i + 1]))
      counts[3] += 1

DFS(0, a_list[0])

print(max_value)
print(min_value)