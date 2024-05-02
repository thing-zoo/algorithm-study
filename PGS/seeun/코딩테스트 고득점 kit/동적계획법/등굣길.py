def solution(m, n, puddles):
    board = [[0] * m for _ in range(n)]
    board[0][0] = 1 # 시작지점 1로 초기화

    for i in range(n):
        for j in range(m):
            if [j+1, i+1] in puddles: # 웅덩이면 계산 X
                continue
            if 0 <= i-1 < n: # 위쪽에서 내려오는 방법 있으면
                board[i][j] += board[i-1][j] % 1000000007
            if 0 <= j-1 < m: # 왼쪽에서 오는 방법 있으면
                board[i][j] += board[i][j-1] % 1000000007
        board[i][j] %= 1000000007
        
    return board[n-1][m-1]