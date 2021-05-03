# s = list(input())

# l = len(s)
# t = []

# for i in range(l):
#     if s[i] == "R":
#         t = t[::-1]
#     else:
#         if t:
#             if t[-1] == s[i]:
#                 t.pop()
#             else:
#                 t.append(s[i])
#         else:
#             t.append(s[i])

# print("".join(t))

from collections import deque

s = list(input())
t = deque()
reverse = False

for i in range(len(s)):
    if s[i] == "R":
        reverse = not reverse
    else:
        if t:
            if reverse:
                if t[0] == s[i]:
                    t.popleft()
                else:
                    t.appendleft(s[i])
            else:
                if t[-1] == s[i]:
                    t.pop()
                else:
                    t.append(s[i])
        else:
            t.append(s[i])

if reverse:
    ans = []
    for _ in range(len(t)):
        ans.append(t.pop())
    # ans = reversed(t)
    print("".join(ans))
else:
    print("".join(t))
