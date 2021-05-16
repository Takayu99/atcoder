n = int(input())
a = list(map(int, input().split()))

cumsum = [0] * (n + 1)
mod = 10 ** 9 + 7
for i in range(n):
    cumsum[i + 1] = cumsum[i] + a[i]
    cumsum[i + 1] %= mod

ans = 0

for i in range(1, n):
    ans += a[n - i] * cumsum[n - i]
    ans %= mod

print(ans)