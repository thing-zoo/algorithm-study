def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])
    answer = 0
    while True:
        change = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != '.':
                    if board[i][j] == board[i][j+1]: # 옆에 있는 블록이 나랑 같으면
                        if board[i][j] == board[i+1][j] == board[i+1][j+1]: # 아래에 있는 두개의 블록도 확인
                            change.add((i, j))
                            change.add((i+1, j))
                            change.add((i, j+1))
                            change.add((i+1, j+1))
        
        # 하나도 터질 블록이 없으면 종료
        if len(change) == 0:
            break
            
        # 터질 블록 갯수 정답에 더하기
        answer += len(change)

        # 터질 블록들 터짐으로 처리
        for c in change:
            board[c[0]][c[1]] = '.'
        
        # 블록 재정리
        init(board, n, m)

    return answer

def init(board, n, m):
    for j in range(n):
        i = m-1
        while i>0:
            flag = False
            if board[i][j] == ".": # 현재 지점이 빈칸이면 위에 있는 블록들 밑으로 내려야함
                for k in range(i, 0, -1):
                    if board[k-1][j] != ".":
                        flag = True
                    board[k][j] = board[k-1][j]
                    board[k-1][j] = "."
                # 위에 남은 것들이 다 .이면 끝내야함
                if flag == False:
                    break
            else: # 현재지점에 블록 있으면 윗칸 검사
                i -= 1        

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))