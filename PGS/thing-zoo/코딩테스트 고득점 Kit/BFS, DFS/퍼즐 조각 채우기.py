import copy
def dfs(graph, y, x, pos, n, key):
    dx = [1,0,-1,0]; dy = [0,1,0,-1]
    graph[y][x] = 2 # 방문표시
    result = [pos]  # 이동 기준이 되는 점
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if graph[ny][nx] == key:
                result += dfs(graph, ny, nx, [pos[0]+dy[i], pos[1]+dx[i]], n, key)
    return result

def rotate(table):
    n = len(table)
    rotated = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1] = table[i][j]
    return rotated
        
def solution(game_board, table):
    answer = 0
    n = len(game_board)
    # game_board의 빈칸 좌표를 구해서 (0,0)좌표를 기준으로 옮기기
    blank = []
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0: # 방문안한 빈칸이면
                blank.append(dfs(game_board, i, j, [0,0], n, 0))
    
    for _ in range(4): # table을 회전시키면서 
        table = rotate(table)
        copy_table = copy.deepcopy(table)
        for i in range(n): # table의 퍼즐 조각 좌표를 구해서 (0,0)좌표를 기준으로 옮기기
            for j in range(n): 
                if table[i][j] == 1: # 방문안한 조각이면
                    piece = dfs(copy_table, i, j, [0,0], n, 1)
                    if piece in blank: # 만약 빈칸에 해당하는 조각이 있다면
                        blank.remove(piece)  # 해당 빈칸 삭제
                        answer += len(piece) # 조각 수 카운트
                        table = copy.deepcopy(copy_table) # 방문표시 업데이트
                    else:
                        copy_table = copy.deepcopy(table) # 방문표시 초기화
    return answer
game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
print(solution(game_board, table))