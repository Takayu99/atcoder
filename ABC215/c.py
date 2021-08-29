import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right
import heapq
import sys
sys.setrecursionlimit(10 ** 6)


s, k = input().split()
k = int(k)

v = ["".join(p) for p in permutations(s)]
v = set(v)
print(sorted(v)[k - 1])