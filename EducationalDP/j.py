#Sushi
#メモ化再帰
from collections import Counter

N = int(input())
a = list(map(int, input().split()))

d = dict(Counter(a))
c = [0, 0, 0, 0]

for i in range(1, 4):
    if i in d.keys():
        c[i] = d[i]
    
dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
flag = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
flag[0][0][0] = 1

def f(c1, c2, c3):
    global flag, dp
    if flag[c1][c2][c3]:
        return dp[c1][c2][c3]
    
    flag[c1][c2][c3] = 1
    fans = 1 / (1 - (N - c1 - c2 - c3) / N)
    if c1 > 0:
        fans += f(c1 - 1, c2, c3) * c1 / (N * (1 - (N - c1 - c2 - c3) / N))
    if c2 > 0:
        fans += f(c1 + 1, c2 - 1, c3) * c2 / (N * (1 - (N - c1 - c2 - c3) / N))
    if c3 > 0:
        fans += f(c1, c2 + 1, c3 - 1) * c3 / (N * (1 - (N - c1 - c2 - c3) / N))
    
    dp[c1][c2][c3] = fans
    return fans


print(f(c[1], c[2], c[3]))
