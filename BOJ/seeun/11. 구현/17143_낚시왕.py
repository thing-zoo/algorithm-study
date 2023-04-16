UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4

# 이동후 위치 계산하는 함수
def get_next_loc(i, j, speed, dir):

    if dir == UP or dir == DOWN:  # i
        cycle = n * 2 - 2
        if dir == UP:
            speed += 2 * (n - 1) - i
        else:
            speed += i

        speed %= cycle
        if speed >= n:
            return (2 * n - 2 - speed, j, UP)
        return (speed, j, DOWN)

    else:  # j
        cycle = m * 2 - 2
        if dir == LEFT:
            speed += 2 * (m - 1) - j
        else:
            speed += j

        speed %= cycle
        if speed >= m:
            return (i, 2 * m - 2 - speed, LEFT)
        return (i, speed, RIGHT)

def move():
    global sharks
    new_sharks = [[0 for _ in range(m)] for _ in range(n)] # 이동한 상태의 상어 위치 담음
    for x in range(n):
        for y in range(m):
            if sharks[x][y] != 0: # 상어가 있으면
                speed = sharks[x][y][0]
                dir = sharks[x][y][1]
                nx, ny, ndir = get_next_loc(x, y, speed, dir)  # 다음 위치를 받아옴
                if new_sharks[nx][ny] != 0: # 만약 이동한 칸에 상어가 있으면
                    new_sharks[nx][ny] = max(new_sharks[nx][ny],(sharks[x][y][0], ndir, sharks[x][y][2]),key=lambda x: x[2],) # 둘중에 크기가 더 큰걸 기준으로 집어넣음
                else:
                    new_sharks[nx][ny] = [sharks[x][y][0], ndir, sharks[x][y][2]] # 없으면 그냥 넣기
    sharks = new_sharks
       
def fishing(idx):
    global basket
    j = idx
    for i in range(n): # 낚시왕의 위치에서 가장 가까운 상어 찾기
        if sharks[i][j] != 0:
            basket += sharks[i][j][2] # 잡은 상어의 크기 더하기
            sharks[i][j] = 0 # 상어 없애기
            break
    # 상어 이동하기
    move()

# Main                    
n, m, shark_num = map(int, input().split())
sharks = [[0 for _ in range(m)] for _ in range(n)]
basket = 0

for i in range(shark_num):
    x, y, speed, dir, size = map(int, input().split())
    x -=1
    y -=1
    sharks[x][y] = [speed, dir, size]

# 열 개수만큼 진행
for i in range(m):
    fishing(i)
print(basket)