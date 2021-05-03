x, y = map(int, input().split())

if x >= y:
    ans = x - y
else:
    ans = y - x

if ans < 3:
    print("Yes")
else:
    print("No")
