from collections import deque
board = []
ans = 0
for _ in range(12):
    board.append(list(input()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def setting():
    global board
    for j in range(6):
        i = 11
        while i>0:
            flag = False
            if board[i][j] == ".": # 현재 지점이 빈칸이면 위에 있는 블록들 밑으로 내려야함
                for k in range(i, 0, -1):
                    if board[k-1][j] != ".":
                        flag = True
                    board[k][j] = board[k-1][j]
                    board[k-1][j] = "."
                # 위에 남은 것들이 다 .이면 끝내야함
                if flag == False:
                    break
            else: # 현재지점에 블록 있으면 윗칸 검사
                i -= 1

def bfs(x, y, color):
    global visited, flag
    queue = deque()
    
    tmp = [] # color 색 뿌요 저장하는 배열
    queue.append([x, y])
    visited[x][y] == True
    cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6:
                # 같은 색이고 아직 검사 안했으면
                if board[nx][ny] == color and visited[nx][ny] == False:
                    queue.append([nx,ny])
                    tmp.append([nx,ny])
                    visited[nx][ny] = True
                    cnt += 1 # 몇칸의 블록을 담았는지
    if cnt >= 4 :
        flag = True # 뿌요 터뜨렸으면 flag True
        for t in tmp:
            board[t[0]][t[1]] = "." # 블록 터뜨리기
        return True
    else:
        return False
        

while True:
    visited = [[False for _ in range(6)] for _ in range(12)]
    flag = False
    for i in range(11, -1, -1):
        for j in range(6):
            if visited[i][j] == False and board[i][j] != ".":
                bfs(i, j, board[i][j])

    if not flag:  # 지금 단계엥서 아무 뿌요도 못 터뜨렸으면 이제 끝
        break
    ans += 1
    setting() # 한단계 끝낸 후 블록 밑으로 정렬
print(ans)