 def solution(N, stages):
    up = [[i, 0] for i in range(N + 2)]
    for stage in stages:
        up[stage][1] += 1
    up = up[1 : -1]
 
    plus = 0
    for i in range(len(up)):
        prev = up[i][1]
        if plus == len(stages):
          up[i][1] = 0
        else:
          up[i][1] = up[i][1] / (len(stages) - plus)
        plus += prev
 
    up.sort(key = lambda x: -x[1])
    result = [u[0] for u in up]
 
    return result