n, k = map(int, input().split())

def g1(x):
    x = list(str(x))
    x.sort(reverse=True)
    return int("".join(x))

def g2(x):
    x = list(str(x))
    x.sort()
    return int("".join(x))

def f(x):
    return g1(x) - g2(x)

ai = n

for _ in range(k):
    ai = f(ai)

print(ai)



