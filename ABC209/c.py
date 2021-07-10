import math
from collections import deque, Counter
from itertools import product, combinations, permutations

n = int(input())
c = list(map(int, input().split()))
mod = 10 ** 9 + 7

c.sort()
ans = 1
for i in range(n):
    ans *= (c[i] - i)
    ans %= mod

print(ans)