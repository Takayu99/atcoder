import math

r, x, y = map(int, input().split())

d = math.sqrt(x**2 + y**2)

if d < r:
    print(2)

else:
    if d % r == 0:
        print(int(d // r))
    else:
        print(int(d // r + 1)) #math.ceil(d/r)
