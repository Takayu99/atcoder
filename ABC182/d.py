#Wandering

n = int(input())
a = list(map(int, input().split()))

x = [0] * n
y = [0] * n
x[0] = a[0]
y[0] = x[0]
xmax = x[0]
ans = max(0, x[0])
if n == 1:
    print(ans)
    exit()

if n == 2:
    print(max(0, a[0] * 2, a[0] * 2 + a[1]))
    exit()

for i in range(1, n):
    x[i] = x[i - 1] + a[i]
    y[i] = y[i - 1] + x[i]
    ans = max(ans, y[i] + xmax)
    xmax = max(xmax, x[i])

print(ans)
