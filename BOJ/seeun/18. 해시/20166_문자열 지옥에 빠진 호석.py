from collections import defaultdict
n, m, k = map(int, input().split())
map = [list(input()) for _ in range(n)]

dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, -1, 1]
strs = defaultdict(int)

def dfs(x, y, string, num):
    strs[string] += 1 # 현재 문자열 딕셔너리에 저장
    if num == 5: # 신이 좋아하는 최대 문자열 길이: 5
        return
    for i in range(8): # 8방향으로 탐색 가능
        nx = (x + dx[i])%n # 범위 벗어나도 반대 방향으로 갈 수 있음
        ny = (y + dy[i])%m

        dfs(nx, ny, string+map[nx][ny], num+1)
    

for i in range(n):
    for j in range(m):
        # 모든 위치에서 탐색 시작 가능
        dfs(i, j, map[i][j], 1)

for _ in range(k):
    string = input()
    print(strs[string])