import math

n, k = map(int, input().split())

lr = [list(map(int, input().split())) for _ in range(k)]
step = set()

for l, r in lr:
    for i in range(l, r + 1):
        step.add(i)


dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    for s in step:
        if i + s > n:
            continue
        elif i + s == n:
            dp[i] += 1
        else:
            dp[i] += dp[i + s]
    dp[i] %= 998244353

print(dp[1])
    





