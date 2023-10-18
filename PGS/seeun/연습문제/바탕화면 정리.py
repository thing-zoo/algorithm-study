def solution(wallpaper):
    answer = []
    n = len(wallpaper)
    m = len(wallpaper[0])
    lux, luy, rdx, rdy = float('inf'), float('inf'), 0, 0
    
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == "#":
                lux = min(lux, i) # 가장 위쪽 행
                luy = min(luy, j) # 가장 왼쫄 열
                rdx = max(rdx, i) # 가장 아래쪽 행
                rdy = max(rdy, j) # 가장 오른쪽 열
    
    answer = [lux, luy, rdx+1, rdy+1]
    return answer