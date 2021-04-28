# n = input()
# l = len(n)

# ans = 0

# for i in range((l - 1) // 2):
#     ans += 9 * (10 ** i)

# if l % 2 == 0:
#     front = int(n[:l // 2])
#     back = int(n[l // 2:])
#     tmp = min(front, back)
#     if tmp >= 10 ** (l // 2 - 1):
#         ans += tmp - 10 ** (l // 2 - 1) + 1

# print(ans)

"""
[len1]10: 0
[len2]~100: 9
[len3]100~1000: 0
[len4]1000~10000: 90
[len5]10000~100000: 0
[len6]100000~1000000:900
[len7]100000~1000000:0
[len8]100000~1000000:9000
[len9]100000~1000000:0
[len10]100000~1000000:90000
[len11]100000~1000000:0
[len12]100000~1000000:900000


1333 = 13, 33

255555 = 255, 555

255100 = 255, 100
"""


n = int(input())
cnt = 0
i = 1

while True:
    s = str(i) * 2
    x = int(s)
    if x <= n:
        cnt += 1
        i += 1
    else:
        break

print(cnt)
