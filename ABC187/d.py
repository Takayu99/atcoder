n = int(input())

ab = [tuple(map(int, input().split())) for i in range(n)]
score = []

x = 0
for i in range(n):
    x -= ab[i][0]
    score.append(2 * ab[i][0] + ab[i][1])

score.sort()

for i in range(1, n + 1):
    x += score.pop()
    if x > 0:
        break

print(i)