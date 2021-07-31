import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right


x = list(input())
x = list(map(int, x))

tmp = x[0]
flag = True
if x[0] == x[1] and x[1] == x[2] and x[2] == x[3]:
    print("Weak")
elif x[1]== (x[0] + 1) % 10 and x[2]== (x[1] + 1) % 10 and x[3]== (x[2] + 1) % 10:
    print("Weak")
else:
    print("Strong")


