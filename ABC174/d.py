n = int(input())

c = list(input())

f = 0
b = n - 1
ans = 0
flag = True

while(flag):
    while(True):
        if c[f] == "W":
            break
        if f + 1 >= n:
            flag = False
            break
        f += 1
    while(True):
        if c[b] == "R":
            break
        if b - 1 < 0:
            flag = False
            break
        b -= 1
    if f < b:
        c[f] = "R"
        c[b] = "W"
        ans += 1
    else:
        break
print(ans)

