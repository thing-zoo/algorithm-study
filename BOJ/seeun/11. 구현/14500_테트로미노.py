import sys
sys.setrecursionlimit(50000000)
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().rstrip().split())))
visited = [[False]*m for _ in range(n)]

maxvalue = max(map(max, board))

maxSum = -1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, nowsum, cnt):
    global maxSum, visited

    if nowsum + maxvalue*(3-cnt) <= maxSum:
        return
    if cnt==3:
        maxSum = max(maxSum, nowsum)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<=ny < m and visited[nx][ny] == False:
                if cnt == 1:
                    visited[nx][ny] = True
                    dfs(x, y, nowsum + board[nx][ny], cnt +1)
                    visited[nx][ny] = False
                
                visited[nx][ny] = True
                dfs(nx, ny, nowsum + board[nx][ny],cnt +1)
                visited[nx][ny] = False
        
for i in range(n):
    for j in range(m):  
        visited[i][j] = True
        dfs(i, j, board[i][j], 0)
        visited[i][j] = False
print(maxSum)