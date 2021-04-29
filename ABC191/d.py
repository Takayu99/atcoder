import math

x, y, r = map(float, input().split())

rr = r * r
cnt = 0
top = math.ceil(y + r)
bottom = math.floor(y - r)
right = math.ceil(x + r)
left = math.floor(x - r)

for i in range(left, right + 1):
    for j in range(bottom, top + 1):
        if (i - x) * (i - x) + (j - y) * (j - y) <= rr:
            cnt += 1

print(cnt)
