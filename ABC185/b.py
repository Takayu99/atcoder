N, M, T = map(int, input().split())

t = 0
charge = N

for i in range(M):
    a, b = map(int, input().split())
    charge -= a - t
    if charge <= 0:
        print("No")
        exit()
    charge += b - a
    if charge > N:
        charge = N
    t = b

charge -= T - t
if charge <= 0:
    print("No")
else:
    print("Yes")
    