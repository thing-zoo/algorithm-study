n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	
visited = [0]*n
cnt = 0

def dfs(x, y):
    global cnt
    visited[y] = 1
    stack.append(x)
    for i in range(n): # 돌면서 연결된거 있으면 dfs 돌기
            if i != y and computers[y][i] == 1 and visited[i] == 0:
                print("connected", y, i)
                dfs(y, i)

for i in range(n):
    for j in range(n):
        if  computers[i][j] == 1 and  visited[j] == 0: # 연결되어있고 아직 안세아렸으면 시작
            print("start!", i, j)
            cnt += 1 # 새로운 네트워크 셀 때마다 +1
            stack = []
            visited[i] = 1
            dfs(i, j)
           
print(cnt)
