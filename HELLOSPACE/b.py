N, D, H = map(int, input().split())

ans = 0

for i in range(N):
    d, h = map(int, input().split())
    b = (h * D - H * d) / (D - d)
    ans = max(ans, b)

print(ans)

