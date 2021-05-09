#Water Heater

N, W = map(int, input().split())

event = []

for _ in range(N):
    s, t, p = map(int, input().split())
    event.append((s, p))
    event.append((t, -p))

event.sort()

demand = 0
for e in event:
    demand += e[1]
    if demand > W:
        print("No")
        exit()

print("Yes")




