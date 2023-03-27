def cut(a, b, n):
    num = graph[a][b]
    for i in range(a, a+n):
        for j in range(b, b+n):
            if graph[i][j] != num:
                for k in range(2):
                    for l in range(2):
                        cut(a+(k*n//2), b+(l*n//2), n//2)
                return
    result[num] += 1
graph = []
result = [0]*2
n = int(input())
for _ in range(n):
    graph.append(list(map(int, input().split())))
cut(0, 0, n)
print(*result, sep="\n")