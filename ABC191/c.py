h, w = map(int, input().split())

s = []

for _ in range(h):
    s.append(list(input()))

ans = 0

for i in range(h - 1):
    for j in range(w - 1):
        if [s[i][j], s[i + 1][j], s[i][j + 1], s[i + 1][j + 1]].count(".") % 2 == 1:
            ans += 1
print(ans)
