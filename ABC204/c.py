from collections import deque
n, m = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)

goto = deque()
ans = 0

for i in range(n):
    seen = [False] * n 
    seen[i] = True
    goto.append(i)
    while(goto):
        v = goto.popleft()
        ans += 1
        for nv in g[v]:
            if not seen[nv]:
                seen[nv] = True
                goto.append(nv)
print(ans)       


