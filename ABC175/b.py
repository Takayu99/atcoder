import math
from itertools import product, combinations

N = int(input())
L = map(int, input().split())
ans = 0
for p in combinations(L, 3):
    flag = True
    if p[0] != p[1] and p[1] != p[2] and p[2] != p[0]:
        for i in range(3):
            if p[i % 3] + p[(i + 1) % 3] <=  p[(i + 2) % 3]:
                flag = False
        if flag:
            ans += 1

print(ans)