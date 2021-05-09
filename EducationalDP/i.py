#Coins

N = int(input())
p = list(map(float, input().split()))

dp =[[0] * (N + 1) for _ in range(N)]

dp[0][0] = 1 - p[0]
dp[0][1] = p[0]

for i in range(N - 1):
    for j in range(N):
        dp[i + 1][j] += dp[i][j] * (1 - p[i + 1])
        dp[i + 1][j + 1] += dp[i][j] * p[i + 1]

print(sum(dp[-1][N // 2 + 1:]))