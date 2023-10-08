def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    tmp = [[0]*(m+1) for _ in range(n+1)] # 공격, 회복 상태를 저장할 배열

    for a, x1, y1, x2, y2, cnt in skill:
        # 1이면 적의 공격 2이면 아군의 회복
        if a == 1:
            cnt *= -1
        tmp[x1][y1] += cnt
        tmp[x1][y2+1] -= cnt
        tmp[x2+1][y1] -= cnt
        tmp[x2+1][y2+1] += cnt
    
    # 가로로 누적합
    for i in range(n+1):
        for j in range(1,m+1):
            tmp[i][j] += tmp[i][j-1]

    # 세로로 누적합
    for i in range(1, n+1):
        for j in range(m+1):
            tmp[i][j] += tmp[i-1][j]

    # board에 공격회복 상태 반영
    for i in range(n):
        for j in range(m):
            board[i][j] += tmp[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer

solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])