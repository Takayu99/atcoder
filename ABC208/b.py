p = int(input())
n = [i for i in range(1, 11)]
for i in range(1, 10):
    n[i] = n[i] * n[i - 1]

ans = 0
for i in range(9, -1, -1):
    ans += p // n[i]
    p %= n[i]
print(ans)