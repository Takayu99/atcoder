S = input()

o = []
x = []

for i, s in enumerate(S):
    if s == "o":
        o.append(str(i))
    elif s == "x":
        x.append(str(i))
ans = 0
for i in range(10000):
    i = list(str(i).zfill(4))
    flag = True
    for p in o:
        if not p in i:
            flag = False
            break
    for p in x:
        if p in i:
            flag = False
            break
    if flag:
        ans += 1

print(ans)
