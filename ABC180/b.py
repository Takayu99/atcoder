import math

n = int(input())
X = list(map(int, input().split()))

m = 0
y = 0

for x in X:
    m += abs(x)
    y += x * x

print(m)
print(math.sqrt(y))
print(max(map(abs, X)))

