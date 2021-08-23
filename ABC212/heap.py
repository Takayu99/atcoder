import heapq

a = [8, 4, 2, 6, 9, 12, 3, 5, 1]
heapq.heapify(a)
# print(a)
# print(heapq.heappop(a))
# print(a)
for i in range(len(a)):
    print(heapq.heappop(a))
    print(a)