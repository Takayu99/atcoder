import math
a, b, w = map(int, input().split())

w *= 1000


if w // a != w // b:
    print("{} {}".format(math.ceil(w / b), math.floor(w / a)))
else:
    if w % a == 0 or w % b == 0:
        print("{} {}".format(math.ceil(w / b), math.floor(w / a)))
    else:
        print("UNSATISFIABLE")
