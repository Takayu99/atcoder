n = int(input())

t = 1
f = 1

for i in range(n):
    s = input()
    if s == "AND":
        f = t + f * 2
    else:
        t = t * 2 + f

print(t)

