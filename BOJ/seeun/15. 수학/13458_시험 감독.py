import math
n = int(input())
nums = list(map(int, input().split()))
b, c = map(int, input().split())
ans = 0
for i in range(n):
    if nums[i]<b: # 총감독 한명으로 커버 되면 한명만 더함
        ans += 1
    else: # 더 필요하면 부감독 필요한 인원 계산
        ans += 1
        ans += math.ceil((nums[i]-b) / c)
print(ans)