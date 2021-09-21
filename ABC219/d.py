import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right
import heapq
import sys
sys.setrecursionlimit(10 ** 6)


n = int(input())
x, y = map(int, input().split())
ab = []
for i in range(n):
    ab.append(list(map(int, input().split())))

dp = [[-1] * n for _ in range(n)]


