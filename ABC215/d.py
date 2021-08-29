import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right
import heapq
import sys
sys.setrecursionlimit(10 ** 6)


def divisor(n):
    div = []
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            div.append(i)
            div.append(n // i)
    return list(set(div))

n, m = map(int, input().split())
a = list(map(int, input().split()))
div = set()

for s in a:
    tmp = divisor(s)
    for t in tmp:
        div.add(t)

div = sorted(list(div))[1:]
res = [True] * (m + 1)

for d in div:
    for i in range(m // d + 1):
        res[d * i] = False

ans = []
for i in range(1, m + 1):
    if res[i]:
        ans.append(i)

print(len(ans))
for i in ans:
    print(i)