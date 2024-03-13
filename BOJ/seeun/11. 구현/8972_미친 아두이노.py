from collections import defaultdict

def find_dir(x, y): # 미친 아두이노가 이동할 위치 반환
    mindist, mindir = 1000000, 1000000
    for i in range(1, 10):
        nx = x + dx[i]
        ny = y + dy[i]
        if  0 <= nx < N and 0 <= ny < M:
            if abs(js[0] - nx) + abs(js[1] - ny) < mindist:
                mindist = abs(js[0] - nx) + abs(js[1] - ny)
                mindir = i
    return [x + dx[mindir], y + dy[mindir]]

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
dir = list(map(int, list(input())))

dx = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]

# 초기 종수, 미친 아두이노 위치 정보 저장
crazy = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'I':
            js = [i, j]
        if board[i][j] == 'R':
            crazy.append([i, j])

ans = True
for i in range(len(dir)):
    tmpboard = [['.'] * M for _ in range(N)]

    # 1. 종수 아두이노 이동
    d = dir[i]
    nx = js[0] + dx[d]
    ny = js[1] + dy[d]

    # 2. 이동한 곳에 미친 아두이노가 있으면 끝
    if board[nx][ny] == 'R':
        ans = False
        break
    else:
        tmpboard[nx][ny] = 'I'
        js = [nx, ny]

    # 3. 미친 아두이노 이동
    bomb = defaultdict(int)
    for c in range(len(crazy)):
        nx, ny = find_dir(crazy[c][0], crazy[c][1])
        if tmpboard[nx][ny] == 'I': # 4. 종수 아두이노와 만나면 끝
            ans = False
            break
        elif tmpboard[nx][ny] == 'R': # 같은 위치에 있는 아두이노는 다 폭파
            bomb[(nx, ny)] += 1 # 터뜨릴 곳 위치, 개수 저장
            crazy[c] = [nx, ny] # 이동한 위치 갱신
        else:
            tmpboard[nx][ny] = 'R'
            crazy[c] = [nx, ny] # 이동한 위치 갱신
    if not ans: # 게임 끝이면 종료
        break

    # 5. 같은 칸에 있는 미친 아두이노 폭파
    for b in bomb.keys():
        x, y = b[0], b[1]
        tmpboard[x][y] = '.' # 겹친 곳 없애기
        for _ in range(bomb[b]+1):
            crazy.remove([x, y]) # 동시에 있었던 미친 아두이노 다 삭제
    
    # tmpboard를 board에 복사
    board = [tmpboard[k][:] for k in range(N)]

if not ans:
    print('kraj', i+1)
else:
    for i in range(N):
        print("".join(board[i]))