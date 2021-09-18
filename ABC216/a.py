import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right
import heapq
import sys
sys.setrecursionlimit(10 ** 6)

x, y = map(int, input().split("."))
x  = str(x)
if y <= 2:
    print(x + "-")
elif y <= 6:
    print(x)
else:
    print(x + "+")


