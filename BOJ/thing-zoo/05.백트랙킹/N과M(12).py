def f():
    if len(result) == m:
        print(*result)
        return
    for i in data:
        if result and result[-1] > i: # 내림차순이면
            continue # 건너뛰기
        result.append(i)
        f()
        result.pop()
result = []
n, m = map(int, input().split())
data = set(map(int, input().split())) # 중복 숫자 제거
data = list(data)
data.sort() # 오름차순 정렬
f()