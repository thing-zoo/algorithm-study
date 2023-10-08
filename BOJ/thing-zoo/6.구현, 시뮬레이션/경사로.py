def isPassable(road): # 해당 길을 지나갈 수 있는지 확인 하는 함수
    ramps = [False]*N # 경사로 존재 여부
    for i in range(N-1):
        if abs(road[i] - road[i+1]) > 1: # 높이차가 1보다 크면
            return False # 불가능
        if road[i] < road[i+1]: # 앞으로 경사로 확인
            for k in range(L):
                if i-k < 0 or ramps[i-k] or road[i] != road[i-k]: # 범위가 아니거나 경사로가 있거나 높이가 다르면
                    return False # 불가능
                if road[i] == road[i-k]: # 높이가 같으면
                    ramps[i-k] = True # 경사로 설치
        elif road[i] > road[i+1]: # 뒤로 경사로 확인
            for k in range(L):
                if i+1+k >= N or ramps[i+1+k] or road[i+1] != road[i+1+k]: # 범위가 아니거나 경사로가 있거나 높이가 다르면
                    return False # 불가능
                if road[i+1] == road[i+1+k]: # 높이가 같으면
                    ramps[i+1+k] = True # 경사로 설치
    return True

def solution():
    count = 0
    for i in range(N): # 가로 길 확인
        if isPassable(board[i]): count += 1
    for i in range(N): # 세로 길 확인
        if isPassable([ board[j][i] for j in range(N) ]): count += 1
    print(count)
board = []
N, L = map(int, input().split())
for _ in range(N):
    board.append(list(map(int, input().split())))
solution()