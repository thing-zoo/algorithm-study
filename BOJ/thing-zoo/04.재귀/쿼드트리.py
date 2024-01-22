def QuadTree(n, a, b):
    number = graph[a][b]
    for i in range(a, a+n):
        for j in range(b, b+n):
            if graph[i][j] != number:
                print("(", end="")
                half = n//2
                QuadTree(half, a, b)
                QuadTree(half, a, b+half)
                QuadTree(half, a+half, b)
                QuadTree(half, a+half, b+half)
                print(")", end="")
                return
    print(number, end="")
n = int(input())
graph = [ ]
for _ in range(n):
    graph.append(list(map(int, list(input()))))
QuadTree(n, 0, 0)