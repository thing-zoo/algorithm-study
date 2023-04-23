from itertools import combinations
def check(): # k번 세로선의 결과가 k인지 확인하는 함수
    for k in range(n): # 세로선 순서대로
        j = k # 세로선
        for i in range(h): # 가로선
            if board[i][j]:
                j += 1 # 옆으로
            elif j > 0 and board[i][j-1]:
                j -= 1
        if k != j: # 세로선의 결과가 다르면
            return False
    return True

def dfs(bridge_count, x, y):
    global answer
    if answer <= bridge_count: # 최소값이상이면
        return # 종료
    if check(): # 모든 세로선이 올바른 결과면
        answer = min(answer, bridge_count) # 최소값 갱신
        return # 종료
    if bridge_count == 3: # 추가 가로선 3개이상이면
        return # 종료
    for i in range(x, h): # 가로선 이동
        if i == x: k = y    # 같은행이면 계속해서 확인
        else: k = 0         # 다른행이면 처음부터 확인
        for j in range(k, n-1): # 세로선 이동
            if (j > 0 and board[i][j-1]) or board[i][j+1]: # 양쪽에 가로선이 있으면
                continue
            if not board[i][j]:
                board[i][j] = True
                dfs(bridge_count + 1, i, j + 2) # 가로선 겹치지 않게 j+2
                board[i][j] = False 

n, m, h = map(int, input().split()) # n: 세로선, m: 가로선, h: 가능한 가로선 개수
board = [[False]*n for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    board[a-1][b-1] = True # 사다리 놓기

answer = 4
dfs(0, 0, 0)
print(answer if answer <= 3 else -1)