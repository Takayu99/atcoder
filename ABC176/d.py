"""
from collections import deque

H, W = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
sx -= 1
sy -= 1
gx -= 1
gy -= 1

field = [list(input()) for _ in range(H)]

s = [[-1] * W for _ in range(W)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
wx = [1, 1, -1, -1, 2, 2, 2, 2, 2, 1, 0, -1, -2, -2, -2, -2, -2, -1, 0, 1]
wy = [1, -1, -1, 1, 2, 1, 0, -1, -2, -2, -2, -2, -2, -1, 0, 1, 2, 2, 2, 2]

ans = -1
goto = deque()
warp = deque()
warp.append([sx, sy])
s[sx][sy] = 0

while(warp):
    sx, sy = warp.popleft()
    # if s[sx][sy] != ans + 1:
    #     continue
    ans = s[sx][sy]
    goto.append([sx, sy])
    while(goto):
        x, y = goto.popleft()
        for i in range(20):
            nx = x + wx[i]
            ny = y + wy[i]
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if field[nx][ny] != "#" and s[nx][ny] == -1:
                s[nx][ny] = ans + 1
                warp.append([nx, ny])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if field[nx][ny] != "#" and s[nx][ny] != ans:
                s[nx][ny] = ans
                goto.append([nx, ny])

    
print(s[gx][gy])
"""

from collections import deque

H, W = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())

s = [list(input()) for _ in range(H)]

d = [[-1] * W for _ in range(H)]
que = deque()
que.append([sx - 1, sy - 1, 0])

while(que):
    x, y, cnt = que.popleft()
    if d[x][y] != -1:
        continue
    d[x][y] = cnt

    for i in range(-2, 3):
        for j in range(-2, 3):
            nx = x + i
            ny = y + j
            if 0 <= nx < H and 0 <= ny < W and s[nx][ny] != "#":
                if abs(i) + abs(j) == 1:
                    que.appendleft([nx, ny, cnt])
                elif abs(i) + abs(j) >= 2:
                    que.append([nx, ny, cnt + 1])

print(d[gx - 1][gy - 1])





