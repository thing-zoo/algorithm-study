def reverse_dir(dir):
    if dir == 1:
        return 2
    elif dir == 2:
        return 1
    elif dir == 3:
        return 4
    elif dir == 4:
        return 3

def move_horse(i):
    # 이동할 말의 위치, 방향 정보
    x, y, d = info[i][0], info[i][1], info[i][2]

    num = horse[x][y].index(i) # i번 말이 몇번째에 깔려있는지 찾기
    horse_list = horse[x][y][num:] # i번 말 포함 위에 올려진 말 모두 가져오기
    horse[x][y] = horse[x][y][:num] # 이동한 말들 제외하고 남은 말만 남겨두기
    
    # 이동할 위치 계산
    nx, ny = x + dx[d], y + dy[d]

    # 체스판을 벗어나거나 파란색 칸
    if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2: 
        d = reverse_dir(d) # 방향 전환
        nx, ny = x + dx[d], y + dy[d] # 이동할 위치 재계산(반대방향으로)

        if not(0 <= nx < N and 0 <= ny < N) or board[nx][ny] == 2: # 이동하려는 곳이 파란색이면 제자리에 있기
            nx, ny = x, y
        elif board[nx][ny] == 1: # 이동하려는 곳이 파란색이면 reverse
            horse_list.reverse()

    # 빨간색 칸
    elif board[nx][ny] == 1: 
        horse_list.reverse() # 이동할 말만 reverse

    # 최종적으로 말 이동
    horse[nx][ny] += horse_list

    # 말 정보 갱신
    info[i][0], info[i][1], info[i][2] = nx, ny, d # i번 말
    for h in horse_list: # 위에 올려져있는 말 정보도 수정
        info[h][0], info[h][1] = nx, ny
    
    return len(horse[nx][ny]) # i번째 말 이동 한 곳의 말 개수 반환

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
horse = [[[] for _ in range(N)] for _ in range(N)]
info = [[]]

# 초기 말 세팅
for i in range(1, K+1):
    x, y, d = map(int, input().split())
    horse[x-1][y-1].append(i)
    info.append([x-1, y-1, d])

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]  
    
t = 1
ans = -1
while t <= 1000:
    for i in range(1, K+1):
        if move_horse(i) >= 4: # i번째 말 이동
            ans = t
    t += 1
    if ans != -1:
        break

print(ans)