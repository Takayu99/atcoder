#Knapsack1
N, W = map(int, input().split())

w = []
v = []

for i in range(N):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)


#i番目以降の品物から，重さの和がj以下になるように選んだ時の，取りうる価値の総和の最大値を返す
def rec(i, j):
    if i == N:
        res = 0
    
    elif j < w[i]:
        res = rec(i + 1, j)

    else:
        res = max(rec(i + 1, j), rec(i + 1, j - w[i]) + v[i])

    return res


#メモ化再帰による実装
def rec_dp(i, j):
    if dp[i][j] != -1:
        return dp[i][j]

    if i == N:
        res = 0
    
    elif j < w[i]:
        res = rec_dp(i + 1, j)

    else:
        res = max(rec_dp(i + 1, j), rec_dp(i + 1, j - w[i]) + v[i])

    dp[i][j] = res

    return res
# dp = [[-1] * (W + 1) for i in range(N + 1)]
# print(rec_dp(0, W))

            


#計算量がO(NW)となる解法
# dp = [[0] * (W + 1) for _ in range(N + 1)]
# for i in range(N):
#     for j in range(W + 1):
#         dp[i + 1][j] = dp[i][j]
#         if j - w[i] >= 0:
#             dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - w[i]] + v[i])
# print(dp[-1][-1])



#計算量がO(NV)となる解法
import bisect
vtotal = sum(v)
INF = 1 << 60
dp = [INF] * (vtotal + 1)

for i in range(N):
    dp_tmp = dp[:]
    for j in range(1, vtotal + 1):
        idx_prev = max(0, j - v[i])
        dp_tmp[j] = min(dp[j], dp[idx_prev] + w[i])
    dp = dp_tmp

print(bisect.bisect_right(dp, W) - 1)