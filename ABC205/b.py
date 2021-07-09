n = int(input())
a = list(map(int, input().split()))

flag = True
a.sort()
for i in range(1, n + 1):
    if i != a[i - 1]:
        flag= False

if flag:
    print("Yes")
else:
    print("No")