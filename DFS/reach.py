#頂点sから頂点tにたどり着けるか
"""
単純にsを始点としたDFSを行い，DFS実施後にseen配列を見ることで各頂点が探索されたかがわかる．
特にseen[t]を見ることで頂点tに到達しているかがわかる
"""

#グリッドグラフの場合
"""
10 10
s.........
#########.
#.......#.
#..####.#.
##....#.#.
#####.#.#.
g.#.#.#.#.
#.#.#.#.#.
#.#.#.#.#.
#.....#...
"""
def dfs(h, w):
    seen[h][w] = True
    for dir in range(4):
        nh = h + dy[dir]
        nw = w + dx[dir]
        if nh < 0 or nh >= H or nw < 0 or nw >= W:
            continue
        if field[nh][nw] == "#":
            continue
        if seen[nh][nw]:
            continue

        dfs(nh, nw)



dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

H, W = map(int, input().split())
field = [input() for _ in range(H)]

seen = [[False] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if field[i][j] == "s":
            sh = i
            sw = j
        if field[i][j] == "g":
            gh = i
            gw = j

dfs(sh, sw)

if seen[gh][gw]:
    print("Yes")
else:
    print("No")