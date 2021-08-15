import sys
from bisect import bisect_left

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.reverse()

dp = [arr[0]]
for i in range(n):
  if arr[i] > dp[-1]:
    dp.append(arr[i])
  else:
    index = bisect_left(dp, arr[i])
    dp[index] = arr[i]

print(n - len(dp))