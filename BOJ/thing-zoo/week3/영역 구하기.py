from collections import deque
def bfs(a,b):
    q = deque([[a,b]])
    graph[a][b] = 1
    answer = 1
    while q:
        y, x = q.popleft()
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = 1
                    q.append([ny, nx])
                    answer += 1
    return answer

dir = [[0,-1],[1,0],[0,1],[-1,0]]
m, n, k = map(int, input().split())     # m:세로, n:가로, k:좌표 개수
graph = [ [0] * n for _ in range(m) ]   # 직사각형 & 방문 표시
result = []
for _ in range(k):
    a, b, c, d = map(int, input().split())  #(a,b): 직사각형 왼쪽아래점, (c,d): 직사각형 오른쪽위점
    for i in range(b, d):
        for j in range(a, c):
            graph[i][j] = 1                 # 직사각형 표시

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            result.append(bfs(i,j))
print(len(result))
print(*sorted(result))