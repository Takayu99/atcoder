import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right
import heapq
import sys
sys.setrecursionlimit(10 ** 6)

n, d = map(int, input().split())

ans = 0
half = math.ceil(d / 2)
for mid in range(half, d):
    for i in range(n - mid):
        ans += 2 ** mid




