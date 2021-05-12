#Patisserie ABC2

"""
n, k = map(int, input().split())

dp = [[0] * (n * 3 + 5) for _ in range(4)]
dp[0][0] = 1

for i in range(3):
    for j in range(i * n + 1):
        dp[i + 1][j + 1] += dp[i][j]
        dp[i + 1][j + n + 1] -= dp[i][j]
    
    for j in range(1, (i + 1) * n + 1):
        dp[i + 1][j] += dp[i + 1][j - 1]

print(dp)

for i in range(3, 3 * n + 1):
    if k <= dp[3][i]:
        x = i
        break
    else:
        k -= dp[3][i]
    
for i in range(1, n + 1):
    jmi = max(1, x - i - n)
    jma = min(n, x - i - 1)
    if jmi > jma:
        continue
    if k > jma - jmi + 1:
        k -= jma - jmi + 1
        continue

    y = jmi + k - 1
    z = x - i - y
    print(i, y, z)
    exit()
"""

n = 3

dp = [[0] * (3 * n + 1) for _ in range(4)]
dp[0][0] = 1

for i in range(3):
    for j in range(i, i * n + 1):
        for k in range(n):
            dp[i + 1][j + k + 1] += dp[i][j]

print(dp)
