def f():
    if len(result) == m:
        print(*result)
        return
    for i in data:
        if result and result[-1] > i: # 내림차순이면
            continue # 건너뛰기
        if result.count(i) < cnt[i]: # 중복 횟수 만큼만 포함 가능
            result.append(i)
            f()
            result.pop()
n, m = map(int, input().split())
data = list(map(int, input().split()))
cnt = {} # 숫자의 중복 횟수 세기
for i in data:
    if i not in cnt:
        cnt[i] = 1
    else:
        cnt[i] += 1
result = []
data = list(set(data)) # 중복 제거: 같은자리에 같은숫자가 오면 안됨
data.sort() # 오름차순 정렬
f()