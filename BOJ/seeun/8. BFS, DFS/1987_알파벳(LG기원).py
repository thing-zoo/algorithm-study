import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
board = [list(input().rstrip()) for _ in range(n)]

ans = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def dfs(x, y, leng):
    global ans
    
    ans = max(ans, leng) # 정답 갱신
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            s = board[nx][ny]
            if not visited[ord(s)-ord('A')]: # 아직 방문하지 않은 알파벳이면
                visited[ord(s)-ord('A')] = True
                dfs(nx, ny, leng+1)
                visited[ord(s)-ord('A')] = False
            else: # 이미 방문한곳이라서 못감
                cnt += 1
        else: # 범위 밖이라서 못감
            cnt += 1
    
    # 아무곳도 못가면 끝
    if cnt == 4:
        return

visited = [False] * (ord('Z') - ord('A')+1)
visited[ord(board[0][0])-ord('A')] = True
dfs(0, 0, 1)
print(ans)