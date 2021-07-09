import math
from collections import deque, Counter
from itertools import product, combinations, permutations

n = int(input())
a = list(map(int, input().split()))

g = [[] for _ in range(n + 1)]
for i in range(n // 2):
    g[a[i]].append(a[n - 1 - 1])
    g[a[n - 1 - i]].append(a[i])

seen = [False] * (n + 1)
goto = deque()
ans = 1

for i in range(1, n + 1):
    if seen[i]:
        continue
    seen[i] = True
    goto.append(i)
    while(goto):
        v = goto.popleft()
        for nv in g[v]:
            if seen[nv]:
                continue
            else:
                goto.append(nv)
        

