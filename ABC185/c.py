import math

l = int(input())

def combination(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

l = int(input())

print(combination(l - 1, 11))

