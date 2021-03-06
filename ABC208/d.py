n, m = map(int, input().split())

abc = [list(map(int, input().split())) for _ in range(m)]

INF = 10 ** 18
dp = [[INF] * n for _ in range(n)]

for v in abc:
    dp[v[0] - 1][v[1] - 1] = v[2]
for i in range(n):
    dp[i][i] = 0

ans = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
            if dp[i][j] < INF:
                ans += dp[i][j]

print(ans)


