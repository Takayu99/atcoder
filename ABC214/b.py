import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right
import heapq
import sys
sys.setrecursionlimit(10 ** 6)

s, t = map(int, input().split())

ans = 0
for i in range(s + 1):
    for j in range(s + 1 - i):
        for k in range(s + 1 - i - j):
            if i * j * k <= t:
                ans += 1

print(ans)
