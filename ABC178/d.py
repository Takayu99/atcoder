s = int(input())
mod = 10 ** 9 + 7
dp = [0] * (s + 1)

for i in range(3, s + 1):
    dp[i] += 1
    for j in range(i - 3, 2, -1):
        dp[i] += dp[j]
        dp[i] %= mod

print(dp[-1])



