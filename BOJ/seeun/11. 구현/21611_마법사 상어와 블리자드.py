N, M = map(int, input().split())
beads = [list(map(int, input().split())) for _ in range(N)]
blizzard_list = [list(map(int, input().split())) for _ in range(M)]
ans = [0, 0, 0, 0]

numTOloc = {} # 칸 번호 별 좌표 저장
locTOnum = {}
i = N//2 # 격자 한가운데서 시작
j = N//2
isign = 1 # i 상하 결정
jsign = -1 # j 좌우 결정
hr = True # 시작은 왼쪽(가로)으로 이동 False이면 세로이동
length = 0 # 몇칸 이동할지
cnt = 1 # 칸 번호

while length < N*N+1:
    if hr and length != N-1: # 마지막 토네이도는 3번 이동함
            length += 1

    if hr: # 가로 이동
        for _ in range(length):
            j += jsign # j 좌/우 이동
            numTOloc[cnt] = [i, j]
            locTOnum[(i, j)] = cnt
            cnt += 1
        jsign *= -1 # 다음을 위해 방향 전환

    else: # 세로이동
        for _ in range(length):
            i += isign # i 상/하 이동
            numTOloc[cnt] = [i, j]
            locTOnum[(i, j)] = cnt
            cnt += 1
        isign *= -1 # 다음을 위해 방향 전환

    hr = not hr # 가로 세로 방향 전환

    if i == 0 and j == 0: # 0, 0에 도착하면 종료
        break

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

def blizzard(d, s):
    broken = []
    for i in range(1, s+1):
        nx = N//2 + dx[d]*i
        ny = N//2 + dy[d]*i
        beads[nx][ny] = 0
        broken.append([locTOnum[(nx, ny)], 1]) # 공격받은 위치, 연속된 구슬 개수
    return broken # 구슬이 없는 곳 위치 반환 -> 구슬 세팅할 때 활용

def init(broken): # 빈칸이 있을 때 메우는 함수 - 공격받은 위치 리스트 받음
    global beads
    broken.sort(reverse = True)# 바깥에 있는 빈칸부터 메워줘야함

    for i in range(len(broken)):
        tmp = numTOloc[broken[i][0]] # 빈칸 위치
        x, y = tmp[0], tmp[1]

        # 빈칸 ~ 마지막 숫자 빈 구간 만큼 앞으로 당겨줌
        for j in range(broken[i][0], N*N-broken[i][1]):
            x2, y2 = numTOloc[j+broken[i][1]] # 이 숫자를
            x1, y1 = numTOloc[j] # 여기에 저장
            beads[x1][y1] = beads[x2][y2]

        # 당기고 남은 숫자들은 0으로 리셋
        for j in range(N*N-broken[i][1], N*N, 1):
            x, y = numTOloc[j]
            beads[x][y] = 0
        


def find_seq(): # 연속된 구슬 찾기 , 폭발한거 개수 카운트 해야됨
    same = [] # 연속된 구슬 칸 번호 저장
    prev = 0 # 이전 구슬 번호
    broken = []
    for i in range(1, N*N):
        x, y = numTOloc[i] # 해당 번호의 위치
        if beads[x][y] == prev: # 이전 구슬과 같으면
            same.append(i) # 번호가 같은 구슬 위치번호 저장
        else: # 이전구슬 이랑 달라졌으면
            if len(same) >= 4: # 이전까지 연속된 구슬 개수가 4개 이상이었으면 폭발함
                broken.append([min(same),  len(same)]) # 폭발한 시작위치와 연속된 구슬 개수 저장
                ans[prev] += len(same) # 폭발한 구슬 개수 정답 저장
            prev = beads[x][y]
            same = [i]
    return broken

def change_beads(): # 구슬 재배열
    new_beads = [[0]*N for _ in range(N)]
    idx = 1 # new_beads를 탐색할 인덱스
    i = 1 # 기존 beads를 탐색할 인덱스
    x, y = numTOloc[i] # 해당 번호의 위치
    nextx, nexty = numTOloc[i+1]
    A = 1 # 구슬 개수
    B = beads[x][y] # 구슬 종류

    # 두 배열중 하나라도 마지막까지 갔으면 종료
    while idx < N*N-1 and i < N*N-1:
        x, y = numTOloc[i] # 해당 번호의 위치
        nextx, nexty = numTOloc[i+1]
        if beads[x][y] == 0:
            break

        # 다음구슬과 다를 때 까지 진행
        while beads[x][y] == beads[nextx][nexty] and i < N*N-1:
            A += 1
            B = beads[x][y]

            i += 1
            x, y = numTOloc[i] # 해당 번호의 위치
            nextx, nexty = numTOloc[i+1]
        
        if A == 1: # 바로 다음거랑 다른 구슬이면
            B = beads[x][y]
        
        # new_beads에 차례대로 저장
        if idx+1 <= N*N-1:
            ax, ay = numTOloc[idx]
            bx, by = numTOloc[idx+1]
        else:
            break
        new_beads[ax][ay] = A
        new_beads[bx][by] = B
        idx += 2
        A = 1
        B = 0
        i += 1
    return new_beads

for d, s in blizzard_list:
    broken = blizzard(d, s) # 블리자드 쏘기
    init(broken) # 빈칸 메우기

    while True: # 폭발할 구슬이 없을 때까지 폭발 - 메우기 반복
        broken = find_seq() # 연속된 구슬 찾기
        if len(broken) == 0:
            break
        init(broken) # 빈칸 메우기

    beads = change_beads() # 구슬 재배열

print(ans[1]+ans[2]*2 + ans[3]*3)