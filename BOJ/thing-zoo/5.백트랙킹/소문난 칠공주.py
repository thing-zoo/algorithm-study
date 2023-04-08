from collections import deque
def bfs(princess): # 7명이 인접하는지 확인
    dx = [1,0,-1,0]; dy = [0,1,0,-1]
    s = [ [0]*5 for _ in range(5) ]
    for i in princess:
        s[i//5][i%5] = 1 # 이다솜파 표시
    q = deque()
    q.append([i//5, i%5])
    s[i//5][i%5] = -1 # 방문표시
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and s[nx][ny] != -1:
                if s[nx][ny] == 1: # 이다솜파면
                    s[nx][ny] = -1 # 방문표시
                    q.append([nx, ny])
                    count += 1 # 카운트
    return count

def dfs(k, y): # k: 조합을 위해 다음 인덱스를 넘겨줌, y: 임다연파 카운트
    global answer
    if y >=4:  # 임다연파가 4명이상이면
        return # 조건에 안맞으므로 종료
    if len(princess) == 7: # 7명이면
        if bfs(princess) == 7: # 인접하면
            answer += 1 # 카운트
        return
    for i in range(k, 25): #5*5를 0~24로 표현
        if i not in princess:
            if grahp[i//5][i%5] == "Y": 
                y += 1
            princess.append(i)
            dfs(i+1, y)
            if grahp[i//5][i%5] == "Y": 
                y -= 1
            princess.pop()

grahp = [ input() for _ in range(5) ]
princess = []
answer = 0
dfs(0, 0) # 25명중 이다솜파가 적어도 4명이상인 7명 선택하기
print(answer)