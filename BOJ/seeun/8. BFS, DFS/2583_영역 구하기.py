import sys
sys.setrecursionlimit(10001)
stack = []
cnt = 0
def dfs(i, j):
    global cnt
    if i<0 or i>=n or j<0 or j>=m:
        return False
    if space[i][j] == 0:
        cnt +=1
        space[i][j] = 1
        dfs(i-1, j)
        dfs(i, j-1)
        dfs(i, j+1)
        dfs(i+1, j)
        
        return True
    else:
        return False

n, m, k = map(int, input().split())

space = [[0]*m for _ in range(n)]
for i in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            space[i][j] = 1

res = []
resnum = 0
for i in range(n):
        for j in range(m):
            if space[i][j] == 0:
                cnt = 0
                resnum += 1
                dfs(i, j)
                res.append(cnt)

res.sort()
print(resnum)
print(*res)