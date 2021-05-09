#Queen on Grid

"""
H, W = map(int, input().split())

s = [input() for _ in range(H)]

dp = [[0] * W for _ in range(H)]

dp[0][0] = 1

for i in range(H):
    for j in range(W):
        for k in range(1, W - j):
            if s[i][j + k] == ".":
                dp[i][j + k] += dp[i][j]
            else:
                break
        for k in range(1, H - i):
            if s[i + k][j] == ".":
                dp[i + k][j] += dp[i][j]
            else:
                break
        for k in range(1, min(W - j, H - i)):
            if s[i + k][j + k] == ".":
                dp[i + k][j + k] += dp[i][j]
            else:
                break
        
print(dp[-1][-1] % (10 ** 9 + 7))
"""


H, W = map(int, input().split())

s = [input() for _ in range(H)]

dp = [[0] * (W + 1) for _ in range(H + 1)]
x = [[0] * (W + 1) for _ in range(H + 1)]
y = [[0] * (W + 1) for _ in range(H + 1)]
z = [[0] * (W + 1) for _ in range(H + 1)]

mod = 10 ** 9 + 7

dp[1][1] = 1


for i in range(1, H + 1):
    for j in range(1, W + 1):
        if i == 1 and j == 1:
            continue
        if s[i - 1][j - 1] == ".":
            # x[i][j] = (x[i][j - 1] + dp[i][j - 1]) 
            # y[i][j] = (y[i - 1][j] + dp[i - 1][j])
            # z[i][j] = (z[i - 1][j - 1] + dp[i - 1][j - 1])
            # dp[i][j] = (x[i][j] + y[i][j] + z[i][j])
            x[i][j] = (x[i][j - 1] + dp[i][j - 1]) % mod 
            y[i][j] = (y[i - 1][j] + dp[i - 1][j]) % mod
            z[i][j] = (z[i - 1][j - 1] + dp[i - 1][j - 1]) % mod
            dp[i][j] = (x[i][j] + y[i][j] + z[i][j]) % mod
        
# print(dp[-1][-1] % (10 ** 9 + 7))
print(dp[-1][-1])




