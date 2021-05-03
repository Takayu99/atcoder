a, b = input().split()

def s(n):
    ans = 0
    for i in n:
        ans += int(i)
    return ans

print(max(s(a), s(b)))
