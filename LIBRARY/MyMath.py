import math

def base_10_to_n(value, base):
    if (value // base):
        return base_10_to_n(value // base, base) + str(value % base)
    
    return str(value % base)


def permutation(n, r):
    return math.factorial(n) // math.factorial(n - r)


def combination(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


