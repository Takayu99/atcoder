import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right
import heapq
import sys
sys.setrecursionlimit(10 ** 6)

n= int(input())

G = [[] for _ in range(n + 1)] 

for i in range(n - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


def dfs(u, p):
    ans.append(u)
    for v in G[u]:
        if v != p:
            dfs(v, u)
            ans.append(u)

for i in range(n + 1):
    G[i].sort()

ans = []
dfs(1, -1)
for a in ans:
    print(a, end=" ")
