
def warshall_floyd(n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

n = 4
INF = 10 ** 18
dp = [[INF] * n for _ in range(n)]



