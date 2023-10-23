def solution(park, routes):
    answer = []
    n = len(park)
    m = len(park[0])
    dog = [0, 0]
    
    for i in range(n):
        for j in range(m):
            if park[i][j] == "S":
                dog = [i, j]
                break
    # 북, 동, 남, 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dir = {"N": 0, "E":1, "S":2, "W": 3}
    x, y = dog[0], dog[1]
    
    print(x,y)
    for r in routes:
        safe = 0
        nx, ny = x, y
        for _ in range(int(r[2])):
            nx += dx[dir[r[0]]]
            ny += dy[dir[r[0]]]

            if 0 <= nx < n and 0 <= ny < m and (park[nx][ny] == "O" or park[nx][ny] == "S"):
                safe += 1
            else: # 범위벗어나거나 장애물 만나면 그냥 멈춤
                break
                
        if safe == int(r[2]):
            x, y = nx, ny
            
        print(x, y)
    answer = [x, y]
                 
    return answer