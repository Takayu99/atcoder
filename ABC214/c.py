import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right
import heapq
import sys
sys.setrecursionlimit(10 ** 6)


INF = 10 ** 9
n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

ans = [INF] * n
ans[0] = t[0]

for i in range(2 * n):
    ans[(i + 1) % n] = min(ans[i % n] + s[i % n], t[(i + 1) % n])

for a in ans:
    print(a)



