import sys
input = sys.stdin.readline

def possible(x, y): # 거리두기 확인
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    
    for i in range(4): # 상하좌우에
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= 0 or ny <= 0 or nx > n or ny > m:
            continue
        if board[nx][ny]: # 사람이 있으면
            return False # 불가능
    return True # 가능
    
def find_seat():
    if len(seated) == 0: # 모든 좌석이 비어있다면
        return (1, 1) # 첫좌석
    candi = []
    for x in range(1, n+1):
        for y in range(1, m+1):
            if not board[x][y] and possible(x, y): # 비었고 거리두기가능 좌석이면
                d = float('inf') # 안전도
                for i, j in seated.values(): # 다른사람과의 거리 중
                    d = min(d, ((x-i)**2+(y-j)**2)**0.5) # 가장 가까운 거리
                candi.append((-d, x, y)) # 정렬순서: 높은 안전도>낮은 X>낮은 Y
    candi.sort()
    if candi:
        return (candi[0][1], candi[0][2])
    else:
        return (-1, -1)
        
def seat(x, y, id):
    # 앉은 상태 표시
    board[x][y] = id
    state[id] = EATING
    seated[id] = (x, y)

def leave(x, y, id):
    # 식사 완료 표시
    board[x][y] = 0
    state[id] = AFTER
    del seated[id]

n, m, q = map(int, input().split())
board = [[0]*(m+1) for _ in range(n+1)] # 좌석표: 빈좌석(0) 앉은좌석(id값)
BEFORE = 0; EATING = 1; AFTER = 2
state = [BEFORE]*10001 # 사원의 현재 상태: 식사전(0) 식사중(1) 식사완료(2)
seated = {}

for _ in range(q):
    task, id = input().split()
    id = int(id)
    if task == 'In':
        if state[id] == EATING:
            print(f'{id} already seated.')
        elif state[id] == AFTER:
            print(f'{id} already ate lunch.')
        elif state[id] == BEFORE:
            x, y = find_seat()
            if x == y == -1:
                print('There are no more seats.')
            else:
                print(f'{id} gets the seat ({x}, {y}).')
                seat(x, y, id)
    else:
        if state[id] == BEFORE:
            print(f'{id} didn\'t eat lunch.')
        elif state[id] == AFTER:
            print(f'{id} already left seat.')
        elif state[id] == EATING:
            x, y = seated[id]
            print(f'{id} leaves from the seat ({x}, {y}).')
            leave(x, y, id)