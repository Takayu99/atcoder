n = int(input())

x = []
y = []

for i in range(n):
    X, Y = map(int, input().split())
    x.append(X)
    y.append(Y)

cnt = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        if -1 <= (y[i] - y[j]) / (x[i] - x[j]) <= 1:
            cnt += 1

print(cnt)