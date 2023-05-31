from collections import defaultdict
def dfs(x, y, sub_string): # dfs로 (x, y)에서부터 모든방향에서의 5칸 내 부분문자열 찾기
    if len(sub_string) <= 5: # 5칸 이내면
        d[sub_string] += 1 # 부분문자열 카운트
    if len(sub_string) == 5: # 5칸이 되면
        return # 종료
    for i in range(8): # 8방향
        nx = (x + dir[i][0])%n # 환형 이동
        ny = (y + dir[i][1])%m
        dfs(nx, ny, sub_string + board[nx][ny]) # 다음문자열 추가

dir = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(-1,-1),(1,-1)] # 상하좌우대각선
n, m, k = map(int, input().split())
board = [input() for _ in range(n)]
d = defaultdict(int) # 모든 부분문자열 저장
for i in range(n):
    for j in range(m):
        dfs(i, j, board[i][j])
for _ in range(k):
    print(d[input()]) # 해당 문자열에 대한 개수 출력