k, n = map(int, input().split())
lans = [] # k개의 랜선 배열
for _ in range(k):
    lans.append(int(input()))
lans.sort() # 정렬하기

answer = 0 # n개 이상 만드는 최대 랜선 길이
start = 1
end = lans[-1] # 가장 큰 랜선길이
while start <= end:
    mid = (start + end)//2
    count = 0
    for lan in lans:
        count += lan//mid # 랜선 개수 세기
    if count >= n: # n개 이상 나오면
        answer = max(answer, mid) # 결과 업데이트
        start = mid + 1 # 더 큰 수로
    else:
        end = mid - 1 # 더 작은 수로
print(answer)