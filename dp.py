w = [75, 70, 90, 60, 120, 125, 185, 205, 175, 270, 315]
v = [7, 6, 10, 10, 22, 17, 23, 27, 20, 33, 36]

N = 11
W = 500



# #シンプルな動的計画法　→　dpテーブルはベクトルで十分
# dp = [[0] * (W + 1) for _ in range(N + 1)]

# for i in range(N):
#     for j in range(W + 1):
#         dp[i + 1][j] = dp[i][j]
#         if j - w[i] >= 0:
#             dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - w[i]] + v[i])

# print(dp[-1][-1])



#dpテーブルをベクトルにした動的計画法
#ループを逆から回す
dp = [0] * (W + 1)
for i in range(N):
    for prev in range(W - w[i], -1, -1):
        new_v = dp[prev] + v[i]
        if new_v > dp[prev + w[i]]:
            dp[prev + w[i]] = new_v

print(dp[-1])


