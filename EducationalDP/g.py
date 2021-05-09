#Longest Path

"""
深さ優先探索

N, M = map(int, input().split())

p = [[0] * N for _ in range(N)]
ans = [0] * N

for _ in range(M):
    x, y = map(int, input().split())
    p[x - 1][y - 1] = 1

index = 0
tmp = 0

def check(n, x):
    global ans
    for i in range(N):
        if p[n][i] == 1:
            check(i, x + 1)
    
    if not all(p[n]):
        ans[index] = max(ans[index], x)


for i in range(N):
    index = i
    check(i, 0)

print(max(ans))
"""




#メモ化再帰

N, M = map(int, input().split())

p = [[0] * N for _ in range(N)]
flag = [0] * N
dp = [0] * N

for _ in range(M):
    x, y = map(int, input().split())
    p[x - 1][y - 1] = 1


def f(x):
    global flag, dp
    if flag[x]:
        return dp[x]
    flag[x] = 1
    fans = 0
    for i in range(N):
        if p[x][i] == 1:
            fans = max(fans, f(i) + 1)
    
    dp[x] = fans
    return fans


ans = 0

for i in range(N):
    ans = max(ans, f(i))

print(ans)





