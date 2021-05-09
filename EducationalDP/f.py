#LCS（最長共通部分系列問題）
s = input()
t = input()

ans = []
x = len(s)
y = len(t)

dp = [[0] * (y + 1) for _ in range(x + 1)]

for i in range(1, x + 1):
    for j in range(1, y + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        
# print(dp[-1][-1])

ans = []
i, j = x, y
while(i >= 1 and j >= 1):
    if dp[i - 1][j] == dp[i][j]:
        i -= 1
    elif dp[i][j - 1] == dp[i][j]:
        j -= 1
    else:
        i -= 1
        j -= 1
        ans.append(s[i])

print("".join(ans[::-1]))


