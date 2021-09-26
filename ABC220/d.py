import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right
import heapq
import sys
sys.setrecursionlimit(10 ** 6)



n = int(input())
a = list(map(int, input().split()))
tmp = [0] * 10

def egg(v, x):
    ten = [0] * 10
    for i in range(10):
        ten[(i + v) % 10] += x[i]
        ten[(i * v) % 10] += x[i]
    for i in range(10):
        ten[i] %= 998244353 
    return ten

tmp[a[0]] = 1
for i in range(1, n):
    tmp = egg(a[i], tmp)

for a in tmp:
    print(a)

