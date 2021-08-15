from itertools import combinations

n, m = map(int, input().split())
city = []
for _ in range(n):
  city.append(list(map(int, input().split())))

homes = []
chickens = []
for i in range(n):
  for j in range(n):
    if city[i][j] == 1:
      homes.append([i, j])
    elif city[i][j] == 2:
      chickens.append([i, j])

def chicken_distance(matrix):
  result = 0
  for home in matrix:
    result += min(home)
  return result

def matrix_maker(hs, cs):
  matrix = []
  iteration = 0
  for h in hs:
    matrix.append([])
    for c in cs:
      dx = h[0] - c[0]
      dy = h[1] - c[1]
      if dx < 0:
        dx *= -1
      if dy < 0:
        dy *= -1
      matrix[iteration].append(dx + dy)
    iteration += 1
  return matrix

cases = list(combinations(chickens, m))
cases_distance = []

if len(chickens) > m:
  for case in cases:
    cases_distance.append(chicken_distance(matrix_maker(homes, case)))
  print(min(cases_distance))  
else:
  print(chicken_distance(matrix_maker(homes, chickens)))