def check(new_lock):
    l = len(new_lock) // 3
    for i in range(l, 2 * l):
        for j in range(l, 2 * l):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    keys = [key, [], [], []]
    for k in range(3):
        for i in range(m):
            keys[k + 1].append([0] * m)
            for j in range(m):
                keys[k + 1][i][j] = keys[k][j][m - i - 1]
    
    new_lock = []
    for i in range(3 * n):
        new_lock.append([0] * (3 * n))
        for j in range(3 * n):
            if i <  2 * n and i >= n and j < 2 * n and j >= n:
                new_lock[i][j] = lock[i - n][j - n]
    
    for k in range(4):
        for i in range(2 * n):
            for j in range(2 * n):
                for x in range(m):
                    for y in range(m):
                        new_lock[i + x][j + y] += keys[k][x][y]

                if check(new_lock):

                    return True
                for x in range(m):
                    for y in range(m):
                        new_lock[i + x][j + y] -= keys[k][x][y]
    return False