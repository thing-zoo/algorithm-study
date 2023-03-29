from collections import deque
def item(graph, characterX, characterY, itemX, itemY):
    dist = [[0]*102 for _ in range(102)]
    dx = [1,0,-1,0]; dy = [0,1,0,-1]
    q = deque()
    q.append([characterY, characterX])
    dist[characterY][characterX] = 1
    while q:
        y,x = q.popleft()
        if y == itemY and x == itemX:
            return dist[y][x]//2
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny <= 101 and 0 <= nx <= 101 and not dist[ny][nx]:
                if graph[ny][nx] == 1:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append([ny,nx])
def frame(graph):
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                if y1 < i < y2 and x1 < j < x2: #사각형의 내부면
                    graph[i][j] = 0  # 내부 칠하기
                if graph[i][j] != 0: # 다른사각형의 내부가 아니면
                    graph[i][j] = 1  # 테두리 칠하기

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [ [-1]*102 for _ in range(102) ] # 붙어있는 테투리때문에 2배로 확장
    frame(graph)
    answer = item(graph, characterX*2, characterY*2, itemX*2, itemY*2)
    return answer

rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
characterX = 1
characterY = 3
itemX = 7
itemY = 8
print(solution(rectangle, characterX, characterY, itemX, itemY))