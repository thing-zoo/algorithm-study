import copy
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cctv = []
dir = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [3, 0]], [[0, 1, 2], [1, 2, 3], [2, 3, 0], [0, 1, 3]], [[0, 1, 2, 3]]]
wide = max(n, m)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for i in range(n):
    for j in range(m):
        if 1 <= board[i][j] <= 5:
            cctv.append([board[i][j], i, j]) # cctv 종류, 좌표

ans = float('inf') # 사각지대의 개수
def find_blind(board):
    tmp = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                tmp += 1
    
    return tmp

def sight(x, y, dir, board): # 현재 카메라가 dir 방향을 볼때 board 수정
    board = [board[i][:] for i in range(n)]

    for d in dir: # 시야 개수 만큼 반복
        nx, ny = x, y
        for _ in range(1, wide): # 격자 내에서 더 넓은 범위 검사
            nx += dx[d]
            ny += dy[d]
            if 0 <= nx < n and 0 <= ny < m: # 모두 격자 이내이면
                if board[nx][ny] == '#' or 1 <= board[nx][ny] <= 5: # 이미 감시되고 있거나 다른 카메라가 있는 곳이면
                    continue
                elif board[nx][ny] == 6: # 벽을 만났으면 이 방향 검사 종료
                    break
                elif board[nx][ny] == 0: # 빈칸이면
                    board[nx][ny] = '#'
    return board


# 현재 보드 상태, 검사할 cctv 번호
def detect(board, cnt):
    global ans

    # 모든 cctv를 다 확인했으면 정답 갱신
    if cnt == len(cctv):
        tmp = find_blind(board)
        ans = min(ans, tmp)
        return

    board = [board[i][:] for i in range(n)]
    k, x, y = cctv[cnt][0], cctv[cnt][1], cctv[cnt][2]

    # 현재 검사할 카메라를 여러각도로 돌려서 감시함
    for d in dir[k]: # 해당 카메라가 볼 수 있는 시야의 종류
        new_board = sight(x, y, d, board)

        detect(new_board, cnt+1)

detect(board, 0)
print(ans)