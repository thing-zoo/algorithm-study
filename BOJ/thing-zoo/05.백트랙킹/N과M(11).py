def f():
    if len(result) == m:
        print(*result)
        return
    for i in data:
        result.append(i)
        f()
        result.pop()
result = []
n, m = map(int, input().split())
data = set(map(int, input().split()))
data = list(data)
data.sort() # 오름차순 정렬
f()