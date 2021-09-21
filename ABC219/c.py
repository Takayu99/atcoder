import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right
import heapq
import sys
sys.setrecursionlimit(10 ** 6)


x = list(input())
n = int(input())
s = []
t = []
for i in range(n):
    c = input()
    s.append(c)

alpha = "abcdefghijklmnopqrstuvwxyz"
convert1 = [0] * 26
convert2 = [0] * 26

for i in range(26):
    for j in range(26):
        if x[i] == alpha[j]:
            convert1[i] = j
            convert2[j] = i

for i in range(n):
    c = list(s[i])
    tmp = []
    for j in range(len(c)):
        tmp.append(alpha[convert1[ord(c[j]) - 97]])
    t.append(tmp)

t.sort()

ans = []
for i in range(n):
    c = list(t[i])
    tmp = []
    for j in range(len(c)):
        tmp.append(alpha[convert2[ord(c[j]) - 97]])
    ans.append("".join(tmp))

for a in ans:
    print(a)






"""
zyxwvutsrqponmlkjihgfedcba
5
b
ab
ba
aab
baa


"""