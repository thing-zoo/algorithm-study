from collections import deque
def count_area(graph, color):
    answer = 0
    for k in color:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == k:
                    bfs(graph, i, j, k)
                    answer += 1
    return answer

def bfs(graph, i, j, k):
    q = deque([[i,j]])
    graph[i][j] = 0 # 방문 표시
    while q:
        y, x = q.popleft()
        for d in dir:
            ny = y + d[1]
            nx = x + d[0]
            if 0 <= ny < n and 0 <= nx < n:
                if graph[ny][nx] == k:
                    graph[ny][nx] = 0 # 방문 표시
                    q.append([ny, nx])

dir = [[1,0],[0,1],[-1,0],[0,-1]]
n = int(input())                        # n*n 배열
graph1 = []       
graph2 = [[0]*n for _ in range(n) ]     # 적록색약 시야
for _ in range(n):
    graph1.append(list(input()))
for i in range(n):
    for j in range(n):
        if graph1[i][j] == 'G':
            graph2[i][j] = 'R'
        else:
            graph2[i][j] = graph1[i][j]

result = []
result.append(count_area(graph1, ('R', 'G', 'B')))
result.append(count_area(graph2, ('R', 'B')))
print(*result)