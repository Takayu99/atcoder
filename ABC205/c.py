a, b, c = map(int, input().split())

c = c % 2

if a >= 0 and b >= 0:
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")
elif a >= 0 and b < 0:
    if c == 1:
        print(">")
    else:
        if abs(a) == abs(b):
            print("=")
        elif abs(a) < abs(b):
            print("<")
        else:
            print(">")
elif a < 0 and b >= 0:
    if c == 0:
        if abs(a) > abs(b):
            print(">")
        elif abs(a) < abs(b):
            print("<")
        else:
            print("=")
    else:
        print("<")
elif a < 0 and b < 0:
    if c == 1:
        if abs(a) < abs(b):
            print(">")
        elif abs(a) > abs(b):
            print("<")
        else:
            print("=")
    else:
        if abs(a) < abs(b):
            print("<")
        elif abs(a) > abs(b):
            print(">")
        else:
            print("=")
