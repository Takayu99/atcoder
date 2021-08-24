import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right
import heapq
import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
if n <= 125:
    print(4)
elif n <= 211:
    print(6)
else:
    print(8)