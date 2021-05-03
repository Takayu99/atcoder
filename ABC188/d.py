N, C = map(int, input().split())

event = []

for _ in range(N):
    a, b, c = map(int, input().split())
    a -= 1
    event.append((a, c))
    event.append((b, -c))

event.sort()
day = 0
cost = 0
total = 0

for e in event:
    if cost > C:
        total += (e[0] - day) * C
    else:
        total += (e[0] - day) * cost
    day = e[0]
    cost += e[1]

print(total)


