import math

n = int(input())

ans = 0

for a in range(1, n):
    ans += math.floor((n - 1) / a)

print(ans)