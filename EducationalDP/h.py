#Grid1

H, W = map(int, input().split())

s = [input() for _ in range(H)]

dp = [[0] * W for _ in range(H)]
dp[0][0] = 1

for i in range(1, W):
    if s[0][i] == ".":
        dp[0][i] = 1
    else:
        break

for i in range(1, H):
    if s[i][0] == ".":
        dp[i][0] = 1
    else:
        break

for i in range(1, H):
    for j in range(1, W):
        if s[i][j] == ".":
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        else:
            dp[i][j] = 0

print(dp[H - 1][W - 1] % (10 ** 9 + 7))




