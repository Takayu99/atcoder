import math
from collections import deque, Counter
from itertools import product, combinations, permutations

n = int(input())
a = list(map(int, input().split()))

s = list(Counter(a).values())
ans = 0
l = len(s)

for i in range(l):
    n -= s[i]
    ans += s[i] * n

print(ans)
