#To 3

from itertools import product

n = list(input())
a = [int(x) for x in n]
k = len(n)
ans = k

for bits in product((True, False), repeat = k):
    tmp = 0
    score = 0
    for i, bit in enumerate(bits):
        if bit:
            tmp += a[i]
        else:
            score += 1
    if tmp % 3 == 0:
        ans = min(ans, score)

if ans == k:
    print(-1)
else:
    print(ans)

