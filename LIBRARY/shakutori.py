#しゃくとり法

"""
#ABC032 C 列
n, k = map(int, input().split())
s = [int(input()) for i in range(n)]

if 0 in s:
    print(n)
    exit()

r = 0
ans = 0
tmp = 1

for l in range(n):
    while r < n and tmp * s[r] <= k:
        tmp *= s[r]
        r += 1
    ans = max(ans, r - l)
    if l == r:
        r += 1
    else:
        tmp //= s[l]

print(ans)
"""


#ABC038 C 単調増加
n = int(input())
a = list(map(int, input().split()))

l = 0
ans = 0

for r in range(n - 1):
    ans += r - l + 1
    if a[r] >= a[r + 1]:
        l = r + 1
ans += n - l

print(ans)






