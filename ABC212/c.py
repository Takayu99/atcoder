import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
i = 0
j = 0
ans = abs(a[0] - b[0])
while(True):
    ans = min(ans, abs(a[i] - b[j]))
    if i + 1 == n and j + 1 == m:
        break
    elif j + 1 >= m:
        i += 1
    elif i + 1 >= n:
        j += 1
    elif a[i] >= b[j]:
        j += 1
    else:
        i += 1


print(ans)

