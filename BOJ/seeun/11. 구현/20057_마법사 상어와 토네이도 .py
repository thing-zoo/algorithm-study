import math
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 좌우상하 별 비율표
dirboard = [[[0,0,2,0,0], [0, 10, 7, 1, 0], [5, -1, 0, 0, 0], [0, 10, 7, 1, 0], [0, 0, 2, 0, 0]],
        [[0,0,2,0,0], [0, 1, 7, 10, 0], [0, 0, 0, -1, 5], [0, 1, 7, 10, 0], [0, 0, 2, 0, 0]],
        [[0, 0, 5, 0, 0], [0, 10, -1, 10, 0], [2, 7, 0, 7, 2], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]],
        [[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [2, 7, 0, 7, 2], [0, 10, -1, 10, 0], [0, 0, 5, 0, 0]]]

answer = 0 # 나간 모래 카운트

def move(x, y, dir): # 토네이도가 도착하는 위치
    global board, answer

    total = board[x][y] # 처음 y에 있던 모래 양 - 계산을 위해 숫자 원본 보존
    remain = board[x][y] # alpha에 들어갈 남은 모래양 계산
    board[x][y] = 0 # 위치 y의 모래 양은 0으로 처리
    alpha = [0, 0]
    i, j = 0, 0 # 비율판 탐색할 인덱스

    # 토네이도 도착 위치를 한가운데로 생각하고 5*5 비율판 탐색
    # pos_x, pos_y: 토네이도가 도착하는 x, y를 가운데로 하여 5*5판 탐색할 인덱스
    for pos_x in range(x-2, x+3, 1):
        for pos_y in range(y-2, y+3, 1):
            if dirboard[dir][i][j] > 0: # 비율이 있는 칸
                if pos_x >= 0 and pos_x < n and pos_y >= 0 and pos_y < n:  # 범위 안에 퍼지는 경우
                    board[pos_x][pos_y] += math.floor(total * (dirboard[dir][i][j]*0.01)) # 비율만큼 더하기
                else: # 범위 밖으로 나가는 경우
                    answer += math.floor(total * (dirboard[dir][i][j]*0.01)) # 비율만큼 나가기

                # 퍼진거나 나간만큼 빼기
                remain -= math.floor(total * (dirboard[dir][i][j]*0.01))

            elif dirboard[dir][i][j] == -1: # a이면 위치 기억해두기
                if pos_x >= 0 and pos_x<n and  pos_y >= 0 and pos_y < n: # 범위 안이면 alpha에 저장 가능
                    alpha = [pos_x, pos_y] # 위치 기억
                else: # 아니면 나갈 예정
                    alpha = [-1, -1] # 범위 밖으로 처리
            j = (j+1) % 5
        i += 1

    # 남은 알파 처리
    if alpha != [-1, -1]: # 알파 위치가 범위 내이면
        board[alpha[0]][alpha[1]] += remain
    else: # 알파가 범위 밖이면
        answer += remain


i = n//2 # 격자 한가운데서 시작
j = n//2
isign = 1 # i 상하 결정
jsign = -1 # j 좌우 결정
hr = True # 시작은 왼쪽(가로)으로 이동 False이면 세로이동
length = 0 # 몇칸 이동할지

while length < n:
    if hr and length != n-1: # 마지막 토네이도는 3번 이동함
            length += 1

    if hr: # 가로 이동
        for _ in range(length):
            j += jsign # j 좌/우 이동
            dir = 0
            if jsign == -1:
                dir = 0 # 왼쪽
            else:
                dir = 1 # 오른쪽
            move(i, j, dir)
        jsign *= -1 # 다음을 위해 방향 전환

    else: # 세로이동
        for _ in range(length):
            i += isign # i 상/하 이동
            dir = 0
            if isign == -1: # 위
                dir = 2
            else: # 아래
                dir = 3
            move(i, j, dir)
        isign *= -1 # 다음을 위해 방향 전환

    hr = not hr # 가로 세로 방향 전환

    if i == 0 and j == 0: # 0, 0에 도착하면 종료
        break

print(answer)