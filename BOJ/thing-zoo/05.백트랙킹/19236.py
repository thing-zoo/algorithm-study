size = 4
# 방향: 0~7, 상부터
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
board = [[0]*size for _ in range(size)] # board[x][y]=물고기 번호
fish = [[]]*(size**2+1) # i번째 물고기 (x,y,d,live)
answer = 0 # 상어가 먹을 수 있는 물고기 번호의 합의 최댓값
def move_fish(a, b, board, fish):
    for i in range(1, size**2+1): # 번호가 작은 물고기부터 이동
        x, y, d, live = fish[i]
        if not live: continue # 죽은 물고기
        for _ in range(8): # 이동가능할때까지
            nx = x + dx[d]
            ny = y + dy[d]
            if (nx < 0 or nx >= size or ny < 0 or ny >= size) or (nx == a and ny == b): # 범위 밖이거나 상어면
                d = (d + 1) % 8  # 다음 방향 45도 반시계 회전
                continue
            # 서로 변경
            j = board[nx][ny]
            fish[i][0], fish[i][1], fish[i][2] = nx, ny, d # 위치, 방향도 변경
            if j != 0: fish[j][0], fish[j][1] = x, y
            board[x][y], board[nx][ny] = j, i
            break

def dfs(x, y, board, fish, eat):
    global answer

    n = board[x][y] # 물고기 번호
    d = fish[n][2]  # 물고기 방향
    board[x][y] = 0 # 물고기 먹기
    fish[n][3] = False # 물고기 죽음 표시
    eat += n
    answer = max(answer, eat)
    move_fish(x, y, board, fish) # 물고기 이동

    for i in range(1, size): # 상어는 최대 size-1칸 이동 가능
        nx = x + dx[d]*i
        ny = y + dy[d]*i
        if nx < 0 or nx >= size or ny < 0 or ny >= size: break # 범위 밖이면 종료
        if board[nx][ny] == 0: continue # 물고기 없는칸 이동불가

        copy_graph = [board[i][:] for i in range(size)]
        copy_fish = [fish[i][:] for i in range(size ** 2 + 1)]
        dfs(nx, ny, copy_graph, copy_fish, eat) # 이동

# 입력 받기
for i in range(size):
    data = list(map(int, input().split()))
    for j in range(0, 2*size, 2):
        n, d = data[j], data[j+1] # 물고기번호, 방향(1~8)
        board[i][j//2] = n
        fish[n] = [i, j//2, d-1, True] # (x,y,d,live)

# 로직 수행
dfs(0, 0, board, fish, 0)
print(answer)