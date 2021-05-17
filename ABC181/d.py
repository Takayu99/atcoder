"""
from collections import Counter
from itertools import permutations

s = list(input())
new = []

counter = dict(Counter(s))

for i in range(1, 10):
    for _ in range(min(counter.get(str(i), 0), 3)):
        new.append(i)

if len(new) == 1:
    if 8 in new:
        print("Yes")
    else:
        print("No")
elif len(new) == 2:
    if (10 * new[0] + new[1]) % 8 == 0 or (10 * new[1] + new[0]) % 8 == 0:
        print("Yes")
    else:
        print("No")
else:
    for p in permutations(new, 3):
        tmp = 100 * p[0] + 10 * p[1] + p[2]
        if tmp % 8 == 0:
            print("Yes")
            exit()

    print("No")
"""

from collections import Counter

n = input()

if len(n) <= 2:
    if int(n) % 8 == 0 or int(n[::-1])  % 8 == 0:
        print("Yes")
    else:
        print("No")
    exit()

cnt = Counter(n)

for i in range(112, 1000, 8):
    if not Counter(str(i)) - cnt:
        print("Yes")
        exit()

print("No")


