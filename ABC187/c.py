# n = int(input())

# odd = set()
# even = set()

# for i in range(n):
#     s = input()
#     if s[0] == "!":
#         if s[1:] in even:
#             print(s[1:])
#             exit()
#         else:
#             odd.add(s)
#     else:
#         if "!" + s in odd:
#             print(s)
#             exit()
#         else:
#             even.add(s)

# print("satisfiable")


n = int(input())
S = set(input() for i in range(n))

for s in S:
    if "!" + s in S:
        print(s)
        exit()

print("satisfiable")