"""
グラフサンプル

sample1
5 7
1 2 50
1 3 80
2 3 20
2 4 15
3 4 10
3 5 15
4 5 30
"""



#ダイクストラ法
#重み付きグラフを用いた最短経路の導出

n, m = map(int, input().split())

G = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append([b, c])

INF = 10 ** 5
dist = [INF] * n
prev = [-1] * n
dist[0] = 0




