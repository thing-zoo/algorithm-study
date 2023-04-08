def f():
    if len(result) == m:
        print(*result)
        return
    for i in data:
        result.append(i)
        f()
        result.pop()
n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
result = []
f()