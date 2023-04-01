import sys
from collections import deque
def bfs():
    q = deque()
    q.append([0,0,0])
    visited[0][0][0] = 1 # 방문표시
    while q:
        y, x, k = q.popleft()
        if y == H-1 and x == W-1: # 탈출
            return visited[y][x][k]-1
        if k < K: # 나이트 이동이 가능하면
            for i in range(8):
                ny = y + dy2[i]
                nx = x + dx2[i]
                if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx][k+1]:
                    if graph[ny][nx] == 0: #벽이 아니면
                        visited[ny][nx][k+1] = visited[y][x][k] + 1
                        q.append([ny, nx, k+1])    
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx][k]:
                if graph[ny][nx] == 0: #벽이 아니면
                    visited[ny][nx][k] = visited[y][x][k] + 1
                    q.append([ny, nx, k])    
    return -1
dx = [1,0,-1,0]; dx2 = [1,2,2,1,-1,-2,-2,-1]
dy = [0,1,0,-1]; dy2 = [-2,-1,1,2,2,1,-1,-2]
input = sys.stdin.readline
K = int(input())
W, H = map(int, input().split())
graph = []
visited = [ [ [0]*(K+1) for _ in range(W) ] for _ in range(H) ]
for _ in range(H):
    graph.append(list(map(int, input().rstrip().split())))
print(bfs())