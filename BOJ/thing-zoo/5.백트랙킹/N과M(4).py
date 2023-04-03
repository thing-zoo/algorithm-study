def f():
    if len(result) == m:
        print(*result)
        return
    for i in range(1, n+1):
        if result and result[-1] > i: #내림차순이면
            continue # 건너뛰기
        result.append(i)
        f()
        result.pop()
n, m = map(int, input().split())
result = []
f()