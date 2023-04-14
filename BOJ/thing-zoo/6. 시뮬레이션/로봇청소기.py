def solution(r, c, d):
    answer = 0
    while True:
        if board[r][c] == DIRTY: # 현재칸이 청소가 되지 않았다면
            board[r][c] = CLEAN # 청소하기
            answer += 1 # 청소한 영역 세기
        dirty = False
        for i in range(4): # 주변에 청소할 칸이 있는지 확인
            nr, nc = r + dx[i], c + dy[i]
            if board[nr][nc] == DIRTY:
                dirty = True
        if not dirty: # 청소할 칸이 없으면 
            nr, nc = r - dx[d], c - dy[d]
            if board[nr][nc] == WALL: # 벽이면
                break # 종료
            else:
                r, c = nr, nc  # 후진
        else: # 청소할 칸이 있으면
            d = (d + 3)%4 # 반시계 90도 회전
            nr, nc = r + dx[d], c + dy[d] 
            if board[nr][nc] == DIRTY: # 청소되지 않은 칸이면
                r, c = nr, nc # 전진
    print(answer)

dx = [-1, 0, 1, 0]; dy = [0, 1, 0, -1]
DIRTY = 0
WALL = 1
CLEAN = 2
n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(n) ]
solution(r,c,d)