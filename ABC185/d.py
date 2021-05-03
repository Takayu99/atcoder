import math

N, M = map(int, input().split())

a = list(map(int, input().split()))
a.sort()

if M == 0:
    print(1)
    exit()
    
d = []
if a[0] > 1:
    d.append(a[0] - 1)

for i in range(1, M):
    if a[i] - a[i - 1] > 1:
        d.append(a[i] - a[i - 1] - 1)

if N - a[M - 1] > 0:
    d.append(N - a[M - 1])

if d:   
    k = min(d)
else:
    print(0)
    exit()

for i in range(len(d)):
    d[i] = math.ceil(d[i] / k)

print(sum(d))

    