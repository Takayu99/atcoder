n = int(input())

xy = [list(map(int, input().split())) for _ in range(n)]

ab = []
INF = 10 ** 5

for i in range(n - 1):
    for j in range(i + 1, n):
        if xy[i][0] == xy[j][0]:
            a = INF
            b = xy[i][0]
        else:
            a = (xy[j][1] - xy[i][1]) / (xy[j][0] - xy[i][0])
            b = (xy[j][0] * xy[i][1] - xy[i][0] * xy[j][1]) / (xy[j][0] - xy[i][0])
        if [a, b] in ab:
            print("Yes")
            exit()
        else:
            ab.append([a, b])

print("No")




