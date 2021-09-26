import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right
import heapq
import sys
sys.setrecursionlimit(10 ** 6)

a, b, c = map(int, input().split())
tmp = c
while(True):
    if a <= c and c <= b:
        print(c)
        exit()
    c += tmp
    if c > 1000:
        print(-1)
        exit()
