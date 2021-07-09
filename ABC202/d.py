import math

def perm(a, b):
    return math.factorial(a + b) // math.factorial(a) // math.factorial(b)

a, b, k = map(int, input().split())
ans = []
pos = 1
x, y = a, b

for i in range(x + y):
    if pos == k:
        for _ in range(a):
            ans.append("a")
        for _ in range(b):
            ans.append("b")
        break
    tmp = perm(a - 1, b)
    if pos + tmp <= k:
        ans.append("b")
        b -= 1
        pos += tmp

    elif pos + tmp > k:
        ans.append("a")
        a -= 1

print("".join(ans))
