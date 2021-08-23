import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right

n, k = map(int, input().split())
c = list(map(int, input().split()))

cnt = Counter(c[0 : k])
ans = len(cnt)

for i in range(k, n):
    cnt[c[i - k]] -= 1
    cnt[c[i]] += 1
    if cnt[c[i - k]] == 0:
        del cnt[c[i - k]]
    ans = max(ans, len(cnt))

print(ans)






