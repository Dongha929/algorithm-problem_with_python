n = int(input())
q = [1] * n
i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5
for l in range(1, n):
  q[l] = min(next2, next3, next5)
  if q[l] == next2:
    i2 += 1
    next2 = q[i2] * 2
  if q[l] == next3:
    i3 += 1
    next3 = q[i3] * 3
  if q[l] == next5:
    i5 += 1
    next5 = q[i5] * 5

print(q[n - 1])