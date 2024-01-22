def dfs(x, y, dist):
    global answer

    answer = max(dist, answer)
    if len(alpha) == answer: # 가능한 최대 알파벳 수에 도달하면 종료
        print(answer)
        exit(0)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if not alpha[ord(board[nx][ny])]: # 같은 알파벳이 아니면
            alpha[ord(board[nx][ny])] = 1
            dfs(nx, ny, dist + 1)
            alpha[ord(board[nx][ny])] = 0 # 다른루트가 포함할 수 있도록 제거


dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

r, c = map(int, input().split())
board = [ ] # 격자판
alpha = { } # 알파벳 방문 표시
for _ in range(r):
    temp = list(input())
    for i in temp:
        alpha[ord(i)] = 0
    board.append(temp)
alpha[ord(board[0][0])] = 1
answer = 0 # 말이 지날 수 있는 최대 칸 수
dfs(0, 0, 1) # 출발칸도 칸수에 포함
print(answer)