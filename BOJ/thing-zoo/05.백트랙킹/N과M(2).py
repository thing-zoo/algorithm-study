def f():
    if len(result) == m:
        print(*result)
        return
    for i in range(1, n+1):
        if not visited[i]:
            if result and result[-1] > i: 
                continue # 오름차순이 아니면 넘기기
            visited[i] = True
            result.append(i)
            f()
            visited[i] = False
            result.pop()
n, m = map(int, input().split())
visited = [False]*(n+1)
result = []
f()