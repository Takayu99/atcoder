n, x = map(int, input().split())

alc = 0

cup = -1

for i in range(n):
    v, p = map(int, input().split())
    alc += v * p
    if cup == -1 and alc > x * 100:
        cup = i + 1

print(cup)

