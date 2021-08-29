import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right
import heapq
import sys
sys.setrecursionlimit(10 ** 6)


n = int(input())
s = []
t = []
for i in range(n):
    x, y = input().split()
    s.append(x)
    t.append(y)

flag = False
for i in range(n - 1):
    for j in range(i + 1, n):
        if s[i] == s[j]:
            if t[i] == t[j]:
                flag = True
                break

if flag:
    print("Yes")
else:
    print("No")
          
