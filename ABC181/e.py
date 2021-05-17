
"""
N, M = map(int, input().split())

H = list(map(int, input().split()))
W = list(map(int, input().split()))
ans = 10 ** 100
for w in W:
    h = H + [w]
    h.sort()
    tmp = 0
    for i in range((N + 1) // 2):
        tmp += h[2 * i + 1] - h[2 * i]
    ans = min(ans, tmp)

print(ans) 
"""

from itertools import accumulate
from bisect import bisect

N, M = map(int, input().split())
H = sorted([int(x) for x in input().split()])
W = [int(x) for x in input().split()]

# 最初の項からペアを作っていく，最後の項が余る
cumsum1 = list(accumulate([0] + [H[i] - H[i - 1] for i in range(1, N, 2)]))
# 2つ目の項からペアを作っていく，最初の項が余る
cumsum2 = list(accumulate([0] + [H[i] - H[i - 1] for i in range(2, N, 2)]))

ans = 10 ** 18
for w in W:
    i = bisect(H, w)
    if i % 2:
        insert = abs(H[i - 1] - w)
    else:
        insert = abs(H[i] - w)
    res = cumsum1[i // 2] + insert + cumsum2[-1] - cumsum2[i // 2]
    ans = min(ans, res)

print(ans)



