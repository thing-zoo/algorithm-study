def dfs(res):
    if len(res) == m:
        print(*res)
        return
    for i in range(1, n+1):
        dfs(res + [i])
    
n, m = map(int, input().split())
dfs([])