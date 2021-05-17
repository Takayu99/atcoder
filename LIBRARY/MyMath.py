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

def bit_count(n):
    #2進数表記した時の1の個数を返す
    x = 0
    while(n > 0):
        if n & 1:
            x += 1
        n = n >> 1
    return x
