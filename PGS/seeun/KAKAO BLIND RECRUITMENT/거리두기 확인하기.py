from collections import deque
n = 5
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def check(x, y, board):
    # 멘헤튼 거리가 2인 곳들을 탐색
    # 가는 길에 파티션 있으면 ㄱㅊ
    queue = deque()
    visited = [[False]*n for _ in range(n)]
    
    queue.append([x, y, 0])
    visited[x][y] = True
    while queue:
        x, y, dist = queue.popleft()
        if dist > 2:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and board[nx][ny] == 'O': # 빈테이블인 경우에만 탐색
                    queue.append([nx, ny, dist + 1])
                if not visited[nx][ny] and board[nx][ny] == 'P' and dist+1<=2: # 멘헤튼 거리 2 이내에 사람 있으면
                    return 0 # 바로 오답
    return 1

def solution(places):
    answer = []

    for p in places:
        ans = 1
        for i in range(n):
            for j in range(n):
                if p[i][j] == 'P':
                    res = check(i, j, p)
                    if res == 0: # 한명이라도 거리두기를 지키지 않으면
                        i, j = n-1, n-1 # 종료
                        ans = 0
                        break
        answer.append(ans)
        
    return answer