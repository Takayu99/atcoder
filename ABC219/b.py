import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right
import heapq
import sys
sys.setrecursionlimit(10 ** 6)

s1 = input()
s2 = input()
s3 = input()
t = list(input())
ans = ""

for c in t:
    if c == "1":
        ans += s1
    elif c == "2":
        ans += s2
    elif c == "3":
        ans += s3

print(ans)


