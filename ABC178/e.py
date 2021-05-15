n = int(input())

point = [list(map(int, input().split())) for _ in range(n)]

r = point[0][0]
l = point[0][0]
t = point[0][1]
b = point[0][1]

rp = lp = tp = bp = 0

for i, p in enumerate(point):
    if p[0] >= r:
        r = p[0]
        rp = i
    if p[0] <= l:
        l = p[0]
        lp = i
    if p[1] >= t:
        t = p[1]
        tp = i
    if p[1] <= b:
        b = p[1]
        bp = i

ans = 0
for p in [rp, lp, tp, bp]: 
    for q in [rp, lp, tp, bp]:
        tmp = abs(point[p][0] - point[q][0]) + abs(point[p][1] - point[q][1])
        ans = max(ans, tmp)

print(ans)



