n, k = map(int, input().split())
nums = list(map(int, input().split()))
ans = n+1

s = 0
e = k-1
cnt = nums[:e].count(1)
    
for s in range(n):
    while e < n and cnt < k: # e가 범위를 벗어나거나 라이언을 k개 모으면 종료
        if nums[e] == 1:
            cnt += 1
        e += 1

    if cnt >= k: # k개 이상 모였으면
        ans = min(ans, e-s) # 정답 갱신

    if nums[s] == 1: # s 옮기기 전 개수 빼주기
        cnt -= 1
        
print(ans if ans != n+1 else -1)