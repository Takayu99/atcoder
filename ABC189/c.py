n = int(input())
a = list(map(int, input().split()))

ans = 0

for l in range(n):
    m = 10 ** 6
    for r in range(l, n):
        m = min(m, a[r])
        ans = max(ans, m * (r + 1 - l))

print(ans)
    