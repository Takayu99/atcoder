#Almost GCD

n = int(input())
a = list(map(int, input().split()))

tmp = 0
for k in range(2, 1001):
    gcd = 0
    for i in range(n):
        if a[i] % k == 0:
            gcd += 1
    if gcd >= tmp:
        tmp = gcd
        ans = k

print(ans)


