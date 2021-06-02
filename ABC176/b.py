n = list(input())
ans = 0
for s in n:
    ans += int(s)

if ans % 9 == 0:
    print("Yes")
else:
    print("No")