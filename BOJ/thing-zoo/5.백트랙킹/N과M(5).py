def f():
    if len(result) == m:
        print(*result)
        return
    for i in data:
        if i not in result:
            result.append(i)
            f()
            result.pop()

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort() # 오름차순으로 정렬
result = []
f()