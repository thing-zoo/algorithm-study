# 반시계 방향
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
air_cleaner = []
r, c, t = map(int, input().split())
a = []
for x in range(r):
    a.append(list(map(int, input().split())))
    if a[x][0] == -1:
        air_cleaner.append((x, 0))
def spread(): # 미세먼지 확산
    # 확산되는 미세먼지 양 구하기
    temp = [[0]*c for _ in range(r)] # 동시확산을 위해 따로 저장
    for x in range(r):
        for y in range(c):
            if a[x][y] <= 0: continue # 미세먼지가 아니면 넘기기

            amount = a[x][y]//5
            count = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= r or ny < 0 or ny >= c or a[nx][ny] == -1: # 범위 밖이거나 공기청정기면 확산안함
                    continue
                temp[nx][ny] += amount
                count += 1
            a[x][y] = max(a[x][y] - amount*count, 0) # 확산된거 제거

    # 확산된 미세먼지 반영하기
    for x in range(r):
        for y in range(c):
            a[x][y] += temp[x][y]

def do_air_cleaner(target, up): # 공기청정기 작동
    if up: s = 1 # 위쪽은 반시계(그대로)
    else: s = -1 # 아래쪽은 시계(r 방향만 바꿔주면 됨)

    x, y = target
    i = 0 # 방향
    pre = 0 # 이전 값(맨 첫칸은 0으로 없애줘야함)
    while True:
        nx = x + dx[i]*s
        ny = y + dy[i]
        if nx == target[0] and ny == target[1]: # 자기자신을 만나면 종료
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c: # 범위밖이면 회전
            i += 1
            continue
        a[nx][ny], pre = pre, a[nx][ny]
        x, y = nx, ny

for _ in range(t): # t초만큼 수행
    spread()
    do_air_cleaner(air_cleaner[0], True)
    do_air_cleaner(air_cleaner[1], False)

answer = 0 # 남은 미세먼지 양
for x in range(r):
    for y in range(c):
        if a[x][y] <= 0: continue  # 미세먼지가 아니면 넘기기
        answer += a[x][y]
print(answer)