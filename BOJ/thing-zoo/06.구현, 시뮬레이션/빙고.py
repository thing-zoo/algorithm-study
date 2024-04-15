def check_bingo():
    result = 0
    for i in range(N):
        if False not in bingo[i]:
            result += 1
    
    for j in range(N):
        flag = True
        for i in range(N):
            if not bingo[i][j]:
                flag = False
                break
        if flag: result += 1
    
    flag = True
    for i in range(N):
        if not bingo[i][i]:
            flag = False
            break
    if flag: result += 1
    
    flag = True
    for i in range(N):
        if not bingo[i][N-1-i]:
            flag = False
            break
    if flag: result += 1
    
    if result >= 3:
        return True
    else:
        return False

N = 5
pos = {}
bingo = [[False]*N for _ in range(N)]
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        pos[temp[j]] = (i, j)

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        x, y = pos[temp[j]]
        bingo[x][y] = True
        if check_bingo():
            print(i*N+j+1)
            exit(0)