S = input()

flag = True

i = 0
is_odd = True

while(i < len(S)):
    if is_odd == S[i].islower():
        is_odd = not is_odd
        i += 1
    else:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")



