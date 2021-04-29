# n = int(input())

# expressed = []
# cnt = 0

# for a in range(2, 10 ** 5 +  1):
#     b = 2
#     while(True):
#         tmp = a ** b
#         if tmp <= n:
#             if not (tmp in expressed):
#                 # cnt += 1
#                 expressed.append(tmp)
#             b += 1
#         else:
#             break

# print(n - len(expressed))

n = int(input())
sq = int(n ** 0.5)
s = set()
for a in range(2, sq + 1):
    x = a * a
    while x <= n:
        s.add(x)
        x *= a

print(n - len(s))
             











# cnt = 0

# for a in range(2, 10 ** 5 + 1):
#     b = 2
#     while(True):
#         if a ** b <= n:
#             cnt += 1
#             b += 1
#         else:
#             break