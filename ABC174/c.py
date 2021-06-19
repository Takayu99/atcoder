k = int(input())

mod = [False] * k
a = 7
ans = 1
while(True):
    if a % k == 0:
        print(ans)
        exit()
    a = (a * 10 + 7) % k
    ans += 1
    if mod[a]:
        print(-1)
        exit()
    else:
        mod[a] = True

