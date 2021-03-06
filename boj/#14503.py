import sys
n, m = list(map(int, sys.stdin.readline().rstrip().split()))
now_x, now_y, now_dir = list(map(int, sys.stdin.readline().rstrip().split()))
if now_dir % 2 == 1:
    now_dir = (now_dir + 2) % 4
room = []
for _ in range(n):
    room.append(list(map(int, sys.stdin.readline().rstrip().split())))

x_direction = [-1, 0, 1, 0]
y_direction = [0, -1, 0, 1]

if room[now_x][now_y] == 1:
    print(0)
else:
    result = 1
    room[now_x][now_y] = 2

    while 1:
        count = 0
        for _ in range(4):
            temp_dir = (now_dir + 1) % 4
            next_x = now_x + x_direction[temp_dir]
            next_y = now_y + y_direction[temp_dir]
            if room[next_x][next_y] == 0:
                now_dir = temp_dir
                now_x = next_x
                now_y = next_y
                room[now_x][now_y] = 2
                result += 1
                break
            else:
                now_dir = temp_dir
                count += 1

        if count == 4:
            next_x = now_x - x_direction[now_dir]
            next_y = now_y - y_direction[now_dir]
            if room[next_x][next_y] != 1:
                now_x = next_x
                now_y = next_y
            else:
                break

    print(result)
