a, b = map(int, input().split())
c, d = map(int, input().split())

ab = a + b
a_b = a - b
cd = c + d
c_d = c - d

if a == c and b == d:
    print(0)

elif ab == cd or a_b == c_d or abs(a - c) + abs(b - d) <= 3:
    print(1)

elif abs(a - c) + abs(b - d) <= 6:
    print(2)

elif (a - b) % 2 == (c - d) % 2:
    print(2)

elif abs(ab - cd) == 1 or abs(ab - cd) == 2 or abs(ab - cd) == 3 or abs(a_b - c_d) == 1 or abs(a_b - c_d) == 2 or abs(a_b - c_d) == 3:
    print(2)

else:
    print(3)




