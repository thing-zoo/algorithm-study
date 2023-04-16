from collections import deque
def roll(dir): # dir방향에 따라 주사위 굴리기
    if dir == 1: # 동
        dice_h.rotate(1)
        temp = dice_h[0]
        dice_h[0] = dice_v[3]
        dice_v[3] = temp
        dice_v[1] = dice_h[1]
    elif dir == 2: # 서
        dice_h.rotate(-1)
        temp = dice_h[2]
        dice_h[2] = dice_v[3]
        dice_v[3] = temp
        dice_v[1] = dice_h[1]
    elif dir == 3: # 북
        dice_v.rotate(-1)
        dice_h[1] = dice_v[1]
    else: # 남
        dice_v.rotate(1)
        dice_h[1] = dice_v[1]

def solution(x, y):
    for dir in dirs: # 명령에 대해
        nx, ny = x + dx[dir-1], y + dy[dir-1] # 다음위치 이동
        if 0 <= nx < n and 0 <= ny < m: # 유효한 범위 내면
            roll(dir) # 굴리기
            if maps[nx][ny]: # 지도값이 0이 아니면
                dice_v[3] = maps[nx][ny] # 지도값을 주사위밑면에 복사
                maps[nx][ny] = 0 # 지도값은 0으로
            else: # 지도값이 0이면
                maps[nx][ny] = dice_v[3] # 주사위 밑면값을 지도에 복사
            x, y = nx, ny            
            print(dice_v[1]) # 주사위 윗면 출력

dice_h = deque([0]*3)
dice_v = deque([0]*4)
dx = [0, 0, -1, 1]; dy = [1, -1, 0, 0]
n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dirs = list(map(int, input().split()))
solution(x, y)