"""
グラフサンプル

sample1
8 12
4 1
4 6
4 2
2 7
6 7
1 3
2 7
3 7
3 0
7 0
2 5
0 5
"""


#トポロジカルソート
from collections import deque

n, m = map(int, input().split())
G = [[] for _ in range(n)]
deg = [0] * n  #各頂点の出次数

for i in range(m):
    a, b = map(int, input().split())
    G[b].append(a)  #逆向きに辺を張る
    deg[a] += 1

que = deque()

#出次数が0の頂点をキューに入れる
for i in range(n):
    if deg[i] == 0:
        que.append(i)

order = []
while(que):
    v = que.popleft()
    order.append(v)
    for nv in G[v]:
        deg[nv] -= 1
        if deg[nv] == 0:
            que.append(nv)

print(order[::-1])


