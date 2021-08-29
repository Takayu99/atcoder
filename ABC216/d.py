import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right
import heapq
import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
a = []
for i in range(m):
    k = int(input())
    x = list(map(int, input().split()))
    a.append(x[::-1])

# n = 4
# m = 5
# a = [[1, 2, 3], [4, 2, 1], [4, 3], [], []]
# a = [[3, 2, 1], [2, 1, 4], [4, 3]]
flag = [False] * m
f = False

dp = [-1] * (n + 1)
todo = deque()
for i in range(m):
    todo.append(i)
# todo.append(0)

while(todo):
#     print("todo: ", todo)
    v = todo.popleft()
    if not a[v]:
        flag[v] = True
        continue
    color = a[v][-1]
    if dp[color] == -1:
        dp[color] = v
    else:
        tmp = dp[color]
#         print("pop!")
#         print("a: ", a)
#         print("dp: ", dp)
#         print("v: ", v)
#         print("tmp: ", tmp)
        
        a[tmp].pop()
        a[v].pop()
        todo.append(v)
        todo.append(tmp)
        if not a[tmp]:
            flag[tmp] = True
        if not a[v]:
            flag[v] = True
    
    if all(flag):
        f = True
        break
        
if f:
    print("Yes")
else:
    print("No")
    
#     print("todo: ", todo)
#     print("a: ", a)
#     print("dp: ", dp)

