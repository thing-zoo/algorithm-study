import sys
from collections import deque
input = sys.stdin.readline
def bfs(y, x, visited, graph, ocean):
    q = deque()
    q.append([y,x])
    visited[y][x] = 1
    while q:
        y, x = q.popleft()
        ocean[y][x] = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and graph[ny][nx] > 0:
                    visited[ny][nx] = 1
                    q.append([ny, nx])
                if not graph[ny][nx]:
                    ocean[y][x] += 1

def solution(graph):
    answer = 0
    while True:
        area = 0
        visited = [ [0]*m for _ in range(n) ]
        ocean = [ [0]*m for _ in range(n) ]
        for i in range(n): # 덩어리 세기
            for j in range(m):
                if graph[i][j] and not visited[i][j]:
                    bfs(i, j, visited, graph, ocean)
                    area += 1

        if area >= 2:
            return answer
        if area == 0:
            return 0
        
        for i in range(n): # 녹이기
            for j in range(m):
                if graph[i][j]:
                    graph[i][j] = max(graph[i][j]-ocean[i][j], 0) 
        
        answer += 1

# 0:바다, 1이상:빙산->인접한 바다칸 수 만큼 녹음
dx = [1,0,-1,0]
dy = [0,1,0,-1]
n, m = map(int, input().split())
graph = []; ice = []
for i in range(n):
    graph.append(list(map(int, input().rstrip().split())))
print(solution(graph))