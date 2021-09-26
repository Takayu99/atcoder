import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right
import heapq
import sys
sys.setrecursionlimit(10 ** 6)


k = int(input())
a, b = map(list, input().split())

a = a[::-1]
b = b[::-1]
x = 0
y = 0
for i in range(len(a)):
    x += int(a[i]) * (k ** i)

for i in range(len(b)):
    y += int(b[i]) * (k ** i)

print(x * y)