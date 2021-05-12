"Happy Birthday!2"

"""
#WA

n = int(input())

A = list(map(int, input().split()))
a = [0] + [x % 200 for x in A]

dp = [[False] * 200 for _ in range(n + 1)]
index = [[] for _ in range(200)]
dp[0][0] = True

for i in range(1, n + 1):
    for j in range(200):
        if dp[i - 1][j]:
            dp[i][j] = True
            if not dp[i - 1][(j + a[i]) % 200]:
                index[(j + a[i]) % 200].extend(index[j])
                index[(j + a[i]) % 200].append(i)
                dp[i][(j + a[i]) % 200] = True
            else:
                print("Yes")
                print(len(index[(j + a[i]) % 200]), end = " ")
                for b in index[(j + a[i]) % 200]:
                    print(b, end = " ")
                print()
                index[j].append(i)
                print(len(index[j]), end = " ")
                for c in index[j]:
                    print(c, end = " ")
                exit()

print("No")
"""

#鳩ノ巣原理
#bit全探索
from itertools import product

n = int(input())

A = list(map(int, input().split()))
a = [x % 200 for x in A]

bits  = product([0, 1], repeat = n)
seen = [[] for _ in range(200)]

for bit in bits:
    index = [i for i in range(n) if bit[i]]
    tmp = sum(a[i] for i in index) % 200
    if seen[tmp]:
        print("Yes")
        print(len(seen[tmp]), *[x + 1 for x in seen[tmp]])
        print(len(index), *[x + 1 for x in index])
        exit()
    
    seen[tmp] = index

print("No")


    