n, m = map(int, input().split())
nums = list(map(int, input().split()))
board = [[0 for _ in range(m)] for _ in range(n)]
for j in range(m):
    h = nums[j]
    for t in range(n-1, n-h-1, -1):
        board[t][j] = 1 # 블록이 있는 자리는 1로 처리

ans = 0
for i in range(n):
    j = 0
    while j < m:
        cnt = 0
        if board[i][j] == 1: # 현재 블록이 있는 곳이면 옆으로 물이 고일 수 있으므로 체크
            j += 1 # 블록 옆칸에서 부터 카운트 시작
            while j < m and board[i][j] != 1: # 또다른 블록을 만나거나 낭떠러지를 만나면 종료
                j += 1
                cnt += 1
            if j == m: # 낭떠러지면 pass
                continue
            elif board[i][j] == 1: # 또다른 블록을 만났으면 빗물이 고인 만큼 저장
                ans += cnt
        else: # 블록이 없는 칸이면 인덱스 옆으로 이동
            j += 1

print(ans)