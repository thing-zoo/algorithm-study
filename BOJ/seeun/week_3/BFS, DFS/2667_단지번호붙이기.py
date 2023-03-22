n = int(input())

stack = []
cnt = 0
home = 0
homeList = []
def dfs(i, j):
    global home
    stack.append([i, j])
    if i<0 or i>=n or j<0 or j>= n:
        return False
    if town[i][j] == 1:
        town[i][j] = 0
        home += 1
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)
        return True
    else: False

town = []
for i in range(n):
    tmp = list(input())
    tmp = list(map(int, tmp))
    town.append(tmp)

for i in range(n):
    for j in range(n):
        if town[i][j] == 1:
            cnt += 1
            home = 0
            dfs(i, j)
            homeList.append(home)

print(cnt)
homeList.sort()
for i in range(cnt):
    print(homeList[i])