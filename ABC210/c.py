import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right

n, k = map(int, input().split())
c = list(map(int, input().split()))
ans = 0
for i in range(n - k + 1):
    s = set(c[i:i + k])
    ans = max(ans, len(s))

print(ans)






