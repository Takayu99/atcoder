n, k = map(int, input().split())

h = list(map(int, input().split()))


dp = [0]

for i in range(n):
    tmp = 10000
    for j in range(1, k):
        if i - j >= 0:
            tmp = min(abs(h[i] - h[i - j]) + dp[i - j], tmp)
    dp.append(tmp)



