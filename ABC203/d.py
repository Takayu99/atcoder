import math
import numpy as np
n, k = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

ans = 10 ** 9
for x in range(n - k + 1):
    for y in range(n - k + 1):
        tmp = []
        for i in range(k):
            for j in range(k):
                tmp.append(a[x + i][y + j])
        tmp.sort()
        ans = min(ans, tmp[math.ceil(k * k / 2) - 1])

print(ans)
