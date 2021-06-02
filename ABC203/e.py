n, m = map(int, input().split())

xy = [list(map(int, input().split())) for _ in range(m)]

# yx = []
# for i in range(m):
#     x, y = map(int, input().split())
#     yx.append([y, x])

xy.sort()
print(xy)
a = set(xy[0])
print(a)

