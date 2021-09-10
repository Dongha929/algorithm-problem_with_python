from collections import deque
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
lab = []
for _ in range(n):
    lab.append(list(map(int, sys.stdin.readline().rstrip().split())))
x_array = [0, 0, -1, 1]
y_array = [-1, 1, 0, 0]
virus = []

# 초기 설정함수
def init_func(lab):
    for i in range(n):
        for j in range(n):
            if lab[i][j] == 2:
                lab[i][j] = '*'
                virus.append([i, j])
            elif lab[i][j] == 1:
                lab[i][j] = '-'
            else:
                lab[i][j] = -1

# 바이러스 하나가 주어졌을때 상하좌우로 퍼지게 하는 함수
def spread(lab, pos_x, pos_y):
    q = deque([[pos_x, pos_y]])
    lab[pos_x][pos_y] = 0
    while q:
        now = q.popleft()
        for i in range(4):
            nx = now[0] + x_array[i]
            ny = now[1] + y_array[i]
            value = lab[now[0]][now[1]]
            if nx < 0 or nx >= n or ny >= n or ny < 0:
                continue
            if type(lab[nx][ny]) == int:
                if lab[nx][ny] == -1 or lab[nx][ny] > (value + 1):
                    lab[nx][ny] = value + 1
                    q.append([nx, ny])
               
            
# 1가지 바이러스 경우에 걸리는 시간을 계산
# def one_case(virus_pos): 
init_func(lab)
for v in virus:
    spread(lab, v[0], v[1])
for p in lab:
    print(p)
