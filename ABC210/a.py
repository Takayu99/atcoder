import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right

n, a, x, y = map(int, input().split())
ans = 0
if a <= n:
    ans += a * x
    ans += y * (n - a)
else:
    ans += n * x

print(ans)


