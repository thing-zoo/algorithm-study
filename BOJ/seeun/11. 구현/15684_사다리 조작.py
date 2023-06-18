# 현재 상태에서 모든 사다리가 자기 위치에 도착하는지 확인
def check():
    for i in range(n): # 라인별로 반복문
        now = i
        for j in range(h): # 가로선 내려가는 반복문
            if board[j][now] == 1: # 현재 자리가 가로선이면 오른쪽으로 이동
                now += 1
            elif now>0 and board[j][now-1] == 1: # 왼쪽에 가로선이 있으면 왼쪽으로 이동
                now -= 1
        if now != i:
            return False
    return True

# dfs 백트래킹으로 탐색
def dfs(x, y, k):
    global ans

    # 현재 상태가 조건을 만족하면 정답 갱신후 종료
    if check():
        ans = min(k, ans)
        return
    # 현재 상태에서 가로선 3개를 놓아도 자기자리로 돌아오지 못하면 종료
    elif k >= 3 or ans <= k:
        return
    # 가로선 놓기
    for i in range(x, h): # 행 반복문
        if i == x: # 현재 행을 확인하는 경우
            now = y # 파라미터로 들어온 세로선부터 검사
        else: # 다른 행이면 
            now = 0 # 첫번째 세로선부터 처음부터 검사
        for j in range(now, n-1): # 세로선 탐색
            if not board[i][j] and not board[i][j+1]: # 현재 자리에 선이 없고 오른쪽에도 선이 없을 때
                if j > 0 and board[i][j-1]: # 왼쪽에 선이 있으면
                    continue
                board[i][j] = 1 # 현재 자리에 선 놓고 이동
                dfs(i, j+2, k+1)
                board[i][j] = 0


n, m, h = map(int, input().split())
board = [[0]*n for _ in range(h)]

# 사다리에 가로선 표시
for _ in range(m):
    line, height = map(int, input().split())
    board[line-1][height-1] = 1

ans = 4 # 최댓값으로 초기화
dfs(0, 0, 0)
print(ans if ans <= 3 else -1)