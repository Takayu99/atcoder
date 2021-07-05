import bisect
n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = k // n
k %= n

b = sorted(a)

for i in range(n):
    if bisect.bisect(b, a[i]) <= k:
        print(ans + 1)
    else:
        print(ans)