import sys
from collections import deque
input = sys.stdin.readline
r, c, n = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
time = [[0] * c for _ in range(r)]

for i in range(r): # 폭탄 초기 시간 세팅
    for j in range(c):
        if board[i][j] == 'O':
            time[i][j] = 2

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def setbomb(): # 없는 곳은 폭탄 놓기, 있는 곳은 시간 줄이기
    for i in range(r):
        for j in range(c):
            if board[i][j] == '.':
                time[i][j] = 3
                board[i][j] = 'O'
            else:
                time[i][j] -= 1

def explode(candi): # 터질 폭탄 위치를 받아서 터뜨리기
    for tmp in candi:
        x, y = tmp[0], tmp[1]
        board[x][y] = '.'
        time[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                board[nx][ny] = '.'
                time[nx][ny] = 0

t = 1         
while t < n:
    setbomb()
    t += 1
    if t == n:
        break

    candi = []
    for i in range(r):
        for j in range(c):
            if time[i][j] > 0: # 폭탄이 있으면 시간 줄이기
                time[i][j] -= 1
            if time[i][j] == 0 and board[i][j] == 'O': # 터져야할 폭탄이면 터질 폭탄 리스트에 넣기
                candi.append([i, j])
    explode(candi) # 실제 폭발 적용하는 함수
    t += 1
    if t == n:
        break

for i in range(r):
        print("".join(board[i]))