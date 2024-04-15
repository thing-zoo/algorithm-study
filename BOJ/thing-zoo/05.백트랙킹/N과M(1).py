def dfs(res):
    if len(res) == m:
        print(*res)
        return
    for i in range(1, n+1):
        if i not in res:
            res.append(i)
            dfs(res)
            res.remove(i)
    
n, m = map(int, input().split())
dfs([])