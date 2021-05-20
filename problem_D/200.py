from itertools import product

n = int(input())

a = list(map(int, input().split()))

dp = [0] * 200

for p in product([True, False], repeat = n):
    tmp = 0
    for i in range(n):
        if p[i]:
            tmp += a[i]
    tmp %= 200
    if dp[tmp] == 0:
        dp[tmp] = p
        # print(dp[tmp])
    else:
        b = [i + 1 for i in range(n) if p[i]]
        c = [i + 1 for i in range(n) if dp[tmp][i]]
        print("Yes")
        print(len(b), *b)
        print(len(c), *c)
        exit()
    

print("No")






