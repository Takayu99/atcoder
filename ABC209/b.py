import math
from collections import deque, Counter
from itertools import product, combinations, permutations

n, x = map(int, input().split())

a = list(map(int, input().split()))

total = 0
for i, b in enumerate(a):
    if i % 2 == 0:
        total += b
    else:
        total += b - 1

if total <= x:
    print("Yes")
else:
    print("No")
