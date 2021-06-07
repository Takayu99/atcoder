# from collections import deque
# n, m = map(int, input().split())
# g = [[] for _ in range(n)]

# for i in range(m):
#     a, b = map(int, input().split())
#     g[a - 1].append(b - 1)

# fr = [set() for _ in range(n)]
# seen = [False] * n

# for i in range(n):
#     # if not fr[i]:
#     goto = deque()
#     goto.append(i)
#     fr[i].add(i)
#     while(goto):
#         v = goto.pop()
#         for nv in g[v]:
#             for f in fr[i]:
#                 fr[nv].add(f)
#                 if not seen[nv]:
#                     seen[nv] = True
#                     goto.append(nv)

# ans = 0
# for f in fr:
#     ans += len(f)
# print(ans)       
# print(fr)         


from collections import deque
n, m = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)

seen = [False] * n
ans = []

def dfs(fr, v):
    seen[v] = True
    ans.append(v)
    for next in g[v]:
        if seen[next]:
            continue
        else:
            dfs(g, next)

for i in range(n):
    dfs([], 0)
print(ans)