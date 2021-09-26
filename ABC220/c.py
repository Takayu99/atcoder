import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right
import heapq
import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
a = list(map(int, input().split()))
x = int(input())

b = [0] * (n + 1)
for i in range(n):
    b[i + 1] = b[i] + a[i]

k = n * (x // b[-1])
tmp = x % b[-1]

for i in range(n):
    if tmp < b[i]:
        break
    else:
        k += 1

print(k)

