
"""
H, W, N, M = map(int, input().split())

ab = [list(map(int, input().split())) for _ in range(N)]
cd = [list(map(int, input().split())) for _ in range(M)]

dp = [[0] * (W + 1) for _ in range(H + 1)]

for c in cd:
    dp[c[0]][c[1]] = -1

for a in ab:
    dp[a[0]][a[1]] = 1

for i in range(H):
    for j in range(W):
        if dp[i][j] == 0:

print(dp)
"""



# 一方向のみ(dの方向のみ)を探索する.
# 探索を止める条件は, ブロックもしくは電球に到達した時. 
def dfs(i, j, d):  
    global H, W
    di, dj = direction[d]
    ni = i + di
    nj = j + dj
    if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == '.':
        path[ni][nj] = 1
        dfs(ni, nj, d)


H, W, N, M = map(int, input().split())

grid = [['.'] * W for _ in range(H)]  # grid[i][j]: i行目j列目のマス. '.': 空き, 'L': 電球, 'B': ブロック
path = [[0] * W for _ in range(H)]  # path[i][j]: i行目j列目のマスに光が届いているかどうか.

# Light
for i in range(N):
    h, w = map(int, input().split())
    h -= 1; w -= 1
    grid[h][w] = 'L'
# Block
for i in range(M):
    C, D = map(int, input().split())
    grid[C - 1][D - 1] = 'B'


direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'L':  # 電球が置かれている地点から探索を開始
            path[i][j] = 1
            for d in range(4):  # 4方向を探索する
                dfs(i, j, d)

cnt = 0
for l in path:
    cnt += sum(l)

print(cnt)
