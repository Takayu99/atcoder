#二部グラフ判定

from collections import deque

n, m = map(int, input().split())

G = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    # a -= 1
    # b -= 1
    G[a].append(b)
    G[b].append(a)

is_bipartite = True
dist = [-1] * n
que = deque()

for v in range(n):
    if dist[v] != -1:
        continue
    dist[v] = 0
    que.append(v)
    while(que):
        v = que.popleft()
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                que.append(nv)
            else:
                if dist[v] == dist[nv]:
                    is_bipartite = False

if is_bipartite:
    print("Yes")
else:
    print("No")
