from itertools import permutations


def assign():
    D = [-1] * 26
    for c, num in zip(chars, per):
        D[c] = num
    
    h1, h2, h3 = t1[-1], t2[-1], t3[-1] #最初の１文字目
    if D[h1] == 0 or D[h2] == 0 or D[h3] == 0:
        return False, D
    return True, D

def convert():
    n1, n2, n3 = 0, 0, 0
    for i, c in enumerate(t1):
        n1 += D[c] * 10 ** i
    for i, c in enumerate(t2):
        n2 += D[c] * 10 ** i
    for i, c in enumerate(t3):
        n3 += D[c] * 10 ** i
    return n1, n2, n3


def judge(n1, n2, n3):
    return n1 + n2 == n3



s1 = input()[::-1]
s2 = input()[::-1]
s3 = input()[::-1]

t1 = [ord(c) - ord("a") for c in s1]
t2 = [ord(c) - ord("a") for c in s2]
t3 = [ord(c) - ord("a") for c in s3]

chars = set()
chars.update(t1, t2, t3)
l = len(chars)

if l > 10:
    print("UNSOLVABLE")
    exit()

for per in permutations(range(10), r=l):
    is_valid, D = assign()
    if not is_valid:
        continue
    
    n1, n2, n3 = convert()
    if judge(n1, n2, n3):
        print(n1)
        print(n2)
        print(n3)
        exit()

print("UNSOLVABLE")







    