x, y = map(int, input().split())
z = [0, 1, 2]

z.remove(x)
if y in z:
    z.remove(y)
    print(z[0])
else:
    print(y)
