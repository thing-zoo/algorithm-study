n = int(input())
board = [[0] * n for _ in range(n)]
info = [[] for _ in range(n*n+1)] # i가 좋아하는 친구 정보
nums = []
for _ in range(n*n):
    s, a, b, c, d = map(int, input().split())
    nums.append(s)
    info[s] = [a, b, c, d]

board[1][1] = nums[0] # 첫 자리는 무조건 1, 1
empty = [[True]*n for _ in range(n)]
empty[1][1] = False
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(1, n*n):
    candi = [] # 자리 후보
    for x in range(n):
        for y in range(n):
            frd, emp = 0, 0
            if not empty[x][y]: # 이미 배치된 자리이면 패스
                continue
            for t in range(4):
                nx = x + dx[t]
                ny = y + dy[t]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if board[nx][ny] in info[nums[i]]: # 주변에 nums[i]가 좋아하는 친구가 있으면
                    frd += 1
                elif board[nx][ny] == 0: # 주변에 빈칸이 있으면
                    emp += 1
            candi.append([frd, emp, x, y])

                

    candi.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    board[candi[0][2]][candi[0][3]] = nums[i]
    empty[candi[0][2]][candi[0][3]] = False

   

ans = 0
for x in range(n):
    for y in range(n):
        cnt = 0
        i = board[x][y]
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] in info[i]: # 주변에 nums[i]가 좋아하는 친구가 있으면
                cnt += 1
            # 1이면 1, 2이면 10, 3이면 100, 4이면 1000
        if cnt == 1:
            ans += 1
        elif cnt == 2:
            ans += 10
        elif cnt == 3:
            ans += 100
        elif cnt == 4:
            ans += 1000
print(ans)