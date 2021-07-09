n, k = map(int, input().split())

ab = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append([a, b])

ab.sort()
money = k
pos = 0
for a, b in ab:
    money -= a - pos
    if money < 0:
        ans = a + money
        print(ans)
        exit()
    money += b
    pos = a


print(pos + money)

