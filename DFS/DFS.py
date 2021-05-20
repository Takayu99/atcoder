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
"""
from collections import deque

n, m = map(int, input().split())

G = [[] for _ in range(n)] #グラフの隣接リスト表現

for i in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

"""
スタックを使用したDFS
root = 0
seen = [False] * n
todo = deque([])
todo.append(root)
seen[root] = True
ans = []

while (todo):
    v = todo.pop()
    ans.append(v)
    for w in G[v]:
        if seen[w] == True:
            continue
        else:
            seen[w] = True
            todo.append(w)

print(ans)
"""


#再帰関数を使用したDFS
seen = [False] * n
ans = []
def dfs(g, v):
    seen[v] = True
    ans.append(v)
    for next in g[v]:
        if seen[next]:
            continue
        else:
            dfs(g, next)

dfs(G, 0)
print(ans)

