S = input()
T = input()

ans = len(T)
for i in range(len(S) - len(T) + 1):
    tmp = len(T)
    s = S[i:i + len(T)]
    for j in range(len(T)):
        if s[j] == T[j]:
            tmp -= 1
    ans = min(tmp, ans)

print(ans)


