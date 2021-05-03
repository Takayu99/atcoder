n = int(input())


def base_10_to_n(value, base):
    if (value // base):
        return base_10_to_n(value // base, base) + str(value % base)
    
    return str(value % base)


ans = 0

for i in range(1, n + 1):
    if not("7" in str(i) or "7" in base_10_to_n(i, 8)):
        ans += 1

print(ans)