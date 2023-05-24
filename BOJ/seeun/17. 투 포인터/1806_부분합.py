n, s = map(int, input().split())
nums = list(map(int, input().split()))

ans = n+1
j = 0
total = nums[0]
for i in range(n):
    while j<n and total < s:
        j += 1
        if j != n:
            total += nums[j]
    if j == n:
        break
    ans = min(ans, j-i+1) # 더 짧은 길이로 갱신
    total -= nums[i] # i를 오른쪽으로 한칸 옮기기 전에 total에서 i값 빼주기
if ans == n+1:
    ans = 0

print(ans)
