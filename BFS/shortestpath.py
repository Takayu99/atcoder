"""
迷路の最短経路問題

入力
8 8
.#....#G
.#.#....
...#.##.
#.##...#
...###.#
.#.....#
...#.#..
S.......
"""


from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

H, W = map(int, input().split())

field = [list(input()) for _ in range(H)]

for h in range(H):
    for w in range(W):
        if field[h][w]  == "S":
            sx = h
            sy = w
        if field[h][w] == "G":
            gx = h
            gy = w


dist = [[-1] * W for _ in range(H)]
dist[sx][sy] = 0
goto = deque()
goto.append([sx, sy])

#探索中に各マスはどのマスから来たのかを表す配列 (最短経路長を知るだけなら、これは不要)
prev_x = [[-1] * W for _ in range(H)]
prev_y = [[-1] * H for _ in range(W)]

while(goto):
    v = goto.popleft()
    x = v[0]
    y = v[1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= H or ny < 0 or ny >= W:
            continue
        if field[nx][ny] == "#":
            continue
        if dist[nx][ny] == -1:
            goto.append([nx, ny])
            dist[nx][ny] = dist[x][y] + 1
            prev_x[nx][ny] = x
            prev_y[nx][ny] = y

#最短経路長の出力
print(dist[gx][gy])

#最短経路の出力
x, y = gx, gy
while(x != -1 and y != -1):
    field[x][y] = "o"
    px = prev_x[x][y]
    py = prev_y[x][y]
    x, y = px, py

for i in range(H):
    for j in range(W):
        print(field[i][j], end = "")
    print()

    
