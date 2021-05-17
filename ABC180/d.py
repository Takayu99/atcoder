x, y, a, b = map(int, input().split())

tmp = x
ans = 0
flag = True

while flag and tmp * (a - 1) < y:
    if tmp * (a - 1) < b:
        tmp *= a
        ans += 1
    else:
        flag = False
    
ans += (y - 1 - tmp) // b

print(ans)

