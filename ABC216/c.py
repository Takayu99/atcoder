import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right
import heapq
import sys
sys.setrecursionlimit(10 ** 6)


n = int(input())
ans = []
while(n >= 1):
    if n % 2 == 1:
        n -= 1
        ans.append("A")
    else:
        n //= 2
        ans.append("B")
print("".join(ans[::-1]))
