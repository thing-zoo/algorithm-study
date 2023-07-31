import sys
input = sys.stdin.readline
n = int(input())
color = []
color.append([0, 0, 0])
for _ in range(n):
    color.append(list(map(int, input().rstrip().split())))

ans = float('inf')
for c in range(3):
    # paint[i][k] : i번째 집 색깔이 k일때 최솟값
    paint = [[-1]*3 for _ in range(n+1)]
    paint[1] = [float('inf'), float('inf'), float('inf')] # 첫번째 집은 다른 색깔로 짓지 않겠다
    paint[1][c] = color[1][c] # 첫번째 집 색깔이 무조건 c일때

    for i in range(2, n+1): # 이후 집들의 색깔을 정함
        paint[i][0] = color[i][0] + min(paint[i-1][1], paint[i-1][2])
        paint[i][1] = color[i][1] + min(paint[i-1][0], paint[i-1][2])
        paint[i][2] = color[i][2] + min(paint[i-1][0], paint[i-1][1])

    paint[n][c] = float('inf') # 첫번째 색깔과달라야 하기 때문에 n번째는 c가 될 수 없다
    ans = min(ans, min(paint[n])) # 최솟값 갱신

print(ans)