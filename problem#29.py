from bisect import bisect_left
import sys

n, c = list(map(int, sys.stdin.readline().rstrip().split()))
homes = []
for _ in range(n):
  homes.append(int(sys.stdin.readline().rstrip()))
homes.sort()

def cal_check(dis):
  count = 0
  index = 0
  while index != len(homes):
    count += 1
    if count == c:
      return True
    index = bisect_left(homes, homes[index] + dis)
  return False  

start = 1
end = homes[-1] - homes[0]
result = 0
while (start <= end):
  mid = (end + start) // 2
  if not cal_check(mid):
    end = mid - 1
  else:
    start = mid + 1
    result = mid
  
print(result)