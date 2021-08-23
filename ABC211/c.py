
s = list(input())
n = len(s)

dp = [[0] * 9 for _ in range(n + 1)]
t = list("chokudai")
dp[0][0] = 1

for i in range(n):
    for j in range(1, 9):
        if s[i] != t[j - 1]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = dp[i][j] + dp[i][j - 1]

print(dp[-1][-1])