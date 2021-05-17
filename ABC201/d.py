"""
h, w = map(int, input().split())

A = [list(input()) for _ in range(h)]
a = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if A[i][j] == "+":
            a[i][j] = 1
        else:
            a[i][j] = -1

dp = [[0] * w for _ in range(h)]

for i in range(1, h):
    if i % 2 == 1:
        dp[i][0] = dp[i - 1][0] + a[i][0]
    else:
        dp[i][0] = dp[i - 1][0] - a[i][0]


for j in range(1, w):
    if j % 2 == 1:
        dp[0][j] = dp[0][j - 1] + a[0][j]
    else:
        dp[0][j] = dp[0][j - 1] - a[0][j]

for i in range(1, h):
    for j in range(1, w):
        if (i + j) % 2 == 1:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + a[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) - a[i][j]

if dp[-1][-1] > 0:
    print("Takahashi")
elif dp[-1][-1] < 0:
    print("Aoki")
else:
    print("Draw")
"""


h, w = map(int, input().split())

A = [list(input()) for _ in range(h)]
a = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if A[i][j] == "+":
            a[i][j] = 1
        else:
            a[i][j] = -1

dp = [[0] * w for _ in range(h)]

for i in range(h - 2, -1, -1):
    if i % 2 == 1:
        dp[i][w - 1] = dp[i + 1][w - 1] - a[i + 1][w - 1]
    else:
        dp[i][w - 1] = dp[i + 1][w - 1] + a[i + 1][w - 1]


for j in range(w - 2, -1, -1):
    if j % 2 == 1:
        dp[h - 1][j] = dp[h - 1][j + 1] - a[h - 1][j + 1]
    else:
        dp[h - 1][j] = dp[h - 1][j + 1] + a[h - 1][j + 1]


print(dp)
for i in range(h - 2, -1, -1):
    for j in range(w - 2, -1, -1):
        if (i + j) % 2 == 1:
            dp[i][j] = min(dp[i + 1][j] - a[i + 1][j], dp[i][j + 1] - a[i][j + 1])
        else:
            dp[i][j] = max(dp[i + 1][j] + a[i + 1][j], dp[i][j + 1] + a[i][j + 1])

if dp[0][0] > 0:
    print("Takahashi")
elif dp[0][0] < 0:
    print("Aoki")
else:
    print("Draw")

print(dp)
print(a)