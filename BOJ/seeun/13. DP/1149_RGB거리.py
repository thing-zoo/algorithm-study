import sys
input = sys.stdin.readline
n = int(input())
color = []
color.append([0, 0, 0])
for _ in range(n):
    color.append(list(map(int, input().rstrip().split())))

paint = [[0]*3 for _ in range(n+1)]
paint[1] = color[1]
# paint[i][k] : i번째 집 색깔이 k일때 최솟값
for i in range(2, n+1):
    paint[i][0] = color[i][0] + min(paint[i-1][1], paint[i-1][2])
    paint[i][1] = color[i][1] + min(paint[i-1][0], paint[i-1][2])
    paint[i][2] = color[i][2] + min(paint[i-1][0], paint[i-1][1])

# print(paint)
print(min(paint[n]))