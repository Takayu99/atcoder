n = int(input())

ans = 10 ** 9 + 1

for i in range(n):
    a, p, x  = map(int, input().split())
    if x - a > 0:
        if ans > p:
            ans = p

if ans == 10 ** 9 + 1:
    ans = -1

print(ans)