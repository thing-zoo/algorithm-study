import sys
input = sys.stdin.readline
def dfs(x, y, size, total):
    global answer
    if total + max_val*(4-size) <= answer: # 계속해도 최대값에 못미치는 경우
        return # 종료
    if size == 4: # 4개가 모이면
        answer = max(answer, total)
        return # 종료
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if size == 2: # 'ㅜ'를 만들어주기 위해
                visited[nx][ny] = True # 방문 표시
                dfs(x, y, size + 1, total + board[nx][ny]) # 다시 기존좌표에서 시작
                visited[nx][ny] = False # back
            visited[nx][ny] = True # 방문 표시
            dfs(nx, ny, size + 1, total + board[nx][ny]) # 다음좌표로
            visited[nx][ny] = False # back

dx = [1,0,-1,0]; dy = [0,1,0,-1]
n, m = map(int, input().split())
board = [ list(map(int, input().rstrip().split())) for _ in range(n) ]
visited = [ [False]*m for _ in range(n) ]
max_val = max(map(max, board)) # 모든 좌표 중 최댓값
answer = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = True # 방문표시
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False # 제거
print(answer)