n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()

answer = 2e9
end = 0
for start in range(n): # start에 대해
    while end < n and a[end] - a[start] < m: # 조건을 충족하는 첫번째 인덱스 찾기
        end += 1
    if end == n: # 범위를 벗어나면
        break # 종료
    answer = min(answer, a[end]-a[start]) # 정답 갱신
    # 다음 start값은 현재값이상일것이므로 현재 end를 유지
print(answer)