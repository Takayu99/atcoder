import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right
import heapq
import sys
sys.setrecursionlimit(10 ** 6)


n = int(input())
ans = 0
tmp = 1
while(True):
    tmp *= 2
    if tmp > n:
        break
    ans += 1

print(ans)
    
    
