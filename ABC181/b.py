n = int(input())

ans = 0

for _ in range(n):
    a, b = map(int, input().split())
    if (a - b) % 2 == 1:
        ans += (a + b) * ((b - a + 1) // 2)
    else:
        ans += (a + b) // 2 * (b - a + 1)

print(ans)


