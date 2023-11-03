n = int(input())
a = list(map(int, input().split()))
answer = 1
result = [1]*n # i에서 밟을 수 있는 최대 개수
for i in range(1, n):
    max_count = 1
    for j in range(i): # i에서 밟을 수 있는 최대 개수 찾기
        if a[j] < a[i]: # 현재값보다 작은 이전값에 대해
            max_count = max(max_count, result[j] + 1) # 이전값 + 1 과 기존값 비교
    result[i] = max_count
print(max(result)) # 최댓값 찾기