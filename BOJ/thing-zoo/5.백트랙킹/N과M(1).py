def f():
    if len(result) == m: # m개를 모두 택했으면 탈출
        print(*result)
        return
    for i in range(1, n+1): # 1~n까지의 수에 대해
        if not visited[i]:  # 아직 i를 방문안했다면
            visited[i] = True   # 방문표시
            result.append(i)    # k번째수를 i로
            f()                 # 다음수를 정하러
            visited[i] = False  # 방문표시 취소
            result.pop()        # 값 다시 빼기

n, m = map(int, input().split())
result = []
visited = [False]*(n+1)
f()