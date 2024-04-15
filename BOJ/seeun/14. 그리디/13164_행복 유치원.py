n, k = map(int, input().split())
nums = list(map(int, input().split()))

gap = []
# 각 사람 별 차이 저장
for i in range(1,n):
    gap.append(nums[i]-nums[i-1])

# 차이가 큰 순서대로 저장
sorted_gap = list(sorted(gap, reverse = True))

# 큰 순서대로 k-1개 제외하고 차이 모두 더함
print(sum(sorted_gap[k-1:]))