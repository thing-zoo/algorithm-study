N = int(input())
init = [list(map(int, input().split())) for _ in range(N)]


def rotate(board):
    new = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new[j][N-i-1] = board[i][j]
    return new

def block_push(board): # board를 왼쪽으로 미는 함수
    new = [[0]*N for _ in range(N)]
    for i in range(N):
        stack = []
        idx = 0
        for j in range(N):
            if board[i][j]: # 숫자가 있는 부분을 stack에 담음
                stack.append(board[i][j])

		# 스택에 있는 숫자를 new에 담아주기
        j = 0
        while j < len(stack):
            if j < len(stack)-1 and stack[j] == stack[j+1]: # 두 블록이 같으면
                new[i][idx] = stack[j]+stack[j+1] # 더해서 new[i][idx]에 저장
                j += 2 # 두칸 이동
            else: # 두 블록이 다르면 그냥 담음
                new[i][idx] = stack[j]
                j += 1
            idx += 1
    return new

ans = 0
def dfs(board, cnt):
    global ans

    if cnt >= 5:
        tmp = 0
        for i in range(N):
            t = max(board[i])
            tmp = max(t, tmp)

        ans = max(ans, tmp)
        return

    for i in range(4): # 4방향으로 밀어보기
        new = [board[i][:] for i in range(N)]
        for _ in range(i):
            new = rotate(new)

        new = block_push(new)
        dfs(new, cnt + 1)

dfs(init, 0)
print(ans)