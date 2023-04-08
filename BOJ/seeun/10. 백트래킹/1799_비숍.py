import sys
input = sys.stdin.readline

def block(x, y, n): 
    for i in range(N):
        if x-i >=0 and y-i >=0:
            temp[x-i][y-i] += n # 대각선에 비숍이 하나 있으면
        if x+i<N and y+i<N:
            temp[x+i][y+i] += n
        if x-i >=0 and y+i <N:
            temp[x-i][y+i] += n
        if x+i<N and y-i>=0:
            temp[x+i][y-i] += n       
    return True

def check(x, y): # 그 자리가 괜찮은 자리인지 확인하는 함수
    if temp[x][y]:
        return False
    return True

def bishop(i, cnt):
    global res
    if i >= len(bnw):
        res = max(cnt, res)
        return

    x, y = bnw[i]

    if check(x, y) : # 대각선에 아직 비숍이없고 방문하지 않았다면
        block(x, y, 1) # x, y 자리와 관련된 대각선들 막기
        bishop(i+1, cnt+1) # 다음 자리 확인하러 감
        block(x, y, -1)
        bishop(i+1, cnt)
    else:
        bishop(i+1, cnt)
    
# Main
N = int(input())
board = []
visited = [[False]*N for _ in range(N)]
cnt = 0
res = 0
bnw = []

for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

# 흰색 부분, 비숍을 놓을 수 있는 위치만 담음
temp = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            if (i+j)%2 == 0:
                bnw.append([i, j])
bishop(0, 0)
res1 = res

# 검은색 부분, 비숍을 놓을 수 있는 위치만 담음
res = 0
bnw = []
temp = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            if (i+j)%2 == 1:
                bnw.append([i, j])
bishop(0, 0)
res2 = res

print(res1+res2)