from collections import deque

jihun = deque()
fire = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
def bfs():
    global cnt
    while True:
        # 불 내기
        templen = len(fire)
        for _ in range(templen):
            fx, fy = fire.popleft()
            check = 0
            for i in range(4):
                nx = fx + dx[i]
                ny = fy + dy[i]
                if nx<0 or nx>=r or ny<0 or ny>=c:
                    continue
                if maze[nx][ny] == '#':
                    check += 1
                    continue
                if maze[nx][ny] == 'F' or maze[nx][ny] == '-1':
                    check += 1
                    continue
                if maze[nx][ny] == '.' or maze[nx][ny] == 'J': # 불 날 수 있는 곳
                    fire.append([nx, ny])
                    maze[nx][ny] = 'F'
                
        # 지훈이 움직이기
        templen = len(jihun)
        cnt += 1
        for _ in range(templen):
            x, y = jihun.popleft()
            check = 0
            already = False
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx == r or ny == c or nx < 0 or ny < 0: # 탈출했으면
                    return True
                if maze[nx][ny] == '.': # 이미 지나온 길: J으로 처리
                    jihun.append([nx, ny])
                    maze[nx][ny] = 'J'
                else: # 갈 수 있는 길 아니면 체크 +1
                    check += 1
            if check == 4 and len(jihun)==0: # check == 4 : 아무데로도 못갔으면
                return False
      
r, c = map(int, input().split())

maze = []
for i in range(r):
    maze.append(list(input()))

for i in range(r):
    for j in range(c):
        if maze[i][j] == "J": 
            jihun.append([i, j])
            
        if maze[i][j] == "F": 
            fire.append([i, j])
            
res = bfs()

if res == False:
    print("IMPOSSIBLE")
else:print(cnt)