import math
x, k, d = map(int, input().split())
x = abs(x)
if x - k * d < 0:
    tmp = math.floor(x / d)
    if (k - tmp) % 2 == 1:
        print(abs(x - (tmp + 1) * d))
    else:
        print(abs(x - tmp * d))
else:
    print(x - k * d)
        