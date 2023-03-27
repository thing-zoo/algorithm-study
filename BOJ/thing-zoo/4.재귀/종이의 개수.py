def cut(a, b, n):
    num = graph[a][b] # 현재값

    for i in range(a, a+n): # 모든값 방문
        for j in range(b, b+n):
            if graph[i][j] != num: # 값이 다를 경우
                for k in range(3): # 9분할
                    for l in range(3):
                        cut(a+(k*n//3), b+(l*n//3), n//3)
                return
    result[num+1] += 1 # 현재값 카운트

n = int(input())
graph = []
result = [0]*3
for _ in range(n):
    graph.append(list(map(int, input().split())))
cut(0, 0, n)
print(*result, sep="\n")