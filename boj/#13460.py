# q = [[red], [blue], iteration]
pos = [-1, 1, -1, 1]
result = -1
def BFS():
  while q:
    now_red, now_blue, count = q.popleft()
    for i in range(4):
      temp_red, temp_blue = cal_pos(now_red, now_blue, i)
      if temp_blue != [-1, -1]:
        if temp_red != [-1, -1]:
          q.append([temp_red, temp_blue, count + 1])
        else:
          result = count + 1
          break

def return_ball_xpos(x_ball, y_ball, dir):
  for _ in range(n):
    temp_x = x_ball + pos[dir]
    if board[temp_x][y_ball] == '#':
      return [x_ball, y_ball]
    elif board[temp_x][y_ball] == 'O':
      return [-1, -1]
    else:
      x_ball = temp_x

# dir에 따라 b1의 위치를 계산해주는 함수 
def cal_pos(b1, b2, dir):
  x_b1, y_b1 = b1
  x_b2, y_b2 = b2
  if dir == 0 or dir == 1:
    if y_b1 != y_b2:
      return [return_ball_xpos(x_b1, y_b1, dir), return_ball_xpos(x_b2, y_b2, dir)]
    

  
