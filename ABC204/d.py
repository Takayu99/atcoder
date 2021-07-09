import math
n = int(input())
t = list(map(int, input().split()))

s = sum(t)
dp = [[False] * (s + 1) for _ in range(n + 1)]
dp[0][0] = True


for i in range(n):
    for j in range(s):
        if dp[i][j]:
            if j + t[i] > s:
                continue
            dp[i + 1][j] = True
            dp[i + 1][j + t[i]] = True

for i in range(math.ceil(s / 2), s + 1):
    if dp[n][i]:
        print(i)
        exit()


