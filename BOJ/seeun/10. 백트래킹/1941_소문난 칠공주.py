girls = [] # 반 학생들 입력 받을 배열
visited = [[0]*5 for _ in range(5)]
link = 0
res = 0
princess = [] # 7공주 모을 배열
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check(num):
    global link    
    r = num // 5
    c = num % 5
    for d in range(4):
        nx = r + dx[d]
        ny = c + dy[d]
        if not (0 <= nx < 5 and 0 <= ny < 5) or visited[nx][ny]:
            continue
        nextNum = nx*5+ny   # 다음 숫자
        if nextNum in princess:    # p에 있다면 방문표시, 재귀로 다음 숫자 넘겨 재검사
            visited[nx][ny] = 1
            link += 1
            check(nextNum)

def dfs(depth, start, cnt):
    global link, res, visited
    if cnt >= 4 or 25-start<7-depth: # 도연이가 4명 이상이거나 남은사람이 더 적으면
        return
    if depth == 7: # 7명 골랐는데
        link = 1
        visited = [[0]*5 for _ in range(5)]
        x, y = princess[0]//5, princess[0]%5
        visited[x][y] = 1
        check(princess[0]) 
        if link == 7: #조건만족하면 +1
            res+= 1
        return
    
    x = start//5
    y = start%5

    if girls[x][y] == "Y":
        princess.append(start)
        dfs(depth+1, start+1, cnt+1)
        princess.pop()
    else:                           # "S"이면 그냥 넘기기 
        princess.append(start)
        dfs(depth+1, start+1, cnt)
        princess.pop()

    dfs(depth, start+1, cnt)

# Main
girls = [input() for _ in range(5)] #일차원 배열로 입력 받기

dfs(0,0, 0)
print(res)