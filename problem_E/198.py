from sys import setrecursionlimit
from collections import Counter
setrecursionlimit(100000)

n = int(input())
c = list(map(int, input().split()))

G = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

seen = [False] * n
color = Counter()
ans = []

def dfs(v):
    seen[v] = True
    if color[c[v]] == 0:
        ans.append(v)
    color[c[v]] += 1
    for next in G[v]:
        if seen[next]:
            continue
        else:
            dfs(next)
    color[c[v]] -= 1
    

dfs(0)

ans.sort()
for a in ans:
    print(a + 1)