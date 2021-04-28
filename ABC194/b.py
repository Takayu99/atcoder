# n = int(input())

# a1 = a2 = b1 = b2 = 10 ** 5

# for i in range(n):
#     a, b = list(map(int, input().split()))

#     if a < a1:
#         a2 = a1
#         a1 = a
#         index_a = i

#     else:
#         if a < a2:
#             a2 = a

#     if b < b1:
#         b2 = b1
#         b1 = b
#         index_b = i

#     else:
#         if b < b2:
#             b2 = b

# if index_a == index_b:
#     print(max(min(a1 + b1, a2, b2), a1, b1))
# else:
#     print(max(a1, b1))

N = int(input())
A = []
B = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = float('INF')  # 正の無限大を初期値にします

for i in range(N):
    for j in range(N):
        if i == j:
            score = A[i] + B[i]
        else:
            score = max(A[i], B[j])
        ans = min(ans, score)

print(ans)