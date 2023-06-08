n, m = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
alpha = [False]*26
ans = 0

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if not alpha[ord(board[nx][ny])-65]: # 아직 방문 안한 알파벳이면
            alpha[ord(board[nx][ny])-65] = True
            # print(alpha)
            dfs(nx, ny, cnt+1)
            # print(alpha)
            alpha[ord(board[nx][ny])-65] = False
 
board = [list(input()) for _ in range(n)]


alpha[ord(board[0][0])-65] = True
dfs(0, 0, 1)
print(ans)