"""
グラフサンプル
sample1
7 6
0 1
1 2
3 6
3 2
4 3
2 5

sample2
15 14
0 1
0 2
0 3
1 4
1 5
2 6
2 7
3 8
3 9
6 10
6 11
7 12
7 13
9 14

sample3
9 13
0 1
0 4
0 2
1 4
1 3
1 8
2 5
3 8
4 8
5 8
5 6
3 7
6 7
"""
"""
#シンプルな実装
from collections import deque

n, m = map(int, input().split())

G = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

seen = [False] * n
goto = deque()
root = 0

goto.append(root)
seen[root] = True
ans = []

while(goto):
    v = goto.popleft()
    for next in G[v]:
        if seen[next]:
            continue
        else:
            goto.append(next)
            seen[next] = True
    ans.append(v)

print(ans)
"""

#始点からの距離distを求めながら実装する方法
from collections import deque

n, m = map(int, input().split())

G = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dist = [-1] * n
goto = deque()
root = 0

dist[root] = 0
goto.append(root)

while(goto):
    v = goto.popleft()
    for next in G[v]:
        if dist[next] != -1:
            continue
        else:
            dist[next] = dist[v] + 1
            goto.append(next)

for i in range(n):
    print(i, ":", dist[i])