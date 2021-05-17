import math

def base_10_to_n(value, base):
    if (value // base):
        return base_10_to_n(value // base, base) + str(value % base)
    
    return str(value % base)


def permutation(n, r):
    return math.factorial(n) // math.factorial(n - r)


def combination(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def divisor(n):
    div = []
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            div.append(i)
            div.append(n // i)
    return list(set(div))

def num_divisor(n):
    div = []
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            div.append(i)
            div.append(n // i)
    return len(set(div))

