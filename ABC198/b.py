# from collections import deque

# n = deque(list(input()))
# f = True
# while(f and len(n) > 0):
#     if(n[-1] != "0"):
#         f = False
#     else:
#         n.pop()


# f = True
# while(f):
#     if len(n) >= 2:
#         if(n.pop() != n.popleft()):
#             f = False

#     else:
#         break

# if f:
#     print("Yes")
# else:
#     print("No")

#-----------------------------------------------------------------------------------#

n = input()

for i in range(10):
    s = "0" * i + n
    if s == s[::-1]:
        print("Yes")
        exit()
    
print("No")