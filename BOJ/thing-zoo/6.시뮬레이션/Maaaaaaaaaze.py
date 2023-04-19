import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline
def bfs(m): # 미로를 탈출하는 이동횟수 구하는 함수
    global answer
    dx = [1,0,-1,0,0,0]; dy = [0,1,0,-1,0,0]; dz = [0,0,0,0,1,-1]
    q = deque(); q.append([0,0,0])
    dist = [[[0]*n for _ in range(n)] for _ in range(n)]
    dist[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        if dist[x][y][z] >= answer: # 현재 최소값이상이면
            return
        if (x, y, z) == (n-1, n-1, n-1):
            answer = min(answer, dist[x][y][z]-1)
            if dist[x][y][z]-1 == 12: # 최소값이면
                print(12)
                exit() # 실행종료
            return
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if 0 <= nx < n and 0 <= ny < n and 0 <= nz < n:
                if not dist[nx][ny][nz] and m[nx][ny][nz]:
                    dist[nx][ny][nz] = dist[x][y][z] + 1
                    q.append([nx,ny,nz])

def rotate(m): # 2차원 배열 회전 함수
    rotated = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n-1-i] = m[i][j]
    return rotated

def dfs(k): # k번째 판
    if k == n: # 모든 판 방문
        if m[n-1][n-1][n-1]:
            bfs(m)
        return # 종료
    for _ in range(4): # 3번 회전시키기
        if m[0][0][0]:
            dfs(k + 1)
        m[k] = rotate(m[k])

n = 5
maze = [[list(map(int, input().strip().split())) for _ in range(n)] for _ in range(n)]
m = [[[0]*n for _ in range(n)] for _ in range(n)]
answer = sys.maxsize

for order in permutations(range(n), n): # 판 순서 정하기
    for i in range(n):
        m[i] = maze[order[i]]
    dfs(0)
print(answer if answer != sys.maxsize else -1)