from collections import defaultdict
n, k = map(int, input().split())
nums = list(map(int, input().split()))

cnt = defaultdict(int)
maxlen = 0 # 현재 길이 저장
ans = 0 # 정답 저장
r = 0
for l in range(n):
    while r < n and cnt[nums[r]] < k: # 겹치는것이 k개 이상이 되면 멈춤
        cnt[nums[r]] += 1
        maxlen += 1
        r += 1
    ans = max(ans, maxlen) # 정답 갱신
    if r == n: # 오른쪽 포인터가 끝까지 갔으면 멈춤
        break
    
    cnt[nums[l]] -= 1 # 왼쪽포인터 옮기기 전에 개수 없애주기
    maxlen -= 1 # 길이도 줄여주기
print(ans)