import sys
sys.setrecursionlimit(250003)

stack = []
cnt = 0
def dfs(i, j):
    stack.append([i, j])
    global cnt
    if i < 0 or i >= n or j < 0 or j >= m:
        return 0
    if paint[i][j] == 1:
        paint[i][j] = 0
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i+1, j)
        dfs(i, j-1)
        cnt += 1
        return cnt
    else: return 0

n, m = map(int, input().split())

paint = []
for i in range(n):
    tmp = list(map(int, input().split()))
    paint.append(tmp)

paint_num = 0
paint_volume=[]
for i in range(n):
    for j in range(m):
        tmp = dfs(i, j)
        paint_volume.append(tmp)
        cnt = 0
        if tmp:
            paint_num += 1

print(paint_num)
print(max(paint_volume))