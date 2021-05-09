n = int(input())

A = list(map(int, input().split()))
a = [x % 200 for x in A]

dp = [[False] * 200 for _ in range(n)]
index = [[] for _ in range(200)]

for i in range(n):
    x = a[i] % 200
    if not dp[i - 1][x]:
        index[x].append(i)
        dp[i][x] = True
    else:
        print("Yes")
        b = index[x]
        c = i
        print("b", b)
        print("c", c)
        exit()
    for j in range(200):
        if dp[i - 1][j]:
            dp[i][j] = True
            if not dp[i - 1][(j + a[i]) % 200]:
                index[(j + a[i]) % 200].extend(index[j])
                index[(j + a[i]) % 200].append(i)
                dp[i][(j + a[i]) % 200] = True
            else:
                print("Yes")
                b = index[x]
                c = index[j].append(i)
                print("b", b)
                print("c", c)
                exit()
    print(index)


print("No")

