n = int(input())
k = int(input())
nums = list(map(int, input().split()))
gap = []
nums.sort()

# 센서 별 거리
for i in range(1,n):
    gap.append(nums[i]-nums[i-1])

gap.sort()
ans = 0

# 간격이 가장 큰 곳 k-1개 제외하고 모두 더하기
for i in range(len(gap)-(k-1)):
    ans += gap[i]
print(ans)