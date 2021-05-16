n = int(input())

mt = []
for i in range(n):
    s, t = input().split()
    t = int(t)
    mt.append((t, s))

mt.sort()

print(mt[-2][1])