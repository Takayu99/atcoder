#Knapsack2
N, W = map(int, input().split())

wv = [list(map(int, input().split())) for _ in range(N)]

INF = 10 ** 9
V = sum(x[1] for x in wv)

dp = [[0] + [INF] * V for _ in range(N + 1) ]

for i, (w, v) in enumerate(wv):
    for j in range(V + 1):
        if j - v >= 0:
            dp[i + 1][j] = min(dp[i][j], dp[i][j - v] + w)
        else:
            dp[i + 1][j] = min(dp[i][j], w)


ans = V
while True:
    tmp = dp[N].pop()
    if tmp <= W:
        break
    ans -= 1
print(ans)



