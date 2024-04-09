from itertools import permutations
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
origin = [list(map(int, input().split())) for _ in range(n)]

def rotate_right(r, c, s, t):
    global board

    tmp = board[r-s+t][c-s+t] # 테두리의 가장 왼쪽위에 있는 숫자 임시 저장

    # 좌
    for i in range(r-s+t, r+s-t):
        board[i][c-s+t] = board[i+1][c-s+t]
    # 하
    for j in range(c-s+t, c+s-t):
        board[r+s-t][j] = board[r+s-t][j+1]
    # 우
    for i in range(r+s-t, r-s+t, -1):
        board[i][c+s-t] = board[i-1][c+s-t]
    # 상
    for j in range(c+s-t, c-s+t+1, -1):
        board[r-s+t][j] = board[r-s+t][j-1]

    board[r-s+t][c-s+t+1] = tmp # 임시 저장한 수 옮기기

def calcul(board):
    ans = float('inf')
    for b in board:
        ans = min(ans, sum(b))
    return ans

minnum = float('inf')
lst = [list(map(int, input().split())) for _ in range(k)]
for combi in permutations(range(k), k): # 0~k-1까지 숫자 순열
    board = [origin[i][:] for i in range(n)] # 원본 배열 복사해서 사용
    for c in combi: # 순열 순서대로 회전연산 수행
        r, c, s = lst[c][0]-1, lst[c][1]-1, lst[c][2]
        for t in range((2*s+1)//2): # t: 몇번째 테두리인지(0~)
            rotate_right(r, c, s, t)

    minnum = min(calcul(board), minnum)

print(minnum)