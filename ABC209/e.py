import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect_left, bisect_right, bisect


def binary_search(array, item):
   head = 0
   tail = len(array) - 1

   while head <= tail:
       center = (head + tail) // 2
       if array[center] == item:
           return center
       elif array[center] < item:
           head = center + 1
       else:
           tail = center - 1

   return None

n = int(input())
s = []
for i in range(n):
    s.append(input())

s.sort()
f = []
b = []
for c in s:
    f.append(c[:3])
    b.append(c[-3:])

G = [[] for _ in range(n)]
for i in range(n):
    v = []
    index = binary_search(f, b[i])
    if index == None:
        continue
    v.append(index)
    tmp = index
    while(True):
        tmp += 1
        if tmp >= n:
            break
        if f[tmp] == b[i]:
            v.append(tmp)
        else:
            break
    tmp = index
    while(True):
        tmp -= 1
        if tmp < 0:
            break
        if f[tmp] == b[i]:
            v.append(tmp)
        else:
            break
    
    for nv in v:
        G[i].append(nv)

print(G)

dp = [-1] * n

    

