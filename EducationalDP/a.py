n = int(input())
h = list(map(int, input().split()))


if n == 2:
    print(abs(h[1] - h[0]))
    exit()


dp = [0]

dp.append(abs(h[1] - h[0]) + dp[0])

for i in range(2, n):
    dp.append(min(abs(h[i] - h[i - 1]) + dp[i - 1], abs(h[i] - h[i - 2]) + dp[i - 2]))

print(dp.pop())