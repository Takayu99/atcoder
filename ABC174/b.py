n, d = map(int, input().split())

xy = [list(map(int, input().split())) for _ in range(n)]
d = d * d
ans = 0

for x, y in xy:
    if x * x + y * y <= d:
        ans += 1
print(ans)