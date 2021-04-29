n, m = map(int, input().split())

ab = []
cd = []
ans = 0


for i in range(m):
    ab.append(list(map(int, input().split())))

k = int(input())

for i in range(k):
    cd.append(list(map(int, input().split())))


for i in range(2 ** k):
    s = set()
    for j in range(k):
        s.add(cd[j][i >> j & 1])

    cnt = 0
    for j in range(m):
        if ab[j][0] in s and ab[j][1] in s:
            cnt += 1
    if cnt > ans:
        ans = cnt

print(ans)



