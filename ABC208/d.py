from collections import deque
import queue

G = [{}]

def setNode(n):
  global G
  G = [{} for i in range(n)]
def addEdge(s,t,w):
  global G
  G[s][t]=w
def solve(s,t,k):
  global G
  fixed = {}
  q = queue.PriorityQueue()
  q.put((0,s))
  while q.empty() == False:
    w,x = q.get()
    if x == t: return w
    if x in fixed: continue
    fixed[x] = w
    for y in G[x]:
      if (y in fixed) == False:
        if y <= k or y == s or y == t:
            q.put((w + G[x][y], y))
  return 0


n,m = map(int,input().split())
setNode(n)
for i in range(m):
  s,t,w = map(int,input().split())
  s -= 1
  t -= 1
  G[s][t] = w
#   G[t][s] = w
# src, dst = 0, 1
# print(solve(src,dst))
dp1 = [[[] for _ in range(n)] for _ in range(n)]
dp2 = [[-1] * n for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            ans += solve(i, j, k)
            # print(ans)
print(ans)
# print(G)
dp2[1][1] = 0
dp1[1][1].append()
print(dp1)
print(dp2)