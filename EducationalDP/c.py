#Vacation
n = int(input())

activity = ("A", "B", "C")

abc = [tuple(map(int, input().split())) for i in range(n)]

dp = [abc[0]]

for i in range(1, n):
    a = max(dp[i - 1][1], dp[i - 1][2]) + abc[i][0]
    b = max(dp[i - 1][0], dp[i - 1][2]) + abc[i][1]
    c = max(dp[i - 1][0], dp[i - 1][1]) + abc[i][2]
    dp.append((a, b, c))


print(max(dp[-1]))